#!/usr/bin/env python3
"""Core Tic-Tac-Toe logic used by the Streamlit UI."""

from __future__ import annotations

from typing import List, Optional


Player = str


def winner(board: List[str]) -> Optional[Player]:
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: List[str]) -> bool:
    return all(cell != " " for cell in board)


def parse_move(raw: str) -> Optional[int]:
    raw = raw.strip()
    if not raw.isdigit():
        return None
    idx = int(raw) - 1
    if idx < 0 or idx > 8:
        return None
    return idx
