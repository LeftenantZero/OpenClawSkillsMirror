"""Parse nowscore copy-paste data into structured match analysis.

Handles the messy tab-separated format from nowscore's odds comparison page.
Columns: company, AH_open(home/line/away), AH_current(home/line/away),
         EU_open(h/d/a), EU_current(h/d/a), OU_open(over/line/under), OU_current.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class NowscoreMatch:
    home: str = ""
    away: str = ""
    companies: list = field(default_factory=list)


def parse_paste(raw: str, home: str = "", away: str = "") -> dict:
    """Parse a nowscore paste dump into structured data.

    Returns dict with keys: home, away, companies(list of dicts),
    ah_summary, eu_summary, ou_summary.
    """
    lines = [l.strip() for l in raw.split("\n") if l.strip() and "\t" in l]
    if not lines:
        return {"error": "No tab-separated data found", "raw_len": len(raw)}

    companies = []
    ah_data = []
    eu_data = []
    ou_data = []

    for line in lines:
        cols = line.split("\t")
        # Skip header rows
        if len(cols) < 5 or "让球初指" in line or "公司" in line:
            continue

        name = cols[0].strip().rstrip("*")

        # Parse Asian Handicap: cols 1-3 = open, 4-6 = current
        ah_open = None
        ah_current = None
        if len(cols) >= 6:
            try:
                home_water = _parse_water(cols[1])
                line_str = cols[2].strip() if len(cols) > 2 else ""
                away_water = _parse_water(cols[3]) if len(cols) > 3 else 0
                ah_line = _parse_ah_line(line_str)
                if ah_line is not None:
                    ah_open = {"home_water": home_water, "line": ah_line, "away_water": away_water}
            except (ValueError, IndexError):
                pass

        if len(cols) >= 9:
            try:
                home_water2 = _parse_water(cols[4])
                line_str2 = cols[5].strip() if len(cols) > 5 else ""
                away_water2 = _parse_water(cols[6]) if len(cols) > 6 else 0
                ah_line2 = _parse_ah_line(line_str2)
                if ah_line2 is not None:
                    ah_current = {"home_water": home_water2, "line": ah_line2, "away_water": away_water2}
            except (ValueError, IndexError):
                pass

        # Parse European odds: cols 7-9 = open, 10-12 = current
        eu_open = None
        eu_current = None
        if len(cols) >= 12:
            try:
                h_o = float(cols[7]) if cols[7].strip() else 0
                d_o = float(cols[8]) if cols[8].strip() else 0
                a_o = float(cols[9]) if cols[9].strip() else 0
                if h_o > 1:
                    eu_open = (h_o, d_o, a_o)
            except ValueError:
                pass
            try:
                h_c = float(cols[10]) if cols[10].strip() else 0
                d_c = float(cols[11]) if cols[11].strip() else 0
                a_c = float(cols[12]) if cols[12].strip() else 0
                if h_c > 1:
                    eu_current = (h_c, d_c, a_c)
            except ValueError:
                pass

        # Parse O/U: cols 13-15 = open, 16-18 = current
        ou_open = None
        ou_current = None
        if len(cols) >= 18:
            try:
                over_o = _parse_water(cols[13])
                line_o = _parse_ou_line(cols[14].strip()) if cols[14].strip() else 0
                under_o = _parse_water(cols[15]) if len(cols) > 15 else 0
                if line_o:
                    ou_open = {"over": over_o, "line": line_o, "under": under_o}
            except (ValueError, IndexError):
                pass
            try:
                over_c = _parse_water(cols[16])
                line_c = _parse_ou_line(cols[17].strip()) if cols[17].strip() else 0
                under_c = _parse_water(cols[18]) if len(cols) > 18 else 0
                if line_c:
                    ou_current = {"over": over_c, "line": line_c, "under": under_c}
            except (ValueError, IndexError):
                pass

        if eu_current or ah_current:
            companies.append({
                "name": name,
                "ah_open": ah_open,
                "ah_current": ah_current,
                "eu_open": eu_open,
                "eu_current": eu_current,
                "ou_open": ou_open,
                "ou_current": ou_current,
            })
            if ah_open:
                ah_data.append(ah_open)
            if ah_current:
                ah_data.append(ah_current)
            if eu_current:
                eu_data.append(eu_current)
            if ou_current:
                ou_data.append(ou_current)

    return {
        "home": home,
        "away": away,
        "companies": companies,
        "company_count": len(companies),
        "_ah": ah_data,
        "_eu": eu_data,
        "_ou": ou_data,
    }


def _parse_water(val: str) -> float:
    """Parse water/odds like '0.95' or '1.01'."""
    v = val.strip()
    if not v:
        return 0.0
    return float(v)


def _parse_ah_line(val: str) -> float | None:
    """Parse AH line like '一/球半', '球半', '平手', '一球'."""
    v = val.strip()
    if not v:
        return None
    mapping = {
        "平手": 0.0,
        "平/半": 0.25,
        "半球": 0.50,
        "半/一": 0.75,
        "一球": 1.00,
        "一/球半": 1.25,
        "球半": 1.50,
        "球半/两": 1.75,
        "两球": 2.00,
        "两/两半": 2.25,
        "两半": 2.50,
        "两半/三": 2.75,
        "三球": 3.00,
        "受平/半": -0.25,
        "受半球": -0.50,
        "受半/一": -0.75,
        "受一球": -1.00,
        "受一/球半": -1.25,
        "受球半": -1.50,
    }
    if v in mapping:
        return mapping[v]
    # Try numeric
    try:
        return float(v)
    except ValueError:
        return None


def _parse_ou_line(val: str) -> float | None:
    """Parse O/U line like '2.5/3', '2.5'."""
    v = val.strip()
    if not v:
        return None
    if "/" in v:
        parts = v.split("/")
        return (float(parts[0]) + float(parts[1])) / 2
    try:
        return float(v)
    except ValueError:
        return None


def print_analysis(data: dict) -> None:
    """Print a clean formatted analysis from parsed nowscore data."""
    if "error" in data:
        print(f"Parse error: {data['error']}")
        return

    cos = data["companies"]
    if not cos:
        print("No company data parsed")
        return

    print(f"\n{'='*65}")
    print(f"  {data.get('home','?')} vs {data.get('away','?')} — 赛事数据分析 (nowscore数据)")
    print(f"{'='*65}")
    print(f"  公司数: {len(cos)}")

    # EU summary
    eu_cos = [c for c in cos if c["eu_current"]]
    if eu_cos:
        avg_h = sum(c["eu_current"][0] for c in eu_cos) / len(eu_cos)
        avg_d = sum(c["eu_current"][1] for c in eu_cos) / len(eu_cos)
        avg_a = sum(c["eu_current"][2] for c in eu_cos) / len(eu_cos)
        imp = 1/avg_h + 1/avg_d + 1/avg_a
        payout = 1/imp
        ph, pd, pa = (1/avg_h)/imp, (1/avg_d)/imp, (1/avg_a)/imp
        print(f"\n📊 欧赔均值: {avg_h:.2f} / {avg_d:.2f} / {avg_a:.2f}")
        print(f"   公平概率: H{ph:.1%} D{pd:.1%} A{pa:.1%} | 返还率: {payout:.1%}")

    # Show individual company data
    print(f"\n{'公司':<12} {'欧赔即时':>18} {'亚盘即时':>18} {'大小球即时':>18}")
    print(f"{'─'*12} {'─'*18} {'─'*18} {'─'*18}")
    for c in cos:
        eu = c["eu_current"]
        eu_str = f"{eu[0]:.2f}/{eu[1]:.2f}/{eu[2]:.2f}" if eu else "-"
        ah = c["ah_current"]
        ah_str = f"{ah['home_water']:.2f}/{ah['line']:.2f}/{ah['away_water']:.2f}" if ah else "-"
        ou = c["ou_current"]
        ou_str = f"O{ou['over']:.2f}/{ou['line']}/{ou['under']:.2f}" if ou else "-"
        print(f"{c['name']:<12} {eu_str:>18} {ah_str:>18} {ou_str:>18}")

    # AH summary
    ah_cos = [c for c in cos if c["ah_open"] and c["ah_current"]]
    if ah_cos:
        avg_open = sum(c["ah_open"]["line"] for c in ah_cos) / len(ah_cos)
        avg_close = sum(c["ah_current"]["line"] for c in ah_cos) / len(ah_cos)
        up = sum(1 for c in ah_cos if c["ah_current"]["line"] > c["ah_open"]["line"] + 0.02)
        down = sum(1 for c in ah_cos if c["ah_current"]["line"] < c["ah_open"]["line"] - 0.02)
        print(f"\n📐 亚盘: 初{avg_open:.2f}→即{avg_close:.2f} | 升{up}降{down}/{len(ah_cos)}")

    # O/U summary
    ou_cos = [c for c in cos if c["ou_open"] and c["ou_current"]]
    if ou_cos:
        avg_open = sum(c["ou_open"]["line"] for c in ou_cos) / len(ou_cos)
        avg_close = sum(c["ou_current"]["line"] for c in ou_cos) / len(ou_cos)
        over_drops = sum(1 for c in ou_cos if c["ou_current"]["over"] < c["ou_open"]["over"] - 0.03)
        under_rises = sum(1 for c in ou_cos if c["ou_current"]["under"] > c["ou_open"]["under"] + 0.03)
        print(f"\n⚽ 大小球: 初{avg_open:.2f}→即{avg_close:.2f} | 大球↓{over_drops} 小球↑{under_rises}")
