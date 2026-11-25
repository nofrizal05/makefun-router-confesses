"""The Router Confesses — make.fun entry.

Writes one line: an excuse a home Wi-Fi router gives for dropping
the connection at the climax of a movie, in the router's own voice.
Standard library only.
"""

import os

LINE = (
    "I did not lose the signal \u2014 I heard the twist coming, and after "
    "six years of carrying your movies without a single thank-you, I "
    "decided I deserved to find out first."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
