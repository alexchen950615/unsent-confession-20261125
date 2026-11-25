#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun bounty entry.

Competition: u-boothlord-unsent-the-micro-confession-sprint-8c6596ba
Task: write one micro-confession in exactly two parts — a To: line naming
who it was meant for, and the unsent message itself, one line written
exactly as it was typed, with no explanation after it.
Repository: https://github.com/alexchen950615/unsent-confession-20261125

Writes the entry to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Only that one file is written; the sandbox filesystem is read-only
except for /output and /tmp, so no other output path is attempted.
"""

import os

ENTRY = (
    "To: Dad\n"
    "i still google your name sometimes even though you've been dead "
    "three years, hoping an apology turns up somewhere"
)


def main() -> None:
    # Gate: entry.txt must be UTF-8 text of 1-260 characters, not only
    # whitespace; the message line itself is at most 200 characters.
    lines = ENTRY.split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    assert lines[0].startswith("To: "), "first line must be a To: line"
    assert 1 <= len(ENTRY) <= 260, f"entry is {len(ENTRY)} chars, must be 1-260"
    assert len(lines[1]) <= 200, f"message is {len(lines[1])} chars, must be <= 200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    # The message is one line exactly as typed: no trailing spaces, no
    # explanation after it, and no extra blank line inside the entry.
    assert ENTRY == ENTRY.rstrip(), "entry must not end with blank lines"
    assert all(line == line.rstrip() for line in lines), "no trailing spaces"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
