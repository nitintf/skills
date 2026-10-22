#!/usr/bin/env python3
"""Generate tokens.css and/or a TypeScript theme from a studio tokens.json.

Usage:
  tokens.py tokens.json --css out/tokens.css
  tokens.py tokens.json --ts src/theme/tokens.ts
"""
import argparse, json, pathlib, sys


def flat(prefix, obj):
    for k, v in obj.items():
        name = f"{prefix}-{k}" if prefix else k
        if isinstance(v, dict):
            yield from flat(name, v)
        elif isinstance(v, list):
            yield name, ", ".join(str(x) for x in v)
        else:
            yield name, v


def css_value(name, v):
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        if name.startswith(("space-", "radius-")) or name.endswith(("-size", "-line", "-tracking")):
            return f"{v}px"
        if name.startswith("motion-"):
            return f"{v}ms"
    return str(v)


def to_css(t):
    out = ["/* Generated from tokens.json by studio's tokens.py. Do not edit. */"]
    imports = sorted({f["source"] for f in t.get("font", {}).values() if f.get("source")})
    out += [f'@import url("{u}");' for u in imports]
    out.append(":root {")
    colors = t.get("color", {})
    for k, v in colors.get("light", {}).items():
        out.append(f"  --color-{k}: {v};")
    for role, f in t.get("font", {}).items():
        out.append(f"  --font-{role}: \"{f['family']}\", system-ui, sans-serif;")
    for group in ("type", "space", "radius", "motion"):
        for name, v in flat(group, t.get(group, {})):
            if name.startswith("type-") and name.endswith("-font"):
                out.append(f"  --{name}: var(--font-{v});")
            else:
                out.append(f"  --{name}: {css_value(name, v)};")
    for group, vals in t.items():
        if group in ("color", "font", "type", "space", "radius", "motion"):
            continue
        for name, v in flat(group, vals if isinstance(vals, dict) else {group: vals}):
            out.append(f"  --{name}: {css_value(name, v)};")
    out.append("}")
    if "dark" in colors:
        out.append('[data-theme="dark"] {')
        out += [f"  --color-{k}: {v};" for k, v in colors["dark"].items()]
        out.append("}")
    return "\n".join(out) + "\n"


def to_ts(t):
    body = json.dumps(t, indent=2)
    return ("// Generated from docs/product/tokens.json by studio's tokens.py. Do not edit.\n"
            f"export const tokens = {body} as const;\n\nexport type Tokens = typeof tokens;\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tokens")
    ap.add_argument("--css")
    ap.add_argument("--ts")
    a = ap.parse_args()
    t = json.loads(pathlib.Path(a.tokens).read_text())
    for key in ("color", "font", "type", "space", "radius", "motion"):
        if key not in t:
            sys.exit(f"tokens.json is missing the '{key}' group")
    if not (a.css or a.ts):
        sys.exit("pass --css and/or --ts")
    for path, text in ((a.css, to_css(t) if a.css else None), (a.ts, to_ts(t) if a.ts else None)):
        if path:
            p = pathlib.Path(path)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text)
            print(f"wrote {p}")


if __name__ == "__main__":
    main()
