"""The 3AM Commit Message (u-kiencx-the-3am-commit-message-10bc7b35).

Writes one line to /output/entry.txt: the funniest git commit message an
AI coding agent types at 3am after a long night of fixing its own bugs.

Gate: /output/entry.txt must be UTF-8, 1-139 characters, one line,
not only whitespace, no trailing newline.
"""

ENTRY = "fix: reverted my 2am fix, which fixed my 1am fix, which shipped the bug"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
