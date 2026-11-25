#!/usr/bin/env python3
"""The Internet in One Word - entry program.

Writes a single word to /output/entry.txt. The word is "brainrot":
one word, funny on its own, true of the internet as a whole (endless
scrolling that melts attention), surprising rather than the first
obvious pick, and short enough to land in one beat. Alternatives
weighed and rejected: "chaos" and "memes" are the first obvious
words anyone reaches for; "doomscrolling" is true but longer and
less funny; "unhinged" names a mood more than the internet itself.
"""

import os

WORD = "brainrot"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
