"""澳客联赛页面赔率适配器 — final working version.

League pages: https://www.okooo.com/soccer/league/{id}/
Structure: <tr> with <td>VS</td> separator, teams in adjacent tds, 3 odds in tds.
"""
from __future__ import annotations

import logging
from datetime import datetime
import re

import requests

from .schema import Match

log = logging.getLogger(__name__)

BASE = "https://www.okooo.com"
LEAGUE_IDS = {
    "E0": 17,   # 英超 (verified)
    "I1": 23,   # 意甲 (verified: 亚特兰大, 萨索洛)
    "SP1": 37,  # 西甲 (tentative)
    "D1": 19,   # 德甲 (tentative)
    "F1": 28,   # 法甲 (tentative: 16 showed intl, try 28)
    "WC": 16,   # 世界杯 (verified 2026-06-26)
}
# ⚠️ 2026-06-26: okooo returning HTTP 405 for most league pages.
# Core pipeline unaffected — use 500.com fixture IDs via ampan_analyze.py

VS_PATTERN = re.compile(r"<td[^>]*>\s*VS\s*</td>", re.IGNORECASE)
DATE_PATTERN = re.compile(r"(\d{2}-\d{2})\s+(\d{2}:\d{2})")
ODDS_PATTERN = re.compile(r">(\d+\.\d{2})<")


def _extract_team(html: str, before: bool) -> str:
    """Extract team name from td adjacent to VS."""
    if before:
        # Find last </td> before position and extract text before it
        td_end = html.rfind("</td>")
        if td_end < 0:
            return ""
        td_start = html.rfind(">", 0, td_end)
        if td_start < 0:
            return ""
        text = html[td_start + 1:td_end]
    else:
        # Find first <td...> after position and extract text
        td_start = html.find("<td")
        if td_start < 0:
            return ""
        content_start = html.find(">", td_start)
        td_end = html.find("</td>", content_start)
        if content_start < 0 or td_end < 0:
            return ""
        text = html[content_start + 1:td_end]
    # Clean: remove nested tags, strip whitespace
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&[a-z]+;", "", text)
    return text.strip()


def fetch_league_odds(league_code: str = "E0", timeout: int = 15) -> list[Match]:
    lid = LEAGUE_IDS.get(league_code)
    if not lid:
        raise ValueError(f"Unknown league: {league_code}")

    r = requests.get(
        f"{BASE}/soccer/league/{lid}/",
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
        timeout=timeout,
    )
    r.encoding = "gb2312"
    html = r.text

    matches: list[Match] = []
    seen = set()

    for vs_m in VS_PATTERN.finditer(html):
        vs_start = vs_m.start()
        vs_end = vs_m.end()

        # Find enclosing <tr>
        tr_start = html.rfind("<tr", 0, vs_start)
        tr_end = html.find("</tr>", vs_end)
        if tr_start < 0 or tr_end < 0:
            continue
        row = html[tr_start:tr_end]

        # Date
        dm = DATE_PATTERN.search(row)
        if not dm:
            continue
        month_day = dm.group(1)
        hour_min = dm.group(2)

        # Team A (before VS)
        before = row[:row.find("VS")]
        team_a = _extract_team(before, before=True)
        # Team B (after VS)
        after = row[row.find("VS") + 2:]
        team_b = _extract_team(after, before=False)

        if not team_a or not team_b:
            continue

        # Odds: find 3 consecutive decimal numbers
        odds = ODDS_PATTERN.findall(row)
        if len(odds) < 3:
            continue
        try:
            odd_h = float(odds[0])
            odd_d = float(odds[1])
            odd_a = float(odds[2])
        except (ValueError, IndexError):
            continue
        if odd_h <= 1 or odd_d <= 1 or odd_a <= 1:
            continue

        key = (month_day, team_a, team_b)
        if key in seen:
            continue
        seen.add(key)

        # Date
        now = datetime.now()
        year = now.year
        try:
            mth = int(month_day[:2])
            if mth < now.month - 3:
                year += 1
            date_iso = datetime.strptime(
                f"{year}-{month_day} {hour_min}", "%Y-%m-%d %H:%M"
            ).strftime("%Y-%m-%d")
        except (ValueError, IndexError):
            date_iso = f"{year}-{month_day}"

        matches.append(
            Match(
                date=date_iso,
                league=league_code,
                league_name="",
                home=team_a,
                away=team_b,
                home_goals=None,
                away_goals=None,
                odds_1x2={"okooo": (odd_h, odd_d, odd_a)},
            )
        )
        if len(matches) >= 50:
            break

    log.info("okooo %s: %d matches", league_code, len(matches))
    return matches
