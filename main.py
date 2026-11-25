#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single-line fridge roast to /output/entry.txt for the
make.fun bounty u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.
Pure standard library only; deterministic output.
"""

import os

ROAST = (
    "My fridge's ice maker sounds like it's chewing gravel, "
    "then spits out three cubes like it's doing me a favour."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the sealed scorer's gate: 1-200 chars, one line, not blank.
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert "\n" not in ROAST and ROAST.strip(), "roast must be one non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)
    print(f"({len(ROAST)} characters)")


if __name__ == "__main__":
    main()
