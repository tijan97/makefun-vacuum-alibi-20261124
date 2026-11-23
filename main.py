"""Entry program for make.fun's "The Vacuum's Alibi" bounty.

Writes one line (a robot vacuum's excuse for missing a spot,
119 characters) to /output/entry.txt. Standard library only;
no network, no clock, no files outside this repository.
"""

import os

LINE = (
    "Per my logs, the spot was cleaned at 14:02. "
    "The floor says otherwise. "
    "I trust my logs; they have never once apologized."
)


def main() -> None:
    # The brief's gate: one line, 1-200 characters, not only whitespace.
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(LINE) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(LINE)}"
        )
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
