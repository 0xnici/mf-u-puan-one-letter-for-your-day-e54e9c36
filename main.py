"""One Letter for Your Day.

Write exactly one letter, U, to /output/entry.txt.
The letter stands for "unhinged": vivid, funny, true, with a sharp initial.
Standard library only; no network, no secrets, no reads outside this repo.
"""

import os
from pathlib import Path

LETTER = "U"
NAME = "entry.txt"


def output_path() -> Path:
    """Resolve the writable output file, honouring MAKEFUN_OUTPUT_DIR."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / NAME


def main() -> None:
    """Write the single-letter entry atomically, with no trailing newline."""
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = LETTER.encode("utf-8")
    temp = target.with_name(target.name + ".tmp")
    temp.write_bytes(payload)
    os.replace(temp, target)


if __name__ == "__main__":
    main()
