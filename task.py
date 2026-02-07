#!/usr/bin/env python3
"""Small task tracker: list and add tasks stored in tasks.txt."""

from __future__ import annotations

import sys
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.txt")


def load_tasks() -> list[str]:
    if not DATA_FILE.exists():
        return []
    return [line.strip() for line in DATA_FILE.read_text().splitlines() if line.strip()]


def save_tasks(tasks: list[str]) -> None:
    DATA_FILE.write_text("\n".join(tasks) + ("\n" if tasks else ""))


def print_usage() -> None:
    print("Usage:")
    print("  task.py list")
    print("  task.py add <task description>")


def main() -> int:
    if len(sys.argv) < 2:
        print_usage()
        return 1

    command = sys.argv[1].lower()
    tasks = load_tasks()

    if command == "list":
        if not tasks:
            print("No tasks yet.")
        else:
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        return 0

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task description.")
            return 1
        task = " ".join(sys.argv[2:]).strip()
        if not task:
            print("Task description cannot be empty.")
            return 1
        tasks.append(task)
        save_tasks(tasks)
        print(f"Added: {task}")
        return 0

    print_usage()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
