"""The Odds API adapter — live/upcoming match odds (optional).

The Odds API provides real-time odds from 40+ bookmakers. Free tier: 500
credits/month (~16 requests/day). One credit per request for most endpoints.

Usage:
    export FOOTY_ODDS_API_KEY=your_key_here
    footy odds --league E0   # fetch live odds for upcoming PL matches
"""
from __future__ import annotations

import logging
import os
from typing import Optional

import requests

from .schema import Match

log = logging.getLogger(__name__)

BASE = "https://api.the-odds-api.com/v4"
# Map league codes to The Odds API sport keys.
SPORT_KEYS = {
    # Big 5
    "E0": "soccer_epl",
    "SP1": "soccer_spain_la_liga",
    "I1": "soccer_italy_serie_a",
    "D1": "soccer_germany_bundesliga",
    "F1": "soccer_france_ligue_one",
    # Secondary Europe
    "N1": "soccer_norway_eliteserien",       # 挪超
    "FI1": "soccer_finland_veikkausliiga",   # 芬超
    "SW1": "soccer_sweden_allsvenskan",       # 瑞超
    "SW2": "soccer_sweden_superettan",        # 瑞甲
    "IR1": "soccer_league_of_ireland",        # 爱超
    "IR2": "soccer_ireland_division1",        # 爱甲
    "SC0": "soccer_scotland_premiership",     # 苏超
    "SC1": "soccer_scotland_championship",    # 苏冠
    "IS1": "soccer_iceland_pepsideild",       # 冰超
    "NED": "soccer_netherlands_eredivisie",   # 荷甲
    "POR": "soccer_portugal_primeira_liga",   # 葡超
    "BEL": "soccer_belgium_first_a",          # 比甲
    "TUR": "soccer_turkey_super_lig",         # 土超
    "DEN": "soccer_denmark_superliga",        # 丹超
    "POL": "soccer_poland_ekstraklasa",       # 波甲
    "CZE": "soccer_czech_republic_first_liga", # 捷甲
    "GRE": "soccer_greece_super_league",      # 希超
    "AUT": "soccer_austria_bundesliga",       # 奥甲
    "SWI": "soccer_switzerland_super_league", # 瑞士超
    "JPN": "soccer_japan_j_league",           # 日职
    "JPN2": "soccer_japan_j2_league",         # 日乙
    "KOR": "soccer_korea_kleague_1",          # 韩K联
    "AUS": "soccer_australia_aleague",        # 澳超
    # Americas
    "BR1": "soccer_brazil_campeonato",        # 巴甲
    "BR2": "soccer_brazil_serie_b",           # 巴乙
    "USA": "soccer_usa_mls",                  # 美职联
    "ARG": "soccer_argentina_primera_division", # 阿甲
    "MEX": "soccer_mexico_ligamx",            # 墨超
    # Asia
    "CN1": "soccer_china_superleague",        # 中超
    # England lower
    "EC": "soccer_efl_champ",                 # 英冠
    "EL1": "soccer_england_league1",          # 英甲
    # Cups / International
    "WC": "soccer_fifa_world_cup",            # 世界杯
    "WCW": "soccer_fifa_world_cup_winner",    # 世界杯冠军
    "UCL": "soccer_uefa_champions_league",    # 欧冠
    "UEL": "soccer_uefa_europa_league",       # 欧联
    "UECL": "soccer_uefa_europa_conference_league", # 欧协联
    "LIB": "soccer_conmebol_copa_libertadores",  # 解放者杯
    "SUD": "soccer_conmebol_copa_sudamericana",   # 南美杯
    "DFB": "soccer_germany_dfb_pokal",         # 德国杯
    "FAC": "soccer_england_fa_cup",            # 足总杯
}


class OddsAPIAdapter:
    """Fetch live/upcoming odds from The Odds API."""

    def __init__(self, api_key: str | None = None, timeout: int = 15):
        self.api_key = api_key or os.environ.get("FOOTY_ODDS_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No API key. Set FOOTY_ODDS_API_KEY env var or pass api_key=."
            )
        self.timeout = timeout

    def fetch_upcoming(self, league: str, regions: str = "uk") -> list[Match]:
        """Fetch upcoming matches with live 1X2 odds.

        `regions`: bookmaker region codes (uk, us, eu, au).
        """
        if league not in SPORT_KEYS:
            raise ValueError(f"Unknown league '{league}'. Known: {list(SPORT_KEYS)}")
        sport = SPORT_KEYS[league]
        url = f"{BASE}/sports/{sport}/odds/"
        params = {
            "apiKey": self.api_key,
            "regions": regions,
            "markets": "h2h",
            "oddsFormat": "decimal",
        }
        resp = requests.get(url, params=params, timeout=self.timeout)
        resp.raise_for_status()
        data = resp.json()
        log.info(
            "Odds API: %d events, %d credits remaining (header: %s)",
            len(data),
            resp.headers.get("x-requests-remaining", "?"),
        )
        return self._parse(data, league)

    @staticmethod
    def _parse(data: list, league: str) -> list[Match]:
        matches: list[Match] = []
        for ev in data:
            home = ev.get("home_team", "")
            away = ev.get("away_team", "")
            commence = ev.get("commence_time", "")
            if not home or not away:
                continue
            odds: dict[str, tuple[float, float, float]] = {}
            for bookmaker in ev.get("bookmakers", []):
                key = bookmaker.get("key", "")
                for market in bookmaker.get("markets", []):
                    if market.get("key") != "h2h":
                        continue
                    outcomes = market.get("outcomes", [])
                    vals: dict[str, float] = {}
                    for o in outcomes:
                        vals[o.get("name", "")] = o.get("price", 0)
                    h = vals.get(home, 0)
                    d = vals.get("Draw", 0)
                    a = vals.get(away, 0)
                    if h and d and a and h > 0 and d > 0 and a > 0:
                        odds[key] = (h, d, a)
            if odds:
                date_str = commence[:10] if "T" in commence else commence
                matches.append(
                    Match(
                        date=date_str,
                        league=league,
                        league_name=league,
                        home=home,
                        away=away,
                        home_goals=None,
                        away_goals=None,
                        odds_1x2=odds,
                    )
                )
        return matches
