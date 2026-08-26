"""捷报网 伤停/阵容 适配器 — NLP-based extraction from Infocat page.

Infocat pages have free-text intelligence, not structured tables.
We extract: player absences (name + reason), formation, lineup hints.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from typing import Optional

import requests

log = logging.getLogger(__name__)

BASE = "https://live.nowscore.com"
INFO_URL = f"{BASE}/Infocat/{{match_id}}.htm"


@dataclass
class PlayerAbsence:
    name: str = ""
    team: str = ""  # "home" or "away"
    reason: str = ""
    detail: str = ""
    impact: str = "medium"


@dataclass
class MatchIntel:
    match_id: str = ""
    home: str = ""
    away: str = ""

    home_formation: str = ""
    away_formation: str = ""

    home_absences: list[PlayerAbsence] = field(default_factory=list)
    away_absences: list[PlayerAbsence] = field(default_factory=list)

    home_lineup_hints: list[str] = field(default_factory=list)
    away_lineup_hints: list[str] = field(default_factory=list)

    home_impact_score: float = 0.0
    away_impact_score: float = 0.0
    summary: str = ""


def fetch_intel(match_id: str, timeout: int = 15) -> Optional[MatchIntel]:
    url = INFO_URL.format(match_id=match_id)
    try:
        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
            timeout=timeout,
        )
        r.encoding = "utf-8"
    except requests.RequestException as e:
        log.warning("Infocat: %s", e)
        return None

    if r.status_code != 200 or len(r.text) < 500:
        return None

    html = r.text
    # Strip HTML tags for NLP
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)

    intel = MatchIntel(match_id=match_id)

    # ---- Team names from title ----
    tm = re.search(r"<title>([^<]+)", html)
    if tm:
        title = re.sub(r"<[^>]+>", "", tm.group(1))
        parts = re.split(r"\s*(?:VS|vs|足球情报|分析预测)\s*", title)
        for p in parts:
            p = p.strip()
            if p and len(p) >= 2 and not intel.home:
                intel.home = p
            elif p and len(p) >= 2 and intel.home and not intel.away:
                intel.away = p

    # ---- Split text into home/away sections ----
    # The page has two main blocks of text, one per team
    home_text, away_text = _split_teams(text)

    # ---- Formations ----
    for txt, is_home in [(home_text, True), (away_text, False)]:
        fm = re.search(r"(\d+-\d+-\d+|\d+-\d+)\s*阵型", txt)
        if fm:
            if is_home:
                intel.home_formation = fm.group(1)
            else:
                intel.away_formation = fm.group(1)

    # ---- Absences from natural language ----
    intel.home_absences = _nl_extract_absences(home_text, "home")
    intel.away_absences = _nl_extract_absences(away_text, "away")

    # ---- Lineup hints ----
    intel.home_lineup_hints = _nl_extract_lineup_hints(home_text)
    intel.away_lineup_hints = _nl_extract_lineup_hints(away_text)

    # ---- Impact ----
    intel.home_impact_score = -len(intel.home_absences) * 0.5
    intel.away_impact_score = -len(intel.away_absences) * 0.5
    for a in intel.home_absences:
        if "主力" in a.detail or "核心" in a.detail:
            intel.home_impact_score -= 0.5
    for a in intel.away_absences:
        if "主力" in a.detail or "核心" in a.detail:
            intel.away_impact_score -= 0.5

    # ---- Summary ----
    parts = []
    if intel.home_formation:
        parts.append(f"{intel.home} {intel.home_formation}")
    if intel.away_formation:
        parts.append(f"{intel.away} {intel.away_formation}")
    if intel.home_absences:
        names = [a.name for a in intel.home_absences]
        parts.append(f"主队缺阵: {', '.join(names)}")
    if intel.away_absences:
        names = [a.name for a in intel.away_absences]
        parts.append(f"客队缺阵: {', '.join(names)}")
    intel.summary = " | ".join(parts) if parts else "暂无阵容情报"

    log.info("Infocat %s: %d home absences, %d away absences",
             match_id, len(intel.home_absences), len(intel.away_absences))
    return intel


def _split_teams(text: str) -> tuple[str, str]:
    """Split text into home and away team sections."""
    # Find a midpoint separator (often "卡塔尔" or second team mention)
    # Simple: find the second occurrence of "阵型" or midpoint of text
    formations = list(re.finditer(r"(\d+-\d+-\d+|\d+-\d+)\s*阵型", text))
    if len(formations) >= 2:
        mid = (formations[0].end() + formations[1].start()) // 2
        return text[:mid], text[mid:]
    # Fallback: split at 50%
    mid = len(text) // 2
    return text[:mid], text[mid:]


def _nl_extract_absences(text: str, team: str) -> list[PlayerAbsence]:
    """Extract player absences from natural language text."""
    absences = []
    # Find sentences with absence keywords
    sentences = re.split(r"[。！；\n]", text)
    for sent in sentences:
        if not any(kw in sent for kw in ["红牌", "停赛", "缺席", "缺阵", "伤病", "受伤", "禁赛"]):
            continue

        # Extract player name: look for Chinese name patterns near the keyword
        # Format: "后卫XXX" or "中场XXX" or "核心XXX"
        name_patterns = [
            r"(?:后卫|中场|前锋|门将|核心|队长|主力)?([\u4e00-\u9fff·]{2,4})(?:因|在|于|上轮|本场|将|吃到|领到|遭到)",
            r"([\u4e00-\u9fff·]{2,4})(?:因|吃到|领到|遭到|红牌|停赛|缺席)",
        ]
        name = ""
        for pat in name_patterns:
            nm = re.search(pat, sent)
            if nm:
                candidate = nm.group(1)
                # Filter false positives
                if candidate not in ["因为", "上轮", "本场", "后续", "比赛", "球队", "小组赛", "世界盃"]:
                    name = candidate
                    break

        if not name:
            # Try: "穆哈雷莫维奇" style foreign names
            fm = re.search(r"([\u4e00-\u9fff·]{3,8})(?:因|在|于|上轮|本场|将|吃到|领到)", sent)
            if fm:
                name = fm.group(1)

        if not name:
            continue

        reason = "红牌停赛" if "红牌" in sent else "伤病" if "伤" in sent else "停赛"
        impact = "high" if ("主力" in sent or "核心" in sent or "队长" in sent) else "medium"
        detail = sent.strip()[:150]

        absences.append(PlayerAbsence(name=name, team=team, reason=reason, detail=detail, impact=impact))
    return absences


def _nl_extract_lineup_hints(text: str) -> list[str]:
    """Extract lineup hints from text."""
    hints = []
    # Find sentences mentioning lineup
    for sent in re.split(r"[。！\n]", text):
        if any(kw in sent for kw in ["首发", "阵型", "顶替", "搭档", "坐镇", "把守", "防线"]):
            hints.append(sent.strip()[:200])
    return hints[:5]
