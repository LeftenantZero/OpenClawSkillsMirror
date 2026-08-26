"""SQLite storage for matches and persistence across runs."""
from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from typing import Iterator, Optional

from ..config import DB_PATH, ensure_dirs
from .schema import Match


def _connect() -> sqlite3.Connection:
    ensure_dirs()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


SCHEMA = """
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    league TEXT NOT NULL,
    league_name TEXT,
    home TEXT NOT NULL,
    away TEXT NOT NULL,
    home_goals INTEGER,
    away_goals INTEGER,
    odds_json TEXT,
    odds_open_json TEXT,
    odds_ou25_json TEXT,
    asian_handicap_json TEXT,
    UNIQUE(date, league, home, away)
);
"""


def init_db() -> None:
    with _connect() as conn:
        conn.executescript(SCHEMA)
    # Migrate old DBs that may not have the new columns.
    _add_column_if_missing("odds_open_json")
    _add_column_if_missing("odds_ou25_json")
    _add_column_if_missing("asian_handicap_json")


def _add_column_if_missing(col: str) -> None:
    try:
        with _connect() as conn:
            conn.execute(f"ALTER TABLE matches ADD COLUMN {col} TEXT")
    except sqlite3.OperationalError:
        pass  # column already exists


@contextmanager
def get_conn() -> Iterator[sqlite3.Connection]:
    conn = _connect()
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def upsert_matches(matches: list[Match]) -> int:
    """Insert/update matches. Returns the number of newly inserted rows."""
    init_db()
    inserted = 0
    with get_conn() as conn:
        for m in matches:
            cur = conn.execute(
                """
                INSERT INTO matches
                    (date, league, league_name, home, away,
                     home_goals, away_goals,
                     odds_json, odds_open_json, odds_ou25_json,
                     asian_handicap_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(date, league, home, away) DO UPDATE SET
                    league_name=excluded.league_name,
                    home_goals=excluded.home_goals,
                    away_goals=excluded.away_goals,
                    odds_json=excluded.odds_json,
                    odds_open_json=excluded.odds_open_json,
                    odds_ou25_json=excluded.odds_ou25_json,
                    asian_handicap_json=excluded.asian_handicap_json
                """,
                (
                    m.date, m.league, m.league_name, m.home, m.away,
                    m.home_goals, m.away_goals,
                    _dumps(m.odds_1x2), _dumps(m.odds_open_1x2),
                    _dumps(m.odds_ou25), _dumps(m.asian_handicap),
                ),
            )
            inserted += cur.rowcount if cur.rowcount > 0 else 0
    return inserted


def _dumps(d: dict) -> str | None:
    return json.dumps(d, default=tuple) if d else None


def _loads(raw: str | None) -> dict:
    if not raw:
        return {}
    data = json.loads(raw)
    return {k: tuple(v) for k, v in data.items()}


def _row_to_match(row: sqlite3.Row) -> Match:
    return Match(
        date=row["date"],
        league=row["league"],
        league_name=row["league_name"] or "",
        home=row["home"],
        away=row["away"],
        home_goals=row["home_goals"],
        away_goals=row["away_goals"],
        odds_1x2=_loads(row["odds_json"]),
        odds_open_1x2=_loads(row["odds_open_json"]),
        odds_ou25=_loads(row["odds_ou25_json"]),
        asian_handicap=_loads(row["asian_handicap_json"]),
    )


def get_matches(
    league: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
    finished_only: bool = False,
) -> list[Match]:
    """Query matches with optional filters. Returns chronological list."""
    init_db()
    clauses = []
    params: list = []
    if league:
        clauses.append("league = ?")
        params.append(league)
    if since:
        clauses.append("date >= ?")
        params.append(since)
    if until:
        clauses.append("date <= ?")
        params.append(until)
    if finished_only:
        clauses.append("home_goals IS NOT NULL AND away_goals IS NOT NULL")
    where = (" WHERE " + " AND ".join(clauses)) if clauses else ""
    sql = f"SELECT * FROM matches{where} ORDER BY date, league"
    with get_conn() as conn:
        rows = conn.execute(sql, params).fetchall()
    return [_row_to_match(r) for r in rows]


def count_matches() -> int:
    init_db()
    with get_conn() as conn:
        return conn.execute("SELECT COUNT(*) FROM matches").fetchone()[0]
