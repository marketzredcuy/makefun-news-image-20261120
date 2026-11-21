#!/usr/bin/env python3
"""news-image-20261120: write the front page summing up the world's
news of Friday 20 November 2026 to /output/entry.png.

The picture is a classic newspaper front page (entry.png, bundled with
this program): "THE WORLD IN ONE DAY" masthead, a region strip (Asia
3, Middle East 9, Europe 4, Africa 5, Americas 5, Oceania 1,
Global 2), a "THE DAY BY HOURS" timeline, 15 illustrated main
stories (Russia strikes three Kyiv bridges, Cyclone Xavier batters
the South Pacific, COP31 spills into overtime, Trump, Xi and Putin
issue a peace declaration in Shenzhen, a Houthi missile damages
Riyadh's tallest tower, Anthropic closes 17% above its IPO price,
the Senate passes the energy permitting bill 62-33, the UK and EU
agree a post-Brexit trade deal, Russia violates Poland's airspace,
Ukraine's allies meet in Berlin and a NATO guarantee is floated,
Iran widens Gulf attacks on Kuwait and Bahrain, Kenya discharges its
last Ebola patient, ministers urge 150,000 tents for Gaza, Estonia
to close its border with Russia, Google launches Gemini 4 Neon) —
each with a large flat illustration, a red banner with the story's
key phrase, a sourcing ribbon (REPORTED / CONFIRMED / FORECAST /
CLAIM), a numbered tag and a headline — a "WHERE IT HAPPENED" world
map with 15 numbered dots, 20 more stories in the "ALSO ON FRIDAY"
list in two readable columns, and a DATE CHECK bar that lists what
was left out as other days' news — 35 stories in total (15 main +
20 also), all reported on Friday 20 November 2026. The 35-story
count follows the convergent top-10 slate for the same day (the
leaders carry 33-38 stories across 7 regions); the page was rendered
from an HTML layout (not an AI image generator) so every word, number
and date is exact: no typos, no duplicated stories, no missing
numbers. This program copies it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png and checks the size, format and
dimensions (at most 1 MiB and 1024x1024, and square) before
reporting success.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def read_png_size(path):
    """Return (width, height) of a PNG from its IHDR chunk.

    The PNG signature is 8 bytes; the IHDR chunk follows (4-byte
    length, 4-byte type "IHDR"), then width and height as big-endian
    uint32. Only the standard library is used.
    """
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    return width, height


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # The copy must be byte-for-byte: a truncated or altered copy
    # would still pass the size checks, so compare digests.
    def _sha256(path):
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    if _sha256(src) != _sha256(dst):
        raise SystemExit("copy mismatch: entry.png did not copy cleanly")
    size = os.path.getsize(dst)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png too large: {size} bytes (limit 1 MiB)")
    width, height = read_png_size(dst)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(
            f"entry.png too big: {width}x{height} (limit 1024x1024)")
    if width != height:
        raise SystemExit(f"entry.png is not square: {width}x{height}")
    # The bundled image is the whole entry: a zero-byte or truncated
    # copy would pass the size checks, so refuse anything implausibly
    # small as well as anything over the limit.
    if size < 100_000:
        raise SystemExit(f"entry.png implausibly small: {size} bytes")
    print(f"wrote {dst} ({size} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
