#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune-cookie line for a software engineer to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "Your lucky numbers are 404, 500, and the story points your manager just invented."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
