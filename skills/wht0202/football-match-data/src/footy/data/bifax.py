"""澳客 必发指数适配器 — 四步验证自动化引擎.

必发(Betfair)交易所数据是赛事分析系统的核心验证维度。
与普通庄家不同，交易所赔率由真实资金博弈形成，不含庄家利润。

四步验证流程:
  Step 1 — 成交量方向验证: 成交占比 vs 隐含概率偏离度
  Step 2 — 交易所vs传统庄家赔率背离: 必发赔率 vs 99家均价
  Step 3 — 庄家盈亏验证: 庄家最怕哪个结果 (负盈亏 = 赔付风险)
  Step 4 — 凯利指数验证: 凯利指数 > 1.0 = 庄家认为该赔率有利可图

Data sources (ranked by reliability):
  1. okooo exchanges page (JS-rendered, requires WebFetch)
  2. nowscore odds page (static HTML, has volume indicators)
  3. Manual input from agent web browsing

Usage:
  from footy.data.bifax import BifaxVerifier

  verifier = BifaxVerifier()
  result = verifier.verify(data_dict)  # data from WebFetch or manual input
  print(result.verdict)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# ---- Data structures ----

@dataclass
class BifaxOutcome:
    """Single outcome (home/draw/away) on the exchange."""

    outcome: str = ""            # "home", "draw", "away"
    label: str = ""              # "主胜", "平局", "客胜"
    exchange_odds: float = 0.0   # 交易所赔率
    volume: float = 0.0          # 成交量
    volume_pct: float = 0.0      # 成交量占比 (%)
    pnl: float = 0.0             # 庄家盈亏 (负 = 庄家怕)
    avg_odds: float = 0.0        # 99家均价
    kelly: float = 0.0           # 凯利指数
    imp_prob: float = 0.0        # 隐含概率 (1/odds, normalized)


@dataclass
class StepResult:
    """Result of a single verification step."""

    step: int = 0
    name: str = ""
    passed: bool = False
    signal: str = ""             # "bullish" / "bearish" / "neutral"
    strength: str = ""           # "strong" / "medium" / "weak"
    detail: str = ""
    score: int = 0               # -2 to +2, aggregated into total


@dataclass
class BifaxVerification:
    """Complete 4-step verification result."""

    match_name: str = ""
    home: BifaxOutcome = field(default_factory=lambda: BifaxOutcome("home", "主胜"))
    draw: BifaxOutcome = field(default_factory=lambda: BifaxOutcome("draw", "平局"))
    away: BifaxOutcome = field(default_factory=lambda: BifaxOutcome("away", "客胜"))
    steps: list[StepResult] = field(default_factory=list)
    total_score: int = 0
    verdict: str = ""            # 综合结论
    recommendation: str = ""

    @property
    def all_passed(self) -> bool:
        return all(s.passed for s in self.steps)

    @property
    def bullish_on(self) -> str:
        """Which outcome does the exchange favor? Returns Chinese label."""
        # Map Chinese labels to outcomes
        label_map = {"主胜": "home", "平局": "draw", "客胜": "away"}
        scores = {"home": 0, "draw": 0, "away": 0}
        for step in self.steps:
            if step.signal == "bullish":
                for label, key in label_map.items():
                    if label in step.detail:
                        scores[key] += 1
        if all(v == 0 for v in scores.values()):
            return "无明显方向"
        best = max(scores, key=scores.get)
        reverse = {"home": "主胜", "draw": "平局", "away": "客胜"}
        return reverse.get(best, "neutral")


class BifaxVerifier:
    """必发四步验证引擎.

    Accepts exchange data and runs 4-step verification.
    Data can come from WebFetch, manual scraping, or API.

    Input format (from WebFetch of okooo exchanges page):
      {
        "home": {"odds": 2.46, "volume": 1407900, "pnl": -648484, "avg": 2.21, "kelly": 0.95},
        "draw": {"odds": 3.25, "volume": 877859, "pnl": -38092, "avg": 2.71, "kelly": 0.88},
        "away": {"odds": 3.50, "volume": 529191, "pnl": 962782, "avg": 3.25, "kelly": 1.05},
      }

    All fields optional — only odds and volume are required for basic analysis.
    """

    # Thresholds
    VOLUME_ANOMALY_THRESHOLD = 40.0    # volume_pct > 40% = anomaly
    PNL_FEAR_THRESHOLD = -50000.0      # pnl < -50k = bookmaker fears
    ODDS_GAP_THRESHOLD = 0.10          # |exchange - avg| > 0.10 = signal
    VOL_PROB_GAP_THRESHOLD = 0.05      # |vol_pct - fair_prob| > 5% = divergence
    KELLY_BULLISH = 1.05               # kelly > 1.05 = bullish
    KELLY_BEARISH = 0.85               # kelly < 0.85 = bearish

    def verify(self, data: dict, match_name: str = "") -> BifaxVerification:
        """Run complete 4-step verification.

        Args:
            data: dict with home/draw/away sub-dicts containing odds, volume, etc.
            match_name: optional match identifier for output

        Returns:
            BifaxVerification with all 4 steps evaluated and total score.
        """
        # Parse outcomes
        home = self._parse_outcome("home", "主胜", data.get("home", {}))
        draw = self._parse_outcome("draw", "平局", data.get("draw", {}))
        away = self._parse_outcome("away", "客胜", data.get("away", {}))

        # Calculate implied probabilities
        self._calc_imp_probs(home, draw, away)

        # Calculate volume percentages if not provided
        total_vol = home.volume + draw.volume + away.volume
        if total_vol > 0:
            for oc in [home, draw, away]:
                if oc.volume_pct == 0:
                    oc.volume_pct = (oc.volume / total_vol) * 100

        result = BifaxVerification(
            match_name=match_name,
            home=home, draw=draw, away=away,
        )

        # ---- Run 4 steps ----
        result.steps = [
            self._step1_volume_direction(home, draw, away),
            self._step2_exchange_vs_traditional(home, draw, away),
            self._step3_bookmaker_pnl(home, draw, away),
            self._step4_kelly_index(home, draw, away),
        ]

        result.total_score = sum(s.score for s in result.steps)

        # Generate verdict
        result.verdict, result.recommendation = self._generate_verdict(result)

        return result

    def _parse_outcome(self, key: str, label: str, d: dict) -> BifaxOutcome:
        """Parse a single outcome from raw data dict."""
        return BifaxOutcome(
            outcome=key,
            label=label,
            exchange_odds=float(d.get("odds", 0) or 0),
            volume=float(d.get("volume", 0) or 0),
            volume_pct=float(d.get("vol_pct", 0) or 0),
            pnl=float(d.get("pnl", 0) or 0),
            avg_odds=float(d.get("avg", 0) or 0),
            kelly=float(d.get("kelly", 0) or 0),
        )

    @staticmethod
    def _calc_imp_probs(home: BifaxOutcome, draw: BifaxOutcome, away: BifaxOutcome):
        """Calculate normalized implied probabilities from exchange odds."""
        total = 0.0
        for oc in [home, draw, away]:
            if oc.exchange_odds > 1:
                oc.imp_prob = 1.0 / oc.exchange_odds
                total += oc.imp_prob

        if total > 0:
            for oc in [home, draw, away]:
                oc.imp_prob = oc.imp_prob / total

    # ---- Step 1: 成交量方向验证 ----
    def _step1_volume_direction(
        self, home: BifaxOutcome, draw: BifaxOutcome, away: BifaxOutcome
    ) -> StepResult:
        """成交量方向验证: 真实资金流向 vs 赔率隐含方向.

        Core logic:
        - If volume is abnormally high on one outcome (>40%) → anomaly
        - If volume_share diverges from fair probability > 5% → money flow signal
        - High volume + low fair prob = smart money going contrarian
        """
        details = []

        # Check volume anomaly
        for oc in [home, draw, away]:
            if oc.volume_pct > self.VOLUME_ANOMALY_THRESHOLD:
                details.append(
                    f"⚠️ {oc.label}成交量占比异常 ({oc.volume_pct:.0f}%)"
                )

        # Check volume vs fair probability divergence
        max_gap = 0.0
        max_gap_outcome = ""
        max_gap_direction = ""

        for oc in [home, draw, away]:
            if oc.volume_pct > 0 and oc.imp_prob > 0:
                gap = (oc.volume_pct / 100) - oc.imp_prob
                if abs(gap) > self.VOL_PROB_GAP_THRESHOLD:
                    direction = "涌入" if gap > 0 else "逃离"
                    details.append(
                        f"📊 {oc.label}资金{direction}: "
                        f"成交{oc.volume_pct:.1f}% vs 公允{oc.imp_prob:.1%} (gap={gap:+.1%})"
                    )
                if abs(gap) > abs(max_gap):
                    max_gap = gap
                    max_gap_outcome = oc.label
                    max_gap_direction = "bullish" if gap > 0 else "bearish"

        if not details:
            return StepResult(
                step=1, name="成交量方向验证",
                passed=True, signal="neutral", strength="weak",
                detail="成交量分布与隐含概率一致，无异常资金流向",
                score=0,
            )

        # Score based on direction
        score = 1 if abs(max_gap) > 0.10 else (0 if abs(max_gap) < 0.08 else 1)
        if max_gap_direction == "bearish":
            score = -score  # money fleeing = bearish

        strength = "strong" if abs(max_gap) > 0.15 else ("medium" if abs(max_gap) > 0.10 else "weak")

        return StepResult(
            step=1, name="成交量方向验证",
            passed=len(details) <= 1,  # fail if too many anomalies
            signal=max_gap_direction,
            strength=strength,
            detail=" | ".join(details),
            score=score,
        )

    # ---- Step 2: 交易所赔率 vs 传统庄家背离 ----
    def _step2_exchange_vs_traditional(
        self, home: BifaxOutcome, draw: BifaxOutcome, away: BifaxOutcome
    ) -> StepResult:
        """交易所vs传统庄家赔率背离验证.

        Key insight: 必发是真实资金博弈, 传统庄家赔率含利润和意图.
        当两者背离时:
        - 交易所赔率 > 99家均价 → 市场真实看好该方向 (传统庄家在压价)
        - 交易所赔率 < 99家均价 → 市场不看好 (传统庄家在抬价吸引资金)
        """
        details = []
        max_gap = 0.0
        max_gap_outcome = ""
        signal = "neutral"

        for oc in [home, draw, away]:
            if oc.exchange_odds > 1 and oc.avg_odds > 1:
                gap = oc.exchange_odds - oc.avg_odds
                if abs(gap) > self.ODDS_GAP_THRESHOLD:
                    direction = "高于" if gap > 0 else "低于"
                    details.append(
                        f"📈 {oc.label}交易所{direction}99家均价 "
                        f"({oc.exchange_odds:.2f} vs {oc.avg_odds:.2f}, gap={gap:+.2f})"
                    )
                if abs(gap) > abs(max_gap):
                    max_gap = gap
                    max_gap_outcome = oc.label

        if not details:
            return StepResult(
                step=2, name="交易所vs传统庄家",
                passed=True, signal="neutral", strength="weak",
                detail="交易所赔率与99家均价一致，无背离信号",
                score=0,
            )

        # Exchange odds HIGHER than traditional = real market likes it MORE
        # Exchange odds LOWER = real market likes it LESS
        signal = "bullish" if max_gap > 0 else "bearish"
        strength = "strong" if abs(max_gap) > 0.20 else ("medium" if abs(max_gap) > 0.15 else "weak")
        score = 2 if abs(max_gap) > 0.20 else (1 if abs(max_gap) > 0.10 else 0)
        if signal == "bearish":
            score = -score

        return StepResult(
            step=2, name="交易所vs传统庄家",
            passed=True,
            signal=signal,
            strength=strength,
            detail=" | ".join(details),
            score=score,
        )

    # ---- Step 3: 庄家盈亏验证 ----
    def _step3_bookmaker_pnl(
        self, home: BifaxOutcome, draw: BifaxOutcome, away: BifaxOutcome
    ) -> StepResult:
        """庄家盈亏验证: 庄家最怕哪个结果.

        Core logic:
        - P&L < 0 (负盈亏): 如果该结果发生，庄家要赔钱 → 庄家害怕
        - P&L > 0 (正盈亏): 庄家希望该结果发生
        - The outcome with most negative P&L = what bookmaker fears most
        """
        details = []
        most_feared = None
        most_feared_pnl = float("inf")

        for oc in [home, draw, away]:
            if oc.pnl != 0:
                if oc.pnl < self.PNL_FEAR_THRESHOLD:
                    details.append(
                        f"💰 庄家最怕{oc.label} (盈亏 {oc.pnl:+,.0f})"
                    )
                if oc.pnl < most_feared_pnl:
                    most_feared_pnl = oc.pnl
                    most_feared = oc

        if not details:
            return StepResult(
                step=3, name="庄家盈亏验证",
                passed=True, signal="neutral", strength="weak",
                detail="庄家盈亏平衡，无明确恐惧方向",
                score=0,
            )

        # The feared outcome = bullish signal (counter-intuitive but true:
        # if bookmakers fear it, it means smart money is betting it)
        signal = "bullish" if most_feared else "neutral"
        strength = "strong" if most_feared_pnl < -200000 else ("medium" if most_feared_pnl < -100000 else "weak")
        score = 2 if most_feared_pnl < -200000 else (1 if most_feared_pnl < -100000 else 0)

        return StepResult(
            step=3, name="庄家盈亏验证",
            passed=True,
            signal=signal,
            strength=strength,
            detail=" | ".join(details) + (
                f" → 庄家最怕{most_feared.label}" if most_feared else ""
            ),
            score=score,
        )

    # ---- Step 4: 凯利指数验证 ----
    def _step4_kelly_index(
        self, home: BifaxOutcome, draw: BifaxOutcome, away: BifaxOutcome
    ) -> StepResult:
        """凯利指数验证: 庄家赔率 vs 市场真实概率.

        Kelly Index = (fair_prob * odds - 1) / (odds - 1) simplified.
        Actually on okooo: 凯利指数 = 庄家赔率 / 市场平均赔率
        > 1.0 = 庄家给的高于市场 → 看好
        < 1.0 = 庄家压价 → 不看好
        """
        details = []
        max_kelly = 0.0
        min_kelly = float("inf")
        best_outcome = ""
        worst_outcome = ""

        for oc in [home, draw, away]:
            if oc.kelly > 0:
                if oc.kelly > self.KELLY_BULLISH:
                    details.append(
                        f"🟢 {oc.label}凯利指数偏高 ({oc.kelly:.2f}) → 庄家看好"
                    )
                elif oc.kelly < self.KELLY_BEARISH:
                    details.append(
                        f"🔴 {oc.label}凯利指数偏低 ({oc.kelly:.2f}) → 庄家不看好"
                    )
                if oc.kelly > max_kelly:
                    max_kelly = oc.kelly
                    best_outcome = oc.label
                if oc.kelly < min_kelly:
                    min_kelly = oc.kelly
                    worst_outcome = oc.label

        if not details:
            # Calculate implied kelly from odds vs avg if raw kelly not provided
            for oc in [home, draw, away]:
                if oc.exchange_odds > 1 and oc.avg_odds > 1:
                    implied_kelly = oc.avg_odds / oc.exchange_odds
                    if implied_kelly > self.KELLY_BULLISH:
                        details.append(
                            f"🟢 {oc.label}隐含凯利偏高 ({implied_kelly:.2f}) → 庄家看好"
                        )
                    elif implied_kelly < self.KELLY_BEARISH:
                        details.append(
                            f"🔴 {oc.label}隐含凯利偏低 ({implied_kelly:.2f}) → 庄家不看好"
                        )

        if not details:
            return StepResult(
                step=4, name="凯利指数验证",
                passed=True, signal="neutral", strength="weak",
                detail="凯利指数正常，无明确偏向",
                score=0,
            )

        # Highest kelly = bullish
        signal = "bullish"
        strength = "strong" if max_kelly > 1.10 else ("medium" if max_kelly > 1.05 else "weak")
        score = 2 if max_kelly > 1.10 else (1 if max_kelly > 1.05 else 0)

        return StepResult(
            step=4, name="凯利指数验证",
            passed=True,
            signal=signal,
            strength=strength,
            detail=" | ".join(details),
            score=score,
        )

    # ---- Verdict generation ----
    def _generate_verdict(self, result: BifaxVerification) -> tuple[str, str]:
        """Generate overall verdict and recommendation from 4-step results."""
        total = result.total_score

        # Count strong signals
        strong_bullish = sum(
            1 for s in result.steps if s.signal == "bullish" and s.strength == "strong"
        )
        strong_bearish = sum(
            1 for s in result.steps if s.signal == "bearish" and s.strength == "strong"
        )

        if total >= 5:
            verdict = "⭐⭐⭐⭐⭐ 必发强烈看好"
            rec = f"交易所真实资金明确支持{result.bullish_on}方向，四步验证全部通过"
        elif total >= 3:
            verdict = "⭐⭐⭐⭐ 必发看好"
            rec = f"交易所资金偏向{result.bullish_on}方向，{strong_bullish}个强烈信号"
        elif total >= 1:
            verdict = "⭐⭐⭐ 必发略看好"
            rec = f"轻微偏向{result.bullish_on}方向，信号强度中等"
        elif total >= -1:
            verdict = "⭐⭐ 必发中性"
            rec = "交易所无明显偏向，四步验证信号混杂"
        elif total >= -3:
            verdict = "⭐ 必发略不看好"
            rec = f"交易所资金轻微撤离，{strong_bearish}个警惕信号"
        elif total >= -5:
            verdict = "⚠️ 必发不看好"
            rec = f"交易所资金撤离明显，{strong_bearish}个强烈警惕信号"
        else:
            verdict = "🚫 必发强烈不看好"
            rec = "交易所真实资金明确反向，强烈建议回避"

        return verdict, rec


# ---- Convenience functions ----

def exchanges_url(match_id: str) -> str:
    """Return the 必发 page URL for a match."""
    return f"https://www.okooo.com/soccer/match/{match_id}/exchanges/"


def fetch_bifax_data(fixture_id: str, match_name: str = "") -> dict | None:
    """Auto-fetch / synthesise Betfair-style exchange data for a match.

    Tries multiple sources in priority order:

    1. **okooo exchanges page** — attempts a direct HTTP GET of the JS-rendered
       exchanges page.  Because the page relies on JavaScript the raw HTML is
       often empty; when it succeeds we parse out odds / volume / P&L / Kelly.

    2. **500.com aggregate** — falls back to computing company-average odds from
       the 29-company European-odds table and treating the *market-implied
       de-vigged* probabilities as a proxy for exchange-implied odds.  Volume
       and P&L are left at 0 so the 4-step engine can still evaluate the
       exchange-vs-traditional gap (Step 2).

    Returns a dict suitable for :func:`BifaxVerifier.verify` or ``None`` when
    no useful data could be assembled.
    """
    import logging
    log = logging.getLogger(__name__)

    # --- Level 1: try okooo exchanges page ---
    try:
        import urllib.request
        url = exchanges_url(fixture_id)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=12) as r:
            html = r.read().decode("utf-8", errors="replace")
        # Quick heuristic: does the page contain actual exchange data?
        if "成交量" in html or "必发指数" in html or "exchange" in html.lower():
            parsed = _parse_okooo_exchanges(html, match_name)
            if parsed:
                log.info("okooo exchanges parsed for fixture %s", fixture_id)
                return parsed
    except Exception as exc:
        log.debug("okooo exchanges fetch failed for %s: %s", fixture_id, exc)

    # --- Level 2: synthesise from 500.com company odds ---
    try:
        from footy.data.wubai import get_odds_full
        full = get_odds_full(fixture_id)
        cur = full.get("current", {})
        opn = full.get("opening", {})
        if len(cur) < 3:
            return None

        # Compute company-average odds for each outcome
        companies = list(cur.keys())
        h_vals = [c[0] for c in cur.values()]
        d_vals = [c[1] for c in cur.values()]
        a_vals = [c[2] for c in cur.values()]
        avg_h = sum(h_vals) / len(h_vals)
        avg_d = sum(d_vals) / len(d_vals)
        avg_a = sum(a_vals) / len(a_vals)

        # De-vig to get "exchange-style" fair odds
        imp_sum = 1/avg_h + 1/avg_d + 1/avg_a
        fair_h = 1 / ((1/avg_h) / imp_sum)
        fair_d = 1 / ((1/avg_d) / imp_sum)
        fair_a = 1 / ((1/avg_a) / imp_sum)

        # Estimate Kelly from the gap between fair and market odds
        kelly_h = (fair_h / avg_h - 1) if avg_h > 0 else 0
        kelly_d = (fair_d / avg_d - 1) if avg_d > 0 else 0
        kelly_a = (fair_a / avg_a - 1) if avg_a > 0 else 0

        data = {
            "home": {
                "odds": round(fair_h, 2),
                "volume": 0,
                "pnl": 0,
                "avg": round(avg_h, 2),
                "kelly": round(kelly_h, 3),
            },
            "draw": {
                "odds": round(fair_d, 2),
                "volume": 0,
                "pnl": 0,
                "avg": round(avg_d, 2),
                "kelly": round(kelly_d, 3),
            },
            "away": {
                "odds": round(fair_a, 2),
                "volume": 0,
                "pnl": 0,
                "avg": round(avg_a, 2),
                "kelly": round(kelly_a, 3),
            },
        }
        log.info(
            "Synthesised bifax data for %s from %d companies (avg odds: %.2f/%.2f/%.2f)",
            fixture_id, len(companies), avg_h, avg_d, avg_a,
        )
        return data
    except Exception as exc:
        log.warning("Failed to synthesise bifax data for %s: %s", fixture_id, exc)

    return None


def _parse_okooo_exchanges(html: str, match_name: str = "") -> dict | None:
    """Try to extract exchange data from an okooo exchanges page HTML.

    Returns a dict in the standard bifax data format, or None on failure.
    """
    import re
    # Look for numeric patterns that look like odds/volume/pnl triplets
    # okooo pages often embed data in JS arrays or table cells
    # This is a best-effort parser — the page is JS-rendered so raw HTML
    # often has empty placeholders.

    # Try to find odds (decimal, e.g. 2.46, 3.25, 3.50)
    odds_pat = re.findall(r'(?:odds|赔率)[^>]*>?\s*(\d+\.\d{2})', html, re.IGNORECASE)
    # Try to find volumes (large integers, e.g. 1407900)
    vol_pat = re.findall(r'(?:volume|成交量|成交)[^>]*>?\s*([\d,]+)', html, re.IGNORECASE)

    if len(odds_pat) >= 3:
        try:
            h_odds = float(odds_pat[0])
            d_odds = float(odds_pat[1])
            a_odds = float(odds_pat[2])
            data = {
                "home": {"odds": h_odds, "volume": 0, "pnl": 0, "avg": h_odds, "kelly": 0},
                "draw": {"odds": d_odds, "volume": 0, "pnl": 0, "avg": d_odds, "kelly": 0},
                "away": {"odds": a_odds, "volume": 0, "pnl": 0, "avg": a_odds, "kelly": 0},
            }
            return data
        except (ValueError, IndexError):
            pass

    return None


def quick_verify(data: dict, match_name: str = "") -> BifaxVerification:
    """Quick 4-step verification with default thresholds."""
    return BifaxVerifier().verify(data, match_name)


def summarize(data: dict) -> str:
    """Generate human-readable 必发 signal summary from structured table data.

    (Legacy function — kept for backward compatibility.)

    data format:
      {"home": {"odds": 2.46, "volume": 1407900, "pnl": -648484, "avg": 2.21},
       "draw": {"odds": 3.25, "volume": 877859, "pnl": -38092, "avg": 2.71},
       "away": {"odds": 3.50, "volume": 529191, "pnl": 962782, "avg": 3.25}}
    """
    result = quick_verify(data)
    lines = [f"必发四步验证: {result.verdict}"]

    for step in result.steps:
        icon = "✅" if step.passed else "❌"
        lines.append(f"  {icon} Step {step.step} [{step.name}]: {step.detail}")

    lines.append(f"\n综合评分: {result.total_score:+d}")
    lines.append(f"建议: {result.recommendation}")

    return "\n".join(lines)
