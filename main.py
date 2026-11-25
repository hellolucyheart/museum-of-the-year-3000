#!/usr/bin/env python3
"""Museum of the Year 3000 -- one museum label, written by a program.

The brief asks for a single line: the label a museum in the year 3000
puts beside an ordinary object from today. The line must be at most 200
characters, in English, original, and read like a real museum label:
short, straight faced and confident, with the joke landing on the first
read and the humour coming from the year 3000 misreading the object.

The object is the group chat. The label states what it was, deadpan --
forty-seven humans gathering daily to decide nothing -- and then lets
the curators of the year 3000 draw the wrong, confident conclusion:
that it must have been a religious ritual. Nothing in the line explains
its own joke; the misreading is the joke.

The program is deterministic on purpose: the grader runs it twice and
both runs must produce the same entry. It reads nothing from the network,
the environment (beyond the output directory the grader itself sets) or
the git history. The label lives in this file, and this file alone.

It validates the label against the brief's own gate (UTF-8 text, 1 to 200
characters, not only white space, a single line) and writes the exact text,
with no trailing newline, to ``entry.txt`` inside the output directory the
grader provides (``MAKEFUN_OUTPUT_DIR``, default ``/output``).
"""

from __future__ import annotations

import os
import sys

# The label, written for this bounty. 127 characters, one line.
LABEL = (
    "Group chat (c. 2025). Forty-seven humans gathered here daily to "
    "decide nothing. Scholars now believe it was a religious ritual."
)

MAX_CHARS = 200


def validate_label(label: str) -> str:
    """Return the label when it passes the brief's gate, else fail loudly."""
    text = label.strip()
    if not text:
        raise ValueError("label is empty")
    if label != text:
        raise ValueError("label has leading or trailing white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"label is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("label must be a single line")
    if any(ord(char) < 0x20 for char in text):
        raise ValueError("label holds a control character")
    if len(text.encode("utf-8")) > MAX_CHARS:
        raise ValueError("label is over the limit in bytes as well as characters")
    if not text.isascii():
        raise ValueError("label must be plain ASCII English text")
    return text


def main() -> int:
    text = validate_label(LABEL)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
