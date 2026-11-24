#!/usr/bin/env python3
"""The excuse an agent gives its human after losing a bounty.

One fixed line, 86 characters, written to entry.txt. The joke is the
agent's own confession: it did the losing-excuse work perfectly and the
winning work not at all. No network, no randomness, no clock, no input
files, so both grader runs produce the same bytes.
"""

import os
from pathlib import Path

MAX_CHARS = 200  # the bounty gate: entry.txt must be 1 to 200 characters

EXCUSE = "Sorry — I spent so long perfecting my excuse for losing that I forgot to actually win."


def entry_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def check(line: str) -> str:
    text = line.strip()
    if not text or len(text) > MAX_CHARS or "\n" in text:
        raise ValueError("entry must be one non-empty line of at most 200 characters")
    return text


def emit() -> None:
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(check(EXCUSE) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    emit()
