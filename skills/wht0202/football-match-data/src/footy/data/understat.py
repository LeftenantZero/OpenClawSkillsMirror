"""Understat xG adapter — expected goals for top 5 leagues.

Source: https://understat.com/
Data embedded as JSON.parse() in <script> tags on match/league pages.

Extracts: xG, xGA, shots, shots on target, deep completions, PPDA.
"""
from __future__ import annotations

import json
import logging
import re
from typing import Optional

import requests

log = logging.getLogger(__name__)

BASE = "https://understat.com"

# Understat league name → our code
LEAGUE_MAP = {
    "EPL": "E0",
    "La_liga": "SP1",
    "Bundesliga": "D1",
    "Serie_A": "I1",
    "Ligue_1": "F1",
}

# Understat → football-data.co.uk team name mapping (key players)
TEAM_MAP = {
    "Real Madrid": "Real Madrid", "Barcelona": "Barcelona",
    "Atletico Madrid": "Ath Madrid", "Athletic Club": "Ath Bilbao",
    "Manchester City": "Man City", "Manchester United": "Man United",
    "Arsenal": "Arsenal", "Chelsea": "Chelsea", "Liverpool": "Liverpool",
    "Tottenham": "Tottenham", "Newcastle United": "Newcastle",
    "Brighton": "Brighton", "Aston Villa": "Aston Villa",
    "West Ham": "West Ham", "Everton": "Everton",
    "Bayern Munich": "Bayern Munich", "Borussia Dortmund": "Dortmund",
    "RB Leipzig": "RB Leipzig", "Bayer Leverkusen": "Leverkusen",
    "Juventus": "Juventus", "AC Milan": "AC Milan",
    "Inter": "Inter", "Napoli": "Napoli", "Roma": "Roma",
    "Paris Saint Germain": "Paris SG", "Lyon": "Lyon",
    "Marseille": "Marseille", "Monaco": "Monaco",
}


def _decode_json(raw: str) -> dict | list:
    """Decode Understat's hex-escaped JSON."""
    return json.loads(raw.encode().decode("unicode_escape"))


def fetch_match(match_id: str, timeout: int = 15) -> Optional[dict]:
    """Fetch xG data for a single match."""
    try:
        r = requests.get(
            f"{BASE}/match/{match_id}",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=timeout,
        )
    except requests.RequestException:
        return None

    scripts = re.findall(r"<script[^>]*>(.*?)</script>", r.text, re.DOTALL)
    for s in scripts:
        if "match_info" in s and "JSON.parse" in s:
            m = re.search(r"JSON\.parse\('([^']+)'\)", s)
            if m:
                return _decode_json(m.group(1))
    return None


def fetch_league_matches(league: str, season: str, timeout: int = 30) -> list[dict]:
    """Fetch all match xG data for a league+season.

    league: "EPL", "La_liga", etc.
    season: "2024", "2023", etc.
    """
    try:
        r = requests.get(
            f"{BASE}/league/{league}/{season}",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=timeout,
        )
    except requests.RequestException:
        return []

    scripts = re.findall(r"<script[^>]*>(.*?)</script>", r.text, re.DOTALL)
    for s in scripts:
        if "datesData" in s and "JSON.parse" in s:
            m = re.search(r"JSON\.parse\('([^']+)'\)", s)
            if m:
                data = _decode_json(m.group(1))
                matches = []
                for date_entry in data:
                    for match in date_entry.get("matches", []):
                        matches.append(match)
                log.info("Understat %s/%s: %d matches", league, season, len(matches))
                return matches
    return []


def get_xg_for_match(match_id: str) -> Optional[dict]:
    """Return {home_xg, away_xg, home_shots, away_shots, ...} for a match."""
    data = fetch_match(match_id)
    if not data:
        return None
    return {
        "home_team": data.get("team_h", ""),
        "away_team": data.get("team_a", ""),
        "home_xg": float(data.get("h_xg", 0)),
        "away_xg": float(data.get("a_xg", 0)),
        "home_goals": int(data.get("h_goals", 0)),
        "away_goals": int(data.get("a_goals", 0)),
        "home_shots": int(data.get("h_shot", 0)),
        "away_shots": int(data.get("a_shot", 0)),
        "home_shot_on_target": int(data.get("h_shotOnTarget", 0)),
        "away_shot_on_target": int(data.get("a_shotOnTarget", 0)),
        "home_deep": int(data.get("h_deep", 0)),
        "away_deep": int(data.get("a_deep", 0)),
        "home_ppda": float(data.get("h_ppda", 0)) if data.get("h_ppda") else 0,
        "away_ppda": float(data.get("a_ppda", 0)) if data.get("a_ppda") else 0,
        "date": data.get("date", ""),
    }
