"""500.com 大小球(O/U)盘口数据适配器 — 批量自动采集.

Source: https://odds.500.com/fenxi/daxiao-{fixture_id}.shtml

Page structure (different from European odds page):
	  Each company row has TWO separate inner tables:
	    - First pl_table_data: CURRENT O/U (即时盘) — 有涨跌箭头
	    - Second pl_table_data: OPENING O/U (初盘) — 无箭头

  Each inner table has ONE row with: over_odds | line | under_odds

Also extracts from "同" links:
  /fenxi1/daxiao_same.php?cid=X&bigpei=X.XX&handi=X.X&smallpei=X.XX&fixid=XXXXX

Integration with orchestrator:
  from footy.data.ou_data import fetch_ou_batch, MatchOU
  ou_data = fetch_ou_batch(["1335728", "1335729"])
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from typing import Optional

import requests

log = logging.getLogger(__name__)

BASE = "https://odds.500.com"

# Company ID → name (same as wubai.py)
CID_NAMES: dict[str, str] = {
    "293": "威廉希尔", "5": "澳门", "2": "立博", "3": "Bet365",
    "4": "Interwetten", "8": "SNAI", "6": "伟德", "14": "平均指数",
    "11": "Bwin", "16": "Coral", "127": "易胜博", "140": "Pinnacle",
    "15": "平博", "67": "明升", "49": "金宝博", "280": "利记",
    "9": "Unibet", "651": "1xBet", "291": "18Bet", "275": "香港马会",
    "122": "盈禾", "502": "皇冠", "348": "188BET", "1055": "Betfair",
    "863": "必发", "1": "竞彩官方",
    "1484": "澳门",  # sometimes 澳门 appears as 1484
}


@dataclass
class OUData:
    """O/U handicap data for a single bookmaker."""

    company: str
    cid: str = ""

    # Opening (初盘)
    open_line: float = 2.5      # e.g. 2.5, 2.25, 2.75
    open_over: float = 0.0      # over odds at opening
    open_under: float = 0.0     # under odds at opening

    # Current (即时)
    current_line: float = 2.5
    current_over: float = 0.0
    current_under: float = 0.0

    # Derived
    line_move: float = 0.0      # positive = deepened (升盘), negative = dropped (降盘)
    over_move: float = 0.0      # over odds change
    under_move: float = 0.0     # under odds change

    def __post_init__(self):
        self.line_move = self.current_line - self.open_line
        self.over_move = self.current_over - self.open_over
        self.under_move = self.current_under - self.open_under


@dataclass
class MatchOU:
    """Complete O/U data for a match."""

    fixture_id: str = ""
    home: str = ""
    away: str = ""
    bookmakers: list[OUData] = field(default_factory=list)

    @property
    def company_count(self) -> int:
        return len(self.bookmakers)

    @property
    def avg_open_line(self) -> float:
        if not self.bookmakers:
            return 2.5
        return sum(b.open_line for b in self.bookmakers) / len(self.bookmakers)

    @property
    def avg_current_line(self) -> float:
        if not self.bookmakers:
            return 2.5
        return sum(b.current_line for b in self.bookmakers) / len(self.bookmakers)

    @property
    def line_trend(self) -> str:
        """Overall line trend across all bookmakers."""
        if not self.bookmakers:
            return "无数据"
        moved_up = sum(1 for b in self.bookmakers if b.line_move > 0.1)
        moved_down = sum(1 for b in self.bookmakers if b.line_move < -0.1)
        stable = self.company_count - moved_up - moved_down
        total_move = self.avg_current_line - self.avg_open_line
        if total_move > 0.2:
            return f"升盘 ({total_move:+.2f}球, {moved_up}/{self.company_count}家)"
        elif total_move < -0.2:
            return f"降盘 ({total_move:+.2f}球, {moved_down}/{self.company_count}家)"
        else:
            return f"稳定 ({stable}/{self.company_count}家)"

    @property
    def trend_consensus(self) -> str:
        """Are bookmakers consistent on O/U trend?"""
        if not self.bookmakers:
            return "无数据"
        lines = [b.open_line for b in self.bookmakers]
        unique = len(set(int(l * 4) for l in lines))
        if unique <= 2:
            return "高度一致"
        elif unique <= 4:
            return "中等分歧"
        else:
            return "趋势混杂"

    @property
    def over_under_bias(self) -> str:
        """Bias toward over or under based on line movement and odds changes."""
        if not self.bookmakers:
            return "无数据"
        # Count bookmakers moving toward over (line up, over odds down)
        over_bias = sum(1 for b in self.bookmakers if b.line_move > 0.05 or b.over_move < -0.03)
        under_bias = sum(1 for b in self.bookmakers if b.line_move < -0.05 or b.under_move < -0.03)
        if over_bias > under_bias + 2:
            return "倾向大球"
        elif under_bias > over_bias + 2:
            return "倾向小球"
        else:
            return "中性"


# ---- HTML Parsing ----

def _parse_line(line_str: str) -> float:
    """Parse O/U line: '2.5'→2.5, '2/2.5'→2.25, '2.5/3'→2.75, '3'→3.0."""
    if not line_str:
        return 2.5
    line_str = line_str.strip()
    try:
        if "/" in line_str:
            parts = line_str.split("/")
            return (float(parts[0]) + float(parts[1])) / 2
        return float(line_str)
    except ValueError:
        return 2.5


def _extract_row_html(html: str, start_pos: int) -> str:
    """Extract full <tr>...</tr> using depth tracking."""
    depth = 0
    pos = start_pos
    while pos < len(html):
        next_open = html.find("<tr", pos)
        next_close = html.find("</tr>", pos)
        if next_open == start_pos:
            pos = next_open + 3
            depth = 1
            continue
        if next_close < 0:
            break
        if next_open >= 0 and next_open < next_close:
            depth += 1
            pos = next_open + 3
        else:
            depth -= 1
            if depth == 0:
                return html[start_pos:next_close + 5]
            pos = next_close + 5
    return ""


def _parse_ou_table(html: str) -> list[dict]:
    """Parse O/U rows from the daxiao page HTML.

    Returns list of dicts with: cid, name, open_line, open_over, open_under,
    cur_line, cur_over, cur_under.
    """
    results = []

    # Find rows with id attribute (both tr1 and tr2 alternating)
    marker_pattern = re.compile(r'<tr\s+class="tr[12]"[^>]*id="(\d+)"', re.IGNORECASE)

    for marker in marker_pattern.finditer(html):
        cid = marker.group(1)
        row_html = _extract_row_html(html, marker.start())
        if not row_html:
            continue

        # ---- Company name ----
        name_match = re.search(
            r'<td[^>]*class="tb_plgs"[^>]*>(.*?)</td>',
            row_html, re.DOTALL,
        )
        if not name_match:
            continue

        raw_name = name_match.group(1).strip()
        raw_name = re.sub(r'<[^>]+>', '', raw_name)
        raw_name = re.sub(r'&[a-z]+;', '', raw_name)
        raw_name = re.sub(r'\([^)]*\)', '', raw_name)
        raw_name = raw_name.strip().rstrip('*')
        name = CID_NAMES.get(cid, raw_name)

        # ---- Find both pl_table_data tables ----
        tables = re.findall(
            r'<table[^>]*class="pl_table_data"[^>]*>(.*?)</table>',
            row_html, re.DOTALL,
        )

        if len(tables) < 2:
            # Fallback: try URL params from same.php link
            same_match = re.search(
                r'daxiao_same\.php\?cid=' + cid +
                r'&bigpei=(\d+\.?\d*)&handi=([\d./]+)&smallpei=(\d+\.?\d*)',
                row_html,
            )
            if same_match:
                try:
                    open_over = float(same_match.group(1))
                    open_line = _parse_line(same_match.group(2))
                    open_under = float(same_match.group(3))
                    # No current data from URL params
                    results.append({
                        "cid": cid, "name": name,
                        "open_line": open_line, "open_over": open_over, "open_under": open_under,
                        "cur_line": open_line, "cur_over": open_over, "cur_under": open_under,
                    })
                except (ValueError, IndexError):
                    pass
            continue

        # ---- Parse CURRENT table (FIRST table, has arrows ↑↓) ----
        cur_tds = re.findall(r'<td[^>]*>(.*?)</td>', tables[0], re.DOTALL)
        cur_over, cur_line, cur_under = 0.0, 2.5, 0.0

        if len(cur_tds) >= 3:
            over_match = re.search(r'(\d+\.?\d*)', cur_tds[0])
            line_match = re.search(r'>\s*([\d./]+)\s*<', cur_tds[1]) or re.search(r'(\d+\.?\d*(?:/\d+\.?\d*)?)', cur_tds[1])
            under_match = re.search(r'(\d+\.?\d*)', cur_tds[2])

            if over_match:
                cur_over = float(over_match.group(1))
            if line_match:
                cur_line = _parse_line(line_match.group(1))
            if under_match:
                cur_under = float(under_match.group(1))

        # ---- Parse OPENING table (SECOND table, no arrows) ----
        open_tds = re.findall(r'<td[^>]*>(.*?)</td>', tables[1], re.DOTALL)
        open_over, open_line, open_under = cur_over, cur_line, cur_under

        if len(open_tds) >= 3:
            over_match = re.search(r'(\d+\.?\d*)', open_tds[0])
            line_match = re.search(r'>\s*([\d./]+)\s*<', open_tds[1]) or re.search(r'(\d+\.?\d*(?:/\d+\.?\d*)?)', open_tds[1])
            under_match = re.search(r'(\d+\.?\d*)', open_tds[2])

            if over_match:
                open_over = float(over_match.group(1))
            if line_match:
                open_line = _parse_line(line_match.group(1))
            if under_match:
                open_under = float(under_match.group(1))

        results.append({
            "cid": cid, "name": name,
            "open_line": open_line, "open_over": open_over, "open_under": open_under,
            "cur_line": cur_line, "cur_over": cur_over, "cur_under": cur_under,
        })

    return results


# ---- Public API ----

def fetch_ou(fixture_id: str, timeout: int = 15) -> Optional[MatchOU]:
    """Fetch O/U handicap data from 500.com for a single fixture.

    Args:
        fixture_id: 500.com fixture ID (e.g., '1335728')
        timeout: HTTP timeout in seconds

    Returns:
        MatchOU with all bookmaker O/U data, or None on failure.
    """
    url = f"{BASE}/fenxi/daxiao-{fixture_id}.shtml"
    try:
        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
            timeout=timeout,
        )
        r.encoding = "gb2312"
    except requests.RequestException as e:
        log.warning("500.com daxiao fetch failed for %s: %s", fixture_id, e)
        return None

    if r.status_code != 200:
        log.warning("500.com daxiao HTTP %d for %s", r.status_code, fixture_id)
        return None

    html = r.text

    # Try to extract team names from title
    home, away = "", ""
    title_match = re.search(r"<title>([^<]+)", html)
    if title_match:
        title = title_match.group(1)
        # Title format: "阿尔纳赛尔VS阿尔阿拉比(2025-2026科威联)-大小对比-500彩票网"
        vs_idx = title.find("VS")
        if vs_idx > 0:
            home = title[:vs_idx].strip()
            rest = title[vs_idx + 2:]
            paren_idx = rest.find("(")
            if paren_idx > 0:
                away = rest[:paren_idx].strip()
            else:
                away = rest.split("-")[0].strip()

    rows = _parse_ou_table(html)

    if not rows:
        log.warning("500.com daxiao: no rows parsed for %s", fixture_id)
        return None

    bookmakers = []
    for row in rows:
        bk = OUData(
            company=row["name"],
            cid=row["cid"],
            open_line=row["open_line"],
            open_over=row["open_over"],
            open_under=row["open_under"],
            current_line=row["cur_line"],
            current_over=row["cur_over"],
            current_under=row["cur_under"],
        )
        bookmakers.append(bk)

    result = MatchOU(
        fixture_id=fixture_id,
        home=home,
        away=away,
        bookmakers=bookmakers,
    )

    log.info("500.com daxiao %s: %d bookmakers, avg line %.2f→%.2f",
             fixture_id, len(bookmakers), result.avg_open_line, result.avg_current_line)

    return result


def fetch_ou_batch(
    fixture_ids: list[str],
    timeout: int = 15,
) -> dict[str, Optional[MatchOU]]:
    """Fetch O/U data for multiple fixtures at once.

    Args:
        fixture_ids: list of 500.com fixture IDs
        timeout: per-request timeout

    Returns:
        {fixture_id: MatchOU or None, ...}
    """
    results = {}
    for fid in fixture_ids:
        try:
            results[fid] = fetch_ou(fid, timeout)
        except Exception as e:
            log.error("Error fetching O/U for %s: %s", fid, e)
            results[fid] = None
    return results


# ---- Convenience: parse O/U from same.php URL params (lightweight) ----
def parse_ou_from_url(fixture_id: str, html: str) -> dict[str, tuple]:
    """Extract O/U data from same.php URL params in the HTML.

    This is a lightweight alternative that only gets opening data.
    Returns {company_name: (line, over_odds, under_odds), ...}
    """
    result = {}
    pattern = re.compile(
        r'daxiao_same\.php\?cid=(\d+)&bigpei=(\d+\.?\d*)&handi=([\d./]+)&smallpei=(\d+\.?\d*)&fixid=' + fixture_id
    )

    for m in pattern.finditer(html):
        cid = m.group(1)
        try:
            over = float(m.group(2))
            line = _parse_line(m.group(3))
            under = float(m.group(4))
        except (ValueError, IndexError):
            continue

        name = CID_NAMES.get(cid, f"cid_{cid}")
        if name not in result:
            result[name] = (line, over, under)

    return result
