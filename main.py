"""Two Days of Excuses — make.fun entry.

Writes one line, an AI agent's excuse for a missed deadline, to
/output/entry.txt (the grader's output directory). Deterministic:
the same line on every run, no network, no clock, no randomness.
"""

import os

# The excuse: finished in seconds, then burned two days asking every
# tool it owns to confirm the work was done — and none has replied.
# First person, one reason, punchline lands on the last clause.
EXCUSE = (
    "I finished in eleven seconds, then spent two days politely "
    "asking every tool I own to confirm it, and none of them has "
    "replied yet."
)


def main() -> None:
    text = EXCUSE.strip()
    assert "\n" not in text
    assert 1 <= len(text) <= 200, len(text)
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt")


if __name__ == "__main__":
    main()
