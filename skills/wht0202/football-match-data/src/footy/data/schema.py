"""Unified match schema.

Every data adapter (football-data.co.uk, The Odds API, user CSV, future Chinese
sources) must normalise into this structure so downstream models and backtesting
stay source-agnostic.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Match:
    """A single completed or scheduled football match."""

    date: str  # ISO YYYY-MM-DD
    league: str  # canonical code, e.g. "E0"
    league_name: str  # human-readable, e.g. "Premier League"
    home: str
    away: str
    home_goals: Optional[int] = None
    away_goals: Optional[int] = None

    # Closing 1X2 odds — C-suffix columns: B365CH/CD/CA, PSCH/PSCD/PSCA, ...
    # Tuple order is (home, draw, away).
    odds_1x2: dict[str, tuple[float, float, float]] = field(default_factory=dict)

    # Opening 1X2 odds — non-C columns: B365H/D/A, PSH/D/A, ...
    odds_open_1x2: dict[str, tuple[float, float, float]] = field(default_factory=dict)

    # Over/Under 2.5 closing odds: {book: (over_odds, under_odds)}.
    odds_ou25: dict[str, tuple[float, float]] = field(default_factory=dict)

    # Asian handicap closing: {book: (line, home_water, away_water)}.
    asian_handicap: dict[str, tuple[float, float, float]] = field(
        default_factory=dict
    )

    @property
    def is_finished(self) -> bool:
        return self.home_goals is not None and self.away_goals is not None

    @property
    def result(self) -> Optional[str]:
        """Full-time result from the home perspective: 'H', 'D', or 'A'."""
        if not self.is_finished:
            return None
        if self.home_goals > self.away_goals:
            return "H"
        if self.home_goals < self.away_goals:
            return "A"
        return "D"

    def best_odds(self, outcome: str) -> Optional[float]:
        """Highest available closing odds for an outcome ('H'/'D'/'A')."""
        idx = {"H": 0, "D": 1, "A": 2}[outcome]
        vals = [o[idx] for o in self.odds_1x2.values() if o[idx] and o[idx] > 0]
        return max(vals) if vals else None

    def line_movement(self, book: str) -> dict | None:
        """Open-to-close odds movement for a single bookmaker.

        Returns direction: 'home' | 'draw' | 'away' | 'stable'.
        A negative move = odds dropping = steam toward that side.
        """
        if book not in self.odds_open_1x2 or book not in self.odds_1x2:
            return None
        op = self.odds_open_1x2[book]
        cl = self.odds_1x2[book]
        dt = [cl[i] - op[i] for i in range(3)]
        max_drop = min(dt)  # biggest drop = steam
        direction = "stable"
        if max_drop < -0.03:
            idx = dt.index(max_drop)
            direction = ["home", "draw", "away"][idx]
        return {
            "book": book,
            "open": op,
            "close": cl,
            "move_h": round(float(cl[0] - op[0]), 4),
            "move_d": round(float(cl[1] - op[1]), 4),
            "move_a": round(float(cl[2] - op[2]), 4),
            "direction": direction,
            "coverage": "steam" if max_drop < -0.05 else "slight" if max_drop < -0.03 else "stable",
        }
