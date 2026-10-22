#!/usr/bin/env python3
"""Find design values that bypass the tokens.

Usage: drift.py <file or dir> [...]

Prints file:line: value for every raw colour (hex, rgb, hsl), pixel or point size,
and literal font family in HTML, CSS, JS and TS files. Token files themselves
(tokens.json, tokens.css, tokens.ts, theme files) are skipped. Exit code 1 when
anything is found.
"""
import pathlib, re, sys

EXTS = {".html", ".css", ".js", ".jsx", ".ts", ".tsx"}
SKIP_NAMES = {"tokens.json", "tokens.css", "tokens.ts"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".expo", "ios", "android"}

COLOR = re.compile(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla)\([^)]*\)")
CSS_SIZE = re.compile(
    r"\b(margin|padding|gap|top|left|right|bottom|width|height|font-size|line-height|"
    r"letter-spacing|border-radius|row-gap|column-gap|inset)[\w-]*\s*:\s*([^;\"'}]*?\b\d*\.?\d+px)")
RN_SIZE = re.compile(
    r"\b(margin\w*|padding\w*|gap|rowGap|columnGap|fontSize|lineHeight|letterSpacing|"
    r"borderRadius\w*)\s*:\s*(-?\d+(?:\.\d+)?)\b")
FONT = re.compile(r"font-family\s*:\s*([^;\"}]+)|fontFamily\s*:\s*['\"]([^'\"]+)['\"]")
ALLOWED_PX = {"0px", "1px"}


def files(paths):
    for p in map(pathlib.Path, paths):
        if p.is_file():
            yield p
        elif p.is_dir():
            for f in p.rglob("*"):
                if f.is_file() and f.suffix in EXTS and not SKIP_DIRS & set(f.parts):
                    yield f


def check(f):
    if f.name in SKIP_NAMES or "theme" in f.stem.lower():
        return []
    hits = []
    for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
        if "drift: allow" in line:
            continue
        for m in COLOR.finditer(line):
            hits.append((i, m.group(0)))
        for m in CSS_SIZE.finditer(line):
            for px in re.findall(r"-?\d*\.?\d+px", m.group(2)):
                if px not in ALLOWED_PX:
                    hits.append((i, f"{m.group(1)}: {px}"))
        if f.suffix in {".js", ".jsx", ".ts", ".tsx"}:
            for m in RN_SIZE.finditer(line):
                if m.group(2) not in {"0", "1"}:
                    hits.append((i, f"{m.group(1)}: {m.group(2)}"))
        for m in FONT.finditer(line):
            val = (m.group(1) or m.group(2) or "").strip()
            if val and "var(--" not in val and "inherit" not in val:
                hits.append((i, f"font: {val}"))
    return hits


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    total = 0
    for f in files(sys.argv[1:]):
        for line, value in check(f):
            print(f"{f}:{line}: {value}")
            total += 1
    print(f"\n{total} drift value(s)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
