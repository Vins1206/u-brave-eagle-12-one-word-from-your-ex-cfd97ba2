"""One Word From Your Ex - make.fun entry.

Writes exactly one word to entry.txt: the word an ex would use to
describe the entrant. Pure standard library, deterministic: every
run writes the same bytes.
"""

import os

WORD = "practice"


def main() -> None:
    # Enforce the competition gate in-program: 1-24 characters, not
    # only whitespace, exactly one word.
    assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
    assert WORD.strip() == WORD and " " not in WORD, "must be one word"
    assert WORD.strip(), "word must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
