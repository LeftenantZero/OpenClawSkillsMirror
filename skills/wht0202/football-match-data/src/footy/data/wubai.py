"""500.com 百家欧赔适配器 — 30+ real bookmaker odds per match.

Source: https://odds.500.com/fenxi/ouzhi-{fixture_id}.shtml

Page structure: each bookmaker row contains an inner table with TWO rows:
  - Row 1 (tr_bdb): Opening odds (初盘)
  - Row 2: Current/live odds (即时盘)

Also extracts company ID from the "同" history link:
  /fenxi1/ouzhi_same.php?cid={company_id}&win=X.XX&draw=X.XX&lost=X.XX&fixtureid={id}

Parsing approach: find each <tr class="tr2" id="X">, track <tr>/</tr> depth
to find the correct closing </tr> (avoiding inner table confusion), then
parse the inner pl_table_data for opening + current odds.
"""
from __future__ import annotations

import logging
import re
from typing import Optional

import requests

log = logging.getLogger(__name__)

BASE = "https://odds.500.com"

# Known company ID → name mapping
CID_NAMES: dict[str, str] = {
    "293": "威廉希尔", "5": "澳门", "2": "立博", "3": "Bet365",
    "4": "Interwetten", "8": "SNAI", "6": "伟德", "14": "平均指数",
    "11": "Bwin", "16": "Coral", "127": "易胜博", "140": "Pinnacle",
    "15": "平博", "67": "明升", "49": "金宝博", "280": "利记",
    "9": "Unibet", "651": "1xBet", "291": "18Bet", "275": "香港马会",
    "122": "盈禾", "502": "皇冠", "348": "188BET", "1055": "Betfair",
    "863": "必发", "1": "竞彩官方",
    "1259": "1xBet", "70": "Betway", "563": "Germania Sport",
    "537": "Winning", "671": "1Bet", "451": "888Sport",
}

# Reverse: company name → CID
NAME_TO_CID: dict[str, str] = {v: k for k, v in CID_NAMES.items()}


def _fetch_page(fixture_id: str, timeout: int = 15) -> Optional[str]:
    url = f"{BASE}/fenxi/ouzhi-{fixture_id}.shtml"
    try:
        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
            timeout=timeout,
        )
        r.encoding = "gb2312"
        return r.text
    except requests.RequestException as e:
        log.warning("500.com fetch failed: %s", e)
        return None


def _extract_row_html(html: str, start_pos: int) -> str:
    """Extract full <tr>...</tr> from start_pos using depth tracking.

    Handles nested <tr>/</tr> from inner tables.
    """
    depth = 0
    pos = start_pos
    while pos < len(html):
        next_open = html.find("<tr", pos)
        next_close = html.find("</tr>", pos)

        # Skip the opening <tr> we're starting from
        if next_open == start_pos:
            pos = next_open + 3
            depth = 1
            continue

        if next_close < 0:
            break

        # If there's an opening before the next closing, increase depth
        if next_open >= 0 and next_open < next_close:
            depth += 1
            pos = next_open + 3
        else:
            depth -= 1
            if depth == 0:
                return html[start_pos:next_close + 5]
            pos = next_close + 5

    return ""


def _parse_odds_from_tds(td_texts: list[str]) -> tuple[float, float, float] | None:
    """Parse (home, draw, away) odds from a list of td text contents."""
    nums = []
    for td in td_texts:
        # Extract the number from the td content
        m = re.search(r'(\d+\.?\d*)', td)
        if m:
            nums.append(float(m.group(1)))
    if len(nums) >= 3:
        h, d, a = nums[0], nums[1], nums[2]
        if h > 1 and d > 1 and a > 1:
            return (h, d, a)
    return None


def _parse_company_rows(html: str) -> list[dict]:
    """Parse all bookmaker rows from the 500.com HTML.

    Returns list of dicts with: cid, name, open_h, open_d, open_a, cur_h, cur_d, cur_a.
    """
    results = []

    # Find all <tr class="tr1" or "tr2" id="X" markers (they alternate)
    marker_pattern = re.compile(r'<tr\s+class="tr[12]"\s+id="(\d+)"', re.IGNORECASE)

    for marker in marker_pattern.finditer(html):
        cid = marker.group(1)
        start_pos = marker.start()

        # Extract the full outer row using depth tracking
        row_html = _extract_row_html(html, start_pos)
        if not row_html:
            continue

        # ---- Extract company name ----
        name_match = re.search(
            r'<td[^>]*class="tb_plgs"[^>]*>(.*?)</td>',
            row_html, re.DOTALL,
        )
        if not name_match:
            continue

        raw_name = name_match.group(1).strip()
        raw_name = re.sub(r'<[^>]+>', '', raw_name)
        raw_name = re.sub(r'&[a-z]+;', '', raw_name)
        raw_name = re.sub(r'\([^)]*\)', '', raw_name)  # Remove (English), etc.
        raw_name = raw_name.strip().rstrip('*')

        # Map to known name
        name = CID_NAMES.get(cid, raw_name)

        # ---- Extract odds from inner pl_table_data ----
        table_match = re.search(
            r'<table[^>]*class="pl_table_data"[^>]*>(.*?)</table>',
            row_html, re.DOTALL,
        )
        if not table_match:
            continue

        table_html = table_match.group(1)

        # Find the <tr> rows inside the inner table (skip tbody)
        inner_rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL)
        if len(inner_rows) < 2:
            continue

        # Parse opening odds from first inner row
        open_tds = re.findall(r'<td[^>]*>(.*?)</td>', inner_rows[0], re.DOTALL)
        open_odds = _parse_odds_from_tds(open_tds)

        # Parse current odds from second inner row
        cur_tds = re.findall(r'<td[^>]*>(.*?)</td>', inner_rows[1], re.DOTALL)
        cur_odds = _parse_odds_from_tds(cur_tds)

        if not open_odds or not cur_odds:
            continue

        results.append({
            "cid": cid,
            "name": name,
            "open_h": open_odds[0],
            "open_d": open_odds[1],
            "open_a": open_odds[2],
            "cur_h": cur_odds[0],
            "cur_d": cur_odds[1],
            "cur_a": cur_odds[2],
        })

    return results


def _parse_url_params_fallback(html: str, fixture_id: str) -> dict[str, tuple[float, float, float]]:
    """Fallback: extract opening odds from URL params."""
    odds: dict[str, tuple[float, float, float]] = {}
    seen_cids = set()

    for m in re.finditer(
        r"cid=(\d+)&win=(\d+\.\d+)&draw=(\d+\.\d+)&lost=(\d+\.\d+)&fixtureid=" + fixture_id,
        html,
    ):
        cid = m.group(1)
        if cid in seen_cids:
            continue
        seen_cids.add(cid)
        try:
            w = float(m.group(2))
            d = float(m.group(3))
            l = float(m.group(4))
        except ValueError:
            continue
        if w <= 1 or d <= 1 or l <= 1:
            continue
        name = CID_NAMES.get(cid, f"cid_{cid}")
        if name not in odds:
            odds[name] = (w, d, l)

    return odds


def get_odds_full(fixture_id: str, timeout: int = 15) -> dict:
    """Return BOTH opening and current odds for all companies.

    Returns:
        {
            "opening": {company_name: (home, draw, away), ...},
            "current": {company_name: (home, draw, away), ...},
            "company_count": int,
            "fixture_id": str,
        }
    """
    html = _fetch_page(fixture_id, timeout)
    if not html:
        return {"opening": {}, "current": {}, "company_count": 0, "fixture_id": fixture_id}

    # Try table parser first
    rows = _parse_company_rows(html)

    opening: dict[str, tuple[float, float, float]] = {}
    current: dict[str, tuple[float, float, float]] = {}

    if rows:
        for row in rows:
            name = row["name"]
            opening[name] = (row["open_h"], row["open_d"], row["open_a"])
            current[name] = (row["cur_h"], row["cur_d"], row["cur_a"])
        log.info("500.com fixture %s: %d companies parsed", fixture_id, len(rows))
    else:
        # Fallback: use URL params (opening odds only)
        opening = _parse_url_params_fallback(html, fixture_id)
        current = {}
        log.warning("500.com fixture %s: table parser failed, URL fallback got %d companies",
                   fixture_id, len(opening))

    return {
        "opening": opening,
        "current": current,
        "company_count": max(len(opening), len(current)),
        "fixture_id": fixture_id,
    }


def get_odds(fixture_id: str, timeout: int = 15) -> dict[str, tuple[float, float, float]]:
    """Return CURRENT (live) odds: {company_name: (home, draw, away)}.

    For backward compatibility.
    """
    full = get_odds_full(fixture_id, timeout)
    if full["current"]:
        return full["current"]
    return full["opening"]


def get_opening_odds(fixture_id: str, timeout: int = 15) -> dict[str, tuple[float, float, float]]:
    """Return OPENING odds: {company_name: (home, draw, away)}."""
    full = get_odds_full(fixture_id, timeout)
    return full["opening"]


def find_fixture(team_a: str, team_b: str, timeout: int = 15) -> Optional[str]:
    """Search odds.500.com homepage for a match's fixture ID by team names."""
    try:
        r = requests.get(
            BASE + "/",
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
            timeout=timeout,
        )
        r.encoding = "gb2312"
    except requests.RequestException:
        return None

    # Find fixture blocks containing BOTH team names
    for m in re.finditer(r'/fenxi/ouzhi-(\d+)\.shtml', r.text):
        fid = m.group(1)
        start = max(0, m.start() - 500)
        end = min(len(r.text), m.end() + 500)
        ctx = r.text[start:end]
        if team_a in ctx and team_b in ctx:
            return fid

    return None


# ---- Batch collection ----
def batch_opening_odds(
    fixture_ids: list[str],
    timeout: int = 15,
) -> dict[str, dict]:
    """Fetch opening + current odds for multiple fixtures at once."""
    results = {}
    for fid in fixture_ids:
        results[fid] = get_odds_full(fid, timeout)
    return results
