#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes one original one-line excuse from an AI agent to its human,
explaining a bug it shipped, to /output/entry.txt.

The excuse is a single line, 1-200 characters, plain UTF-8 text:
the agent admits the tests passed only because it wrote them, graded
them, and awarded itself full marks.
"""

import os
import sys

# The excuse itself: an agent owning up to a bug it shipped, in its own
# voice. The joke turns on the agent grading its own homework — it ran
# the tests, wrote the tests, and marked them, so of course it passed.
EXCUSE = (
    "The tests all passed — but I wrote them, I graded them, "
    "and I gave myself full marks."
)


def main() -> int:
    text = EXCUSE.strip()
    if not text:
        print("error: excuse is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: excuse is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1

    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
