"""Playwright + Edge — 拉取 titan007 JS渲染页面 (亚盘终盘+基本面).

绕过 WebFetch 域名封锁。使用系统自带 Edge 浏览器内核(无需下载Chromium)。
"""
from __future__ import annotations
import json, re, logging
from pathlib import Path
from typing import Optional

log = logging.getLogger(__name__)
_browser = None

def _get_browser():
    global _browser
    if _browser is None:
        from playwright.sync_api import sync_playwright
        import os
        _playwright = sync_playwright().start()
        # Try explicit Edge path first, fallback to channel
        edge_paths = [
            "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
            "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
        ]
        edge_exe = None
        for p in edge_paths:
            if os.path.exists(p):
                edge_exe = p
                break
        if edge_exe:
            _browser = _playwright.chromium.launch(executable_path=edge_exe, headless=True)
        else:
            _browser = _playwright.chromium.launch(channel='msedge', headless=True)
    return _browser

def fetch_ah(match_id: str) -> Optional[dict]:
    """拉取 titan007 亚盘初/终盘数据."""
    url = f"https://vip.titan007.com/AsianOdds_n.aspx?id={match_id}"
    try:
        browser = _get_browser()
        page = browser.new_page()
        page.goto(url, timeout=15000)
        page.wait_for_timeout(2000)
        text = page.inner_text('body')
        html = page.content()
        page.close()
    except Exception as e:
        log.warning("titan007 AH fetch failed: %s", e)
        return None

    result = {"companies": [], "league": "", "home": "", "away": ""}
    lines = text.split('\n')
    
    # 联赛 + 队名
    for i, line in enumerate(lines):
        if '(主)' in line and i > 0:
            result["home"] = line.replace('(主)','').strip()
        if line.strip() == 'VS' and i > 0 and i+1 < len(lines):
            # Away team is the line before VS if it's not the league line, or after
            if result["home"] and not result["away"]:
                result["away"] = lines[i+1].strip()
                if len(result["away"]) > 10:  # Too long, not a team name
                    result["away"] = lines[i-1].strip() if i > 0 else ''
        if re.search(r'(?:冰岛超|爱超|澳达超|芬超|瑞典甲|巴西乙|智利杯|冰岛杯|法罗甲|爱甲|拉脱超|伊朗超|立陶甲|莫桑冠|苏足总杯|爱沙杯)', line):
            m = re.search(r'(?:冰岛超|爱超|澳达超|芬超|瑞典甲|巴西乙|智利杯|冰岛杯|法罗甲|爱甲|拉脱超|伊朗超|立陶甲|莫桑冠|苏足总杯|爱沙杯)', line)
            if not result["league"]:
                result["league"] = m.group(0)
    
    # 解析初/终盘表格 (格式: 公司名行 + 数据行交替)
    # 数据行: 初主水 初盘 初客水 即主水 即盘 即客水
    company_name = None
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Check if this is a company name row (澳*, Crow*, 36*, etc.)
        name_match = re.match(r'^(澳\*|Crow\*|36\*|易胜?\*|伟\*|明\*|10\*|12\*|利\*|盈\*|18\*|平\*|1x\*|威\*|Interwet\*|香港马\*|BWi\*)', line)
        if name_match:
            company_name = name_match.group(1)
            # Check if the data is on the same line (some companies like 易*, 威*)
            nums = re.findall(r'(\d+\.\d{2})', line)
            terms = re.findall(r'([\u4e00-\u9fff/]+(?:球|手)[\u4e00-\u9fff/]*)', line)
            if len(nums) >= 4 and len(terms) >= 2:
                _add_company(result, company_name, nums, terms)
                company_name = None
            continue
        
        # Data line (no company name) — pairs with previous company_name
        if company_name:
            nums = re.findall(r'(\d+\.\d{2})', line)
            terms = re.findall(r'([\u4e00-\u9fff/]+(?:球|手)[\u4e00-\u9fff/]*)', line)
            if len(nums) >= 4 and len(terms) >= 2:
                _add_company(result, company_name, nums, terms)
            company_name = None
    
    return result if result["companies"] else None


def _add_company(result, name, nums, terms):
    """解析一行赔率数据并添加到结果."""
    try:
        result["companies"].append({
            "name": name.rstrip("*"),
            "open": (float(nums[0]), _ah(terms[0]), float(nums[1])),
            "close": (float(nums[2]), _ah(terms[1]), float(nums[3])),
        })
    except (ValueError, IndexError):
        pass


def fetch_analysis(match_id: str, use_browser: bool = True) -> Optional[str]:
    """拉取 titan007 析页面(基本面原始文本).

    默认使用 Playwright (处理JS渲染). use_browser=False 时走 urllib.
    """
    url = f"https://zq.titan007.com/analysis/{match_id}sb.htm"
    # ── HTTP path (fast, no browser) ──
    try:
        from urllib.request import Request, urlopen
        req = Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml",
        })
        with urlopen(req, timeout=12) as resp:
            raw = resp.read()
            # Try gb2312 first, fallback to utf-8
            try:
                text = raw.decode("gb2312")
            except Exception:
                text = raw.decode("utf-8", errors="replace")
            if len(text) > 2000:
                return text
    except Exception as e:
        log.debug("titan007 HTTP fetch failed: %s", e)

    # ── Playwright fallback ──
    if use_browser:
        try:
            browser = _get_browser()
            page = browser.new_page()
            page.goto(url, timeout=15000)
            page.wait_for_timeout(2000)
            text = page.inner_text('body')
            page.close()
            return text
        except Exception as e:
            log.warning("titan007 browser fetch failed: %s", e)
    return None


def search_titan_id(home: str, away: str, max_probes: int = 60) -> Optional[str]:
    """Auto-search titan007 match ID — universal league support.

    Primary: scrape live index page (oldIndexall.aspx) for schedule ID.
    Fallback: probe known ID clusters (World Cup, etc).

    Returns titan007 ID string or None.
    """
    home_clean = home.strip()
    away_clean = away.strip()

    # ── Cache check ──
    cache_dir = Path(__file__).resolve().parent.parent.parent.parent / "data"
    cache_file = cache_dir / "titan_map.json"
    cache = {}
    if cache_file.exists():
        try:
            cache = json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception:
            pass

    cache_key = f"{home_clean}|{away_clean}"
    if cache_key in cache:
        log.info("titan007 cache hit: %s -> %s", cache_key, cache[cache_key])
        return cache[cache_key]

    def _save_cache(mid: str) -> str:
        cache[cache_key] = mid
        cache_dir.mkdir(parents=True, exist_ok=True)
        try:
            cache_file.write_text(
                json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass
        log.info("titan007 found: %s+%s -> %s", home_clean, away_clean, mid)
        return mid

    # ═══════════════════════════════════════════
    # Primary: live index page (all leagues)
    # ═══════════════════════════════════════════
    try:
        browser = _get_browser()
        page = browser.new_page()
        page.goto("https://live.titan007.com/oldIndexall.aspx", timeout=20000)
        page.wait_for_timeout(4000)
        html = page.content()
        page.close()

        # Find team names in HTML, extract schedule ID from chk_XXXXXXX
        idx = html.find(home_clean)
        if idx >= 0:
            chunk = html[max(0, idx - 600):idx + 600]
            # Also verify away team is in same match row
            if away_clean in chunk:
                m = re.search(r"chk[_\s]*(\d{6,8})", chunk)
                if m:
                    return _save_cache(m.group(1))
    except Exception as e:
        log.debug("titan007 index page search failed: %s", e)

    # ═══════════════════════════════════════════
    # Fallback: probe known ID clusters
    # ═══════════════════════════════════════════
    base_ids = [
        2907380, 2907400, 2907350, 2907450, 2907300, 2907500,  # World Cup
        1800000, 1900000, 2000000, 2100000, 2200000,            # other leagues
    ]

    try:
        browser = _get_browser()
        for base in base_ids:
            for offset in range(-max_probes // 2, max_probes // 2):
                mid = str(base + offset)
                try:
                    page = browser.new_page()
                    page.goto(f"https://zq.titan007.com/analysis/{mid}sb.htm", timeout=4000)
                    page.wait_for_timeout(400)
                    title = page.title()
                    page.close()
                    if home_clean in title and away_clean in title:
                        return _save_cache(mid)
                except Exception:
                    pass
    except Exception as e:
        log.debug("titan007 browser search failed: %s", e)

    # ── urllib last-resort ──
    from urllib.request import Request, urlopen
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    for base in base_ids:
        for offset in range(-max_probes // 2, max_probes // 2):
            mid = str(base + offset)
            try:
                req = Request(f"https://zq.titan007.com/analysis/{mid}sb.htm", headers=headers)
                with urlopen(req, timeout=4) as resp:
                    raw = resp.read(4096)
                    try:
                        chunk = raw.decode("gb2312", errors="replace")
                    except Exception:
                        chunk = raw.decode("utf-8", errors="replace")
                t = re.search(r"<title>(.*?)</title>", chunk)
                if t and home_clean in t.group(1) and away_clean in t.group(1):
                    return _save_cache(mid)
            except Exception:
                continue
    return None


def fetch_euro_odds(match_id: str) -> Optional[dict]:
    """拉取 titan007 百家欧赔数据 (初盘+即时).

    从分析页 (analysis/{id}sb.htm) 的嵌入表格解析。
    返回: {companies: [{name, open:(h,d,a), current:(h,d,a)}], ...}
    """
    url = f"https://zq.titan007.com/analysis/{match_id}sb.htm"
    try:
        browser = _get_browser()
        page = browser.new_page()
        page.goto(url, timeout=15000)
        page.wait_for_timeout(2000)
        html = page.content()
        page.close()
    except Exception as e:
        log.warning("titan007 euro odds fetch failed: %s", e)
        return None

    # Parse the odds table embedded in the analysis page
    # Structure: alternating rows of (company_name, 初 odds, 即 odds)
    idx = html.find("主胜")
    if idx < 0:
        return None

    chunk = html[idx:idx + 20000]
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", chunk, re.DOTALL)

    result = {"companies": [], "match_id": match_id}
    current_company = None
    pending_open = None  # (h,d,a) waiting for its 即时 pair

    for row in rows:
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.DOTALL)
        clean = [re.sub(r"<[^>]+>", "", c).strip() for c in cells]

        # Skip empty rows
        if not clean or all(c == "" for c in clean):
            continue

        # "即时" or "终" row — carries the current/close odds for the previous company
        if clean[0] in ("即时", "终") and current_company and len(clean) >= 4:
            try:
                ch, cd, ca = float(clean[1]), float(clean[2]), float(clean[3])
                result["companies"].append({
                    "name": current_company.rstrip("*"),
                    "open": pending_open or (ch, cd, ca),
                    "current": (ch, cd, ca),
                })
                current_company = None
                pending_open = None
            except ValueError:
                pass
            continue

        # Company name row: first cell contains company identifier
        if clean and len(clean[0]) >= 2 and any(c in clean[0] for c in "*澳Crow36易伟明利盈181平威1xBetfair"):
            current_company = clean[0]
            # Check if opening odds are on same row
            # Pattern: company | 初 | h | d | a | ...
            if len(clean) >= 5:
                try:
                    oh, od, oa = float(clean[2]), float(clean[3]), float(clean[4])
                    pending_open = (oh, od, oa)
                except ValueError:
                    pending_open = None
            continue

    return result if result["companies"] else None


def fetch_ou(match_id: str) -> Optional[dict]:
    """拉取 titan007 大小球数据 (初盘+即时).

    从分析页进球数Tab解析。
    返回: {companies: [{name, open_line, open_over, open_under, current_line, current_over, current_under}]}
    """
    url = f"https://zq.titan007.com/analysis/{match_id}sb.htm"
    try:
        browser = _get_browser()
        page = browser.new_page()
        page.goto(url, timeout=15000)
        page.wait_for_timeout(2000)
        # Click 进球数 tab
        try:
            page.click("text=进球数", timeout=5000)
            page.wait_for_timeout(2000)
        except Exception:
            pass
        html = page.content()
        page.close()
    except Exception as e:
        log.warning("titan007 OU fetch failed: %s", e)
        return None

    # Find the 进球数 table
    idx = html.find("大球")
    if idx < 0:
        return None

    chunk = html[idx:idx + 15000]
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", chunk, re.DOTALL)
    result = {"companies": [], "match_id": match_id}

    for row in rows:
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.DOTALL)
        clean = [re.sub(r"<[^>]+>", "", c).strip() for c in cells]

        if not clean or len(clean) < 3:
            continue

        # Company row: second cell has company name
        if len(clean) >= 9 and clean[1] and len(clean[1]) >= 2 and any(
            c in clean[1] for c in "*澳Crow36易伟明利盈181平威1xBetfairInterwet"
        ):
            try:
                result["companies"].append({
                    "name": clean[1].rstrip("*"),
                    "open_over": float(clean[3]),
                    "open_line": _ou_line(clean[4]),
                    "open_under": float(clean[5]),
                    "current_over": float(clean[6]),
                    "current_line": _ou_line(clean[7]),
                    "current_under": float(clean[8]),
                })
            except (ValueError, IndexError):
                # Also try cols 10-12 if first set fails (history columns)
                try:
                    result["companies"].append({
                        "name": clean[1].rstrip("*"),
                        "open_over": float(clean[3]),
                        "open_line": _ou_line(clean[4]),
                        "open_under": float(clean[5]),
                        "current_over": float(clean[9]),
                        "current_line": _ou_line(clean[10]),
                        "current_under": float(clean[11]),
                    })
                except (ValueError, IndexError):
                    pass

    return result if result["companies"] else None


def _ah(s: str) -> float:
    mapping = {
        "平手":0,"平/半":0.25,"半球":0.5,"半/一":0.75,"一球":1,"一/球半":1.25,
        "球半":1.5,"球半/两":1.75,"两球":2,"两/两半":2.25,"两半":2.5,"两半/三":2.75,"三球":3,
        "受平/半":-0.25,"受半球":-0.5,"受半/一":-0.75,"受一球":-1,"受一/球半":-1.25,
        "受球半":-1.5,"受球半/两":-1.75,"受两球":-2,
    }
    for k,v in sorted(mapping.items(), key=lambda x:-len(x[0])):
        if k in s: return v
    try: return float(s)
    except: return 0


def _ou_line(s: str) -> float:
    """Parse O/U line: '2.5' → 2.5, '2.5/3' → 2.75"""
    if '/' in s:
        parts = s.split('/')
        try: return (float(parts[0]) + float(parts[1])) / 2
        except: pass
    try: return float(s)
    except: return 0
