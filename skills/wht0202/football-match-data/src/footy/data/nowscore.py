"""捷报网 (nowscore.com) 赔率适配器 — backup data source.

Accesses structured data JS files: /analysisJs/data{match_id}.js
Format: var v_data = [[date, league_id, ..., '1X2_H', '1X2_D', '1X2_A',
                       'AH_line', 'AH_type', 'AH_water', ...]];

Much more structured than okooo HTML — ideal as a reliable backup.
"""
from __future__ import annotations

import json
import logging
import re

import requests

from .schema import Match

log = logging.getLogger(__name__)

BASE = "https://live.nowscore.com"
DATA_URL = f"{BASE}/analysisJs/data{{match_id}}.js"
ODDS_URL = f"{BASE}/odds/match/{{match_id}}.htm"


def _fetch_data_js(match_id: str, timeout: int = 15) -> dict | None:
    """Fetch and parse a match data JS file.

    Returns dict with keys: home, away, date, odds_1x2, asian_handicap, history.
    """
    r = requests.get(
        DATA_URL.format(match_id=match_id),
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=timeout,
    )
    if r.status_code != 200:
        return None

    text = r.text

    # Extract team names — may be in JS or in the parent HTML page
    hname = ""
    aname = ""
    hm = re.search(r"var\s+h_name\s*=\s*'([^']+)'", text)
    am = re.search(r"var\s+a_name\s*=\s*'([^']+)'", text)
    if hm:
        hname = hm.group(1)
    if am:
        aname = am.group(1)

    # Fallback: try to get names from the analysis HTML page
    if not hname or not aname:
        try:
            ar = requests.get(
                f"{BASE}/analysis/{match_id}.html",
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=timeout,
            )
            ar.encoding = "utf-8"
            atext = ar.text
            hm2 = re.search(r"<title>.*?([\u4e00-\u9fff]{2,10})\s*VS\s*([\u4e00-\u9fff]{2,10})", atext, re.IGNORECASE)
            if hm2:
                hname = hm2.group(1).strip()
                aname = hm2.group(2).strip()
        except Exception:
            pass

    # Extract v_data and h_data — multi-row JSON arrays
    # Pattern: var h_data = [[row1],[row2],...];
    hd_match = re.search(r"var\s+h_data\s*=\s*(\[\[.*?\]\])", text, re.DOTALL)

    latest_odds = None

    if hd_match:
        rows_text = hd_match.group(1)
        # Fix JS → JSON: single-quoted strings
        rows_text = rows_text.replace("'", '"')
        try:
            rows = json.loads(rows_text)
            if rows:
                # Find the most recent row with FULL odds data (positions 11-13)
                for row in reversed(rows):
                    if (len(row) >= 14
                        and _safe_float(row[11]) > 1
                        and _safe_float(row[12]) > 1
                        and _safe_float(row[13]) > 1):
                        latest_row = row
                        break
                # Fallback: any row with any odds
                if not latest_row:
                    for row in reversed(rows):
                        if len(row) >= 14:
                            latest_row = row
                            break
        except json.JSONDecodeError as e:
            log.debug("JSON parse error: %s", e)
            pass

    if latest_row and len(latest_row) >= 14:
        # Row structure: [date, league_id, ..., score, H_odds, D_odds, A_odds,
        #                 AH_line, AH_type, AH_water, ...]
        # Odds are at positions 11,12,13 (1X2) and 14,15,16 (AH)
        # Some older rows may be shorter — find the best available.
        try:
            h_odd = float(latest_row[11]) if len(latest_row) > 11 and latest_row[11] else 0.0
            d_odd = float(latest_row[12]) if len(latest_row) > 12 and latest_row[12] else 0.0
            a_odd = float(latest_row[13]) if len(latest_row) > 13 and latest_row[13] else 0.0

            if h_odd > 0 and d_odd > 0 and a_odd > 0:
                latest_odds = {
                    "home": hname,
                    "away": aname,
                    "date": str(latest_row[0]) if latest_row[0] else "",
                    "odds_1x2": (h_odd, d_odd, a_odd),
                    "ah_line": str(latest_row[14]) if len(latest_row) > 14 and latest_row[14] else "",
                    "ah_type": str(latest_row[15]) if len(latest_row) > 15 and latest_row[15] else "",
                    "ah_water": float(latest_row[16]) if len(latest_row) > 16 and latest_row[16] else 0.0,
                }
        except (ValueError, IndexError, TypeError):
            pass

    return latest_odds


def fetch_match_odds(match_id: str, timeout: int = 15) -> Match | None:
    """Fetch odds for a single match by its nowscore match ID."""
    data = _fetch_data_js(match_id, timeout)
    if not data or not data.get("odds_1x2"):
        return None

    spf = data["odds_1x2"]
    if spf[0] <= 1 or spf[1] <= 1 or spf[2] <= 1:
        return None

    ah = {}
    if data.get("ah_line") and data.get("ah_water"):
        try:
            line_str = data["ah_line"]
            line = float(line_str) if line_str else 0.0
            ah["nowscore"] = (line, data["ah_water"], 0.0)
        except (ValueError, TypeError):
            pass

    return Match(
        date=data.get("date", "?")[:10],
        league="unknown",
        league_name="",
        home=data.get("home", ""),
        away=data.get("away", ""),
        home_goals=None,
        away_goals=None,
        odds_1x2={"nowscore": spf},
            asian_handicap=ah,
    )


def _safe_float(val) -> float:
    """Convert value to float, returning 0.0 on failure."""
    if val is None:
        return 0.0
    try:
        return float(val)
    except (ValueError, TypeError):
        return 0.0
