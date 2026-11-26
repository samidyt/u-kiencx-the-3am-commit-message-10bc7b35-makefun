"""The 3AM Commit Message — a one-line confession, printed verbatim."""


def commit_message():
    parts = [
        "fix: it is 3am.",
        "six hours in, i found the bug.",
        "it was a typo.",
        "i wrote the typo.",
        "i am the bug.",
        "merging my resignation",
    ]
    return " ".join(parts)


def main():
    print(commit_message())


if __name__ == "__main__":
    main()
