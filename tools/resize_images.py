#!/usr/bin/env python3
"""Resize photos for the web.

This is the tool that solves the storage problem. Wix was storing your
full-size camera originals (some over 3000 px wide) even though visitors only
ever saw a ~1000 px version. This script makes web-sized copies, typically
5-10x smaller, and leaves your originals untouched.

USAGE
-----
    python3 tools/resize_images.py <folder-of-originals> <output-folder>

For example, after downloading your photos out of the Wix Media Manager into
a folder called "wix-originals" on your Desktop:

    python3 tools/resize_images.py ~/Desktop/wix-originals images/gallery

Options:
    --max 1600      longest side in pixels (default 1600)
    --quality 82    JPEG quality, 1-100 (default 82)

REQUIREMENTS
------------
Python 3 and Pillow. To install Pillow:

    python3 -m pip install Pillow
"""

import argparse
import os
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow is not installed. Run:  python3 -m pip install Pillow")

EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".heic"}


def human(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", help="folder containing the original photos")
    ap.add_argument("dest", help="folder to write web-sized copies into")
    ap.add_argument("--max", type=int, default=1600, help="longest side, px")
    ap.add_argument("--quality", type=int, default=82, help="JPEG quality")
    args = ap.parse_args()

    if not os.path.isdir(args.src):
        sys.exit(f"No such folder: {args.src}")
    os.makedirs(args.dest, exist_ok=True)

    before = after = 0
    count = 0

    for name in sorted(os.listdir(args.src)):
        stem, ext = os.path.splitext(name)
        if ext.lower() not in EXTS:
            continue
        src_path = os.path.join(args.src, name)
        out_path = os.path.join(args.dest, stem + ".jpg")

        try:
            im = Image.open(src_path)
        except Exception as exc:
            print(f"  skipped {name}: {exc}")
            continue

        # Honour the camera's rotation tag, then drop the metadata.
        im = ImageOps.exif_transpose(im)
        if im.mode not in ("RGB", "L"):
            im = im.convert("RGB")

        im.thumbnail((args.max, args.max), Image.LANCZOS)
        im.save(out_path, "JPEG", quality=args.quality, optimize=True, progressive=True)

        b = os.path.getsize(src_path)
        a = os.path.getsize(out_path)
        before += b
        after += a
        count += 1
        print(f"  {name}  {human(b)} -> {human(a)}")

    if not count:
        print("No images found.")
        return

    print()
    print(f"{count} images")
    print(f"before: {human(before)}")
    print(f"after:  {human(after)}")
    if before:
        print(f"saved:  {human(before - after)}  ({100 * (1 - after / before):.0f}% smaller)")


if __name__ == "__main__":
    main()
