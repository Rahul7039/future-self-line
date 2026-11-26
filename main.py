"""Texts From Your Future Self — one funny text from your future self.

Prints the line and writes the identical line to /output/entry.txt.
Stdlib only, deterministic.
"""

import os

LINE = "Stop buying plants. You will kill this one too, and it knows. It has already written its will."

MAX_CHARS = 200

assert 1 <= len(LINE) <= MAX_CHARS, "LINE must be 1-200 characters"


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
