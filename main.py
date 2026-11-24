"""Dog Ate My Homework — make.fun entry.

A tiny deterministic program: it writes one line, the excuse a dog gives
after being caught eating the homework, to /output/entry.txt. No network,
no randomness, no clock — the same bytes every run.
"""

from pathlib import Path

# The excuse, in the dog's own voice. The dog is not sorry: anything left
# on the floor is fair game until somebody says the magic word "submit".
ENTRY = "It was on the floor, which is legally a chew toy until someone says 'submit.'"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
