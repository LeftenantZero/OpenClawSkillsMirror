"""Adapter protocol.

Adapters normalise raw data from any source into the unified Match schema.
The football-data.co.uk adapter is built-in; users can implement this protocol
to plug in authorised Chinese sources (e.g. 竞彩 official public data) without
the project shipping a scraper.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable

from .schema import Match


@runtime_checkable
class DataAdapter(Protocol):
    """A source of historical (and optionally upcoming) matches."""

    def fetch(self, league: str, seasons: list[str]) -> list[Match]:
        """Return matches for the given league and season codes.

        Seasons are league-specific shorthand, e.g. ["2324"] for 2023-24 in the
        football-data.co.uk scheme. Adapters define their own season format.
        """
        ...
