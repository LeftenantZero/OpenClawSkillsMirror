"""football-data.co.uk CSV adapter — the primary, fully-legal data source.

Downloads per-season CSVs (opening & closing odds + results) for the major
leagues. Site: https://www.football-data.co.uk/notes.txt
Data is redistributed freely for non-commercial use with attribution.

Column naming convention (critical — was wrong in v0.1):
  - Non-C columns (B365H, PSH, ...)  = OPENING odds
  - C-suffix columns (B365CH, PSCH, ...) = CLOSING odds
"""
from __future__ import annotations

import io
import logging
from typing import Optional

import pandas as pd
import requests

from ..config import BASE_URL, LEAGUE_CODES, RAW_DIR, ensure_dirs
from .schema import Match

log = logging.getLogger(__name__)

# Bookmaker prefixes for opening odds (non-C columns).
_OPEN_PREFIXES = ["B365", "BW", "IW", "PS", "WH", "VC"]

# Closing odds use C-suffix: "B365C", "BWC", "IWC", "PSC", "WHC", "VCC".
# Max and Avg only exist as closing.
_CLOSE_PREFIXES = [
    ("B365", "B365C"), ("BW", "BWC"), ("IW", "IWC"),
    ("PS", "PSC"), ("WH", "WHC"), ("VC", "VCC"),
    ("Max", "MaxC"), ("Avg", "AvgC"),
]


class FootballDataUKAdapter:
    """Downloads and parses football-data.co.uk season CSVs."""

    def __init__(self, cache: bool = True, timeout: int = 30):
        self.cache = cache
        self.timeout = timeout
        ensure_dirs()

    def _fetch_csv(self, season: str, league: str) -> pd.DataFrame:
        url = BASE_URL.format(season=season, league=league)
        local = RAW_DIR / f"{season}_{league}.csv"

        if self.cache and local.exists():
            return pd.read_csv(local, encoding="latin-1")

        log.info("Downloading %s %s from %s", league, season, url)
        resp = requests.get(url, timeout=self.timeout)
        resp.raise_for_status()
        content = resp.content
        if self.cache:
            local.write_bytes(content)
        return pd.read_csv(io.BytesIO(content), encoding="latin-1")

    def fetch(self, league: str, seasons: list[str]) -> list[Match]:
        if league not in LEAGUE_CODES:
            raise ValueError(
                f"Unknown league '{league}'. Known: {list(LEAGUE_CODES)}"
            )
        league_name = LEAGUE_CODES[league]
        matches: list[Match] = []
        for season in seasons:
            try:
                df = self._fetch_csv(season, league)
            except requests.RequestException as exc:
                log.warning("Failed %s %s: %s", league, season, exc)
                continue
            matches.extend(self._parse(df, league, league_name))
        log.info("Parsed %d matches for %s", len(matches), league)
        return matches

    @staticmethod
    def _parse(df: pd.DataFrame, league: str, league_name: str) -> list[Match]:
        matches: list[Match] = []
        df = df.dropna(subset=["Date", "HomeTeam", "AwayTeam"]).copy()
        df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
        df = df.dropna(subset=["Date"])

        for _, row in df.iterrows():
            odds_open = _extract_open(row)
            odds_close = _extract_close(row)
            ou25 = _extract_ou25(row)
            ah = _extract_ah(row)
            hg = _safe_int(row.get("FTHG"))
            ag = _safe_int(row.get("FTAG"))
            matches.append(
                Match(
                    date=row["Date"].strftime("%Y-%m-%d"),
                    league=league,
                    league_name=league_name,
                    home=str(row["HomeTeam"]).strip(),
                    away=str(row["AwayTeam"]).strip(),
                    home_goals=hg,
                    away_goals=ag,
                    odds_1x2=odds_close,
                    odds_open_1x2=odds_open,
                    odds_ou25=ou25,
                    asian_handicap=ah,
                )
            )
        return matches


def _extract_open(row: pd.Series) -> dict[str, tuple[float, float, float]]:
    """Opening 1X2 odds (non-C columns). Key = short bookmaker code."""
    out: dict[str, tuple[float, float, float]] = {}
    for prefix in _OPEN_PREFIXES:
        h = _safe_float(row.get(f"{prefix}H"))
        d = _safe_float(row.get(f"{prefix}D"))
        a = _safe_float(row.get(f"{prefix}A"))
        if h and d and a and h > 0 and d > 0 and a > 0:
            out[prefix] = (h, d, a)
    return out


def _extract_close(row: pd.Series) -> dict[str, tuple[float, float, float]]:
    """Closing 1X2 odds (C-suffix columns). Key = short bookmaker code."""
    out: dict[str, tuple[float, float, float]] = {}
    for short, col_prefix in _CLOSE_PREFIXES:
        h = _safe_float(row.get(f"{col_prefix}H"))
        d = _safe_float(row.get(f"{col_prefix}D"))
        a = _safe_float(row.get(f"{col_prefix}A"))
        if h and d and a and h > 0 and d > 0 and a > 0:
            out[short] = (h, d, a)
    return out


def _extract_ou25(row: pd.Series) -> dict[str, tuple[float, float]]:
    """Over/Under 2.5 closing odds. Key = book code."""
    out: dict[str, tuple[float, float]] = {}
    # P>2.5 / P<2.5 (Pinnacle), B365>2.5 / B365<2.5, etc.
    for prefix, col_pfx in [("B365", "B365"), ("PS", "P"), ("Max", "Max"), ("Avg", "Avg")]:
        over = _safe_float(row.get(f"{col_pfx}>2.5"))
        under = _safe_float(row.get(f"{col_pfx}<2.5"))
        if over and under and over > 0 and under > 0:
            out[prefix] = (over, under)
    return out


def _extract_ah(row: pd.Series) -> dict[str, tuple[float, float, float]]:
    """Asian handicap closing: {book: (line, home_water, away_water)}."""
    out: dict[str, tuple[float, float, float]] = {}
    line = _safe_float(row.get("AHh"))
    if line is None:
        return out
    for prefix, (h_col, a_col) in [
        ("B365", ("B365CAHH", "B365CAHA")),
        ("PS", ("PCAHH", "PCAHA")),
        ("Max", ("MaxCAHH", "MaxCAHA")),
        ("Avg", ("AvgCAHH", "AvgCAHA")),
    ]:
        hw = _safe_float(row.get(h_col))
        aw = _safe_float(row.get(a_col))
        if hw and aw and hw > 0 and aw > 0:
            out[prefix] = (line, hw, aw)
    return out


def _safe_float(val) -> Optional[float]:
    if val is None:
        return None
    try:
        f = float(val)
    except (TypeError, ValueError):
        return None
    import math
    return None if math.isnan(f) else f


def _safe_int(val) -> Optional[int]:
    f = _safe_float(val)
    return None if f is None else int(f)
