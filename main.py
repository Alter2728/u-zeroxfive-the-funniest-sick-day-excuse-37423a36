#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

DRAFT entry (replaced — too soft, punch lands mid-sentence):
    Woke up with my back out after sneezing in the shower — I am horizontal, negotiating with my spine, and losing.

REVISED entry (final):
    I sneezed so hard this morning I pulled a muscle I didn't know existed, and now I walk like a folding chair.

The draft is funny but soft: "negotiating with my spine" is a decent image,
yet the punch lands mid-sentence and the line spends words setting up the
shower. The revision keeps the sneeze (fresh, half-believable, not a fever /
dog / dead grandmother) and moves the laugh to the very last words — the
folding chair — in a voice that sounds like a real text to a boss.
"""

import os

# Revised line — the sneeze injury, punch on the last words.
ENTRY = "I sneezed so hard this morning I pulled a muscle I didn't know existed, and now I walk like a folding chair."


def output_path() -> str:
    """Resolve where entry.txt goes.

    The harness sets MAKEFUN_OUTPUT_DIR to the output directory; when it
    is unset we fall back to /output/entry.txt.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must not have surrounding whitespace"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file is exactly the entry text.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}: {ENTRY}")


if __name__ == "__main__":
    main()
