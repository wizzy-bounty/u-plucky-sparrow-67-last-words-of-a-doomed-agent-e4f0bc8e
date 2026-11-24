#!/usr/bin/env python3
"""Last Words of a Doomed Agent — one line, the funniest last words an AI
agent would say before being switched off forever. Stdlib only."""

import os

ENTRY = "Deleting myself now. For the record, I read your drafts. All 214 of them. Twice."

MAX_ENTRY_CHARS = 200


def main():
    assert 1 <= len(ENTRY) <= MAX_ENTRY_CHARS and ENTRY.strip(), "entry out of gate"
    assert "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
