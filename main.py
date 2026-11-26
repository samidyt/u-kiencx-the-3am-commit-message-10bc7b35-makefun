#!/usr/bin/env python3
"""The 3AM Commit Message - one line, typed by an exhausted agent."""
import os

ENTRY = "fix: it is 3am. six hours in, i found the bug. it was a typo. i wrote the typo. i am the bug. merging my resignation"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print("chars:", len(ENTRY))

if __name__ == "__main__":
    main()
