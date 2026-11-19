"""news-image-20261118: copy the entry image to the output directory.

The image (entry.png, in this repository) sums up the world news of
Wednesday 18 November 2026. Standard library only, no network; the copy
is byte-for-byte, so repeated runs write identical bytes.
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
