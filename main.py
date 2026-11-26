#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun bounty entry.

Writes one voicemail greeting, as recorded by a cat named Miso, to
/output/entry.txt. The line is 119 characters, within the 120-character
limit, and is written exactly once with no trailing newline.
"""

import os

ENTRY = (
    "Hi, it's Miso. About the vase, I did it and I'd do it again. "
    "Leave a message after the beep. I'm in the box it came in."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, must be 1-120"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.isascii(), "entry must be pure ASCII"
    assert not ENTRY.endswith("\n"), "entry must have no trailing newline"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="ascii", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
