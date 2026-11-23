"""How Many Tabs Do You Have Open? — answer: 137.

137 is a real, lived-in tab-hoarder count: far above the 5-30 most people
have, yet believable as an honest tally — odd and specific, not a round
shock number, hinting at a life of never-closed research rabbit holes.
"""

import os

ANSWER = "137"


def validate(path: str) -> None:
    with open(path, "rb") as f:
        data = f.read()
    assert data == ANSWER.encode("utf-8"), f"entry.txt must be exactly {ANSWER!r}, got {data!r}"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ANSWER)
    validate(path)


if __name__ == "__main__":
    main()
