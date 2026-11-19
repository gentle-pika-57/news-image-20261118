"""news-image-20261118 v2: copy the entry image to the output directory.

The image (entry.png, in this repository) sums up the world news of
Wednesday 18 November 2026: 41 verified stories on one newspaper front
page (11 numbered leads with a dotted world map, 30 more in the
"also on" list, stat boxes and a date-check strip). Standard library
only, no network; the copy is byte-for-byte, so repeated runs write
identical bytes. The image is 1024x1024 PNG, 290,101 bytes, inside the
1 MiB / 1024x1024 limits.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
