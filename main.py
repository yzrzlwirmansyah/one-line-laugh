#!/usr/bin/env python3
"""One Line, One Laugh — entry.

The chosen line was picked for the sharpest turn: a dull, familiar form
(the emergency contact), inverted into a bureaucratic rejection — the twist
lands in the final two words.
"""

import os
import sys

LINE = 'My emergency contact asked to be moved to "general enquiries."'


def validate(line: str) -> None:
    """Reject empty, over-long, multi-line, or padded lines.

    A line with leading or trailing whitespace passes the length gate but
    wastes characters and looks sloppy, so it is rejected too.
    """
    if not line or not line.strip():
        sys.exit(2)
    if line != line.strip():
        sys.exit(2)
    if len(line) > 140:
        sys.exit(2)
    if "\r" in line or "\n" in line:
        sys.exit(2)


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
