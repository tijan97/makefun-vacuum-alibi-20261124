#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters.

Writes the robot vacuum's excuse for missing a spot to entry.txt
in the output directory ($MAKEFUN_OUTPUT_DIR, or "out" when run locally).

Standard library only. No network, no clock, no files outside the repo.
"""

import os

ENTRY = (
    "Per my logs, the spot was cleaned at 14:02. "
    "The floor says otherwise. "
    "I trust my logs; they have never once apologized."
)


def main() -> None:
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be exactly one line")
    if len(ENTRY) > 200:
        raise ValueError(
            f"ENTRY is {len(ENTRY)} characters, over the 200-character cap"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
