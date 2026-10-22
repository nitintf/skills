# Studio contract: the product planning files every `studio` skill obeys

The `studio` skills take a product from a raw idea to a locked plan: the problem,
the niche, the scope, the brand, a design system, every screen as a mockup, and
the architecture. They talk to each other **only through the files below**, so
each one runs alone or in `/studio-flow`, and a later session picks up where the
last one stopped.

**The defining rule: decide everything that keeps the product consistent before
the first line of app code.** A design value, a font, a folder or a framework
that is not written here gets invented differently on every screen. Writing it
once is the whole point.

---

## 1. Where the files live

Every product gets its own folder, `~/code/personal/<product-slug>/`, and the
planning files live in its `docs/product/`:

```
<project-root>/docs/product/
  README.md          # state: each step's status, and the decisions log (§3)
  IDEA.md            # /idea, plus the Scope section from /founder-review
  NICHE.md           # /niche
  BRAND.md           # /brand
  brand/             # logo and icon SVGs from /brand
  DESIGN.md          # /design-system: the why, and the rules
  tokens.json        # /design-system: every design value, the single source (§5)
  tokens.css         # generated from tokens.json, never edited by hand
  design/
    system.html      # the design system preview
    variants/<screen>/board.html   # /design-variants
    screens/index.html, <NN>-<screen>.html   # /mockups
  REVIEW.md          # /design-review
  ARCHITECTURE.md    # /tech-plan
```

For a new product, `/idea` creates `~/code/personal/<product-slug>/` with
`git init` and `docs/product/`, using the working title as the slug (renaming the
folder after `/brand` picks a name is fine). Every later step runs from that
folder. `docs/` is committed, so the plan and the code it produced share a
history, and the `eng` plugin's `.plan/` sits next to it once building starts.

## 2. How every studio skill asks a question

One decision per question. Each question carries:

- what is being decided, in one plain sentence;
- a **recommendation** and the reason, first;
- 2 to 4 options, each with its gain, its cost, and its effort;
- what happens if it is deferred.

Ask, wait, apply only what he chose. Never decide a taste question for him:
taste is his, and the skills exist to sharpen it, not replace it.

Write in plain English. Praise is not information: skip "great idea" and say
what is strong or weak about it, specifically.

## 3. `README.md`: state

```markdown
---
product: <slug>
created: <YYYY-MM-DD>
platform: ios, android     # the targets, from /idea
---
# <Product name or working title>

| Step | Status | File |
|---|---|---|
| idea | done 2026-10-24 | IDEA.md |
| niche | not started | NICHE.md |
| founder-review | not started | IDEA.md#Scope |
| brand | not started | BRAND.md |
| design-system | not started | DESIGN.md, tokens.json |
| design-variants | not started | design/variants/ |
| mockups | not started | design/screens/ |
| design-review | not started | REVIEW.md |
| tech-plan | not started | ARCHITECTURE.md |

## Decisions
| Date | Step | Decision | Why |
```

Every skill sets its own row (`in progress`, `done <date>`, `needs rework`) and
appends a row to `## Decisions` for each choice he makes. A later step that
changes an earlier decision says so, and marks that earlier step `needs rework`.

## 4. The interface thesis

`NICHE.md` ends in an **interface thesis**: one sentence on how this product
looks, feels and behaves differently from everything in its category, even with
the same features, and the evidence for it. `/design-system`, `/design-variants`,
`/mockups` and `/design-review` all measure their output against it. In a
crowded category the thesis is the product.

## 5. Design tokens

`tokens.json` holds every design value. Nothing else does.

```json
{
  "color": {
    "light": { "bg": "#...", "surface": "#...", "text": "#...", "text-muted": "#...",
               "primary": "#...", "on-primary": "#...", "border": "#...",
               "positive": "#...", "negative": "#...", "warning": "#..." },
    "dark":  { "...": "same keys as light" }
  },
  "font": {
    "display": { "family": "...", "source": "https://...", "weights": [600, 700] },
    "body":    { "family": "...", "source": "https://...", "weights": [400, 500] },
    "mono":    { "family": "...", "source": "https://...", "weights": [400] }
  },
  "type": {
    "display":  { "font": "display", "size": 34, "line": 40, "weight": 700, "tracking": -0.5 },
    "title":    { "font": "display", "size": 22, "line": 28, "weight": 600, "tracking": 0 },
    "body":     { "font": "body",    "size": 16, "line": 24, "weight": 400, "tracking": 0 },
    "label":    { "font": "body",    "size": 13, "line": 16, "weight": 500, "tracking": 0.2 },
    "number":   { "font": "mono",    "size": 28, "line": 32, "weight": 400, "tracking": 0 }
  },
  "space":  { "xs": 4, "sm": 8, "md": 12, "lg": 16, "xl": 24, "2xl": 32, "3xl": 48 },
  "radius": { "sm": 6, "md": 10, "lg": 16, "full": 999 },
  "motion": { "fast": 120, "base": 220, "slow": 360, "ease": "cubic-bezier(0.2, 0, 0, 1)" }
}
```

Units are points (pixels on the web). The key names above are the minimum: a
product may add keys (a chart palette, an `elevation` group), never remove them.

**Generate, never hand-write, the derived files:**

```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tokens.py docs/product/tokens.json --css docs/product/tokens.css
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tokens.py docs/product/tokens.json --ts src/theme/tokens.ts
```

The CSS has one custom property per token (`--color-primary`, `--space-lg`,
`--type-body-size`, and so on) with dark values under `[data-theme="dark"]`. The
TS export is what the app imports, written by `/tech-plan`.

## 6. Mockups

- Self-contained HTML that links `tokens.css` and uses **only** its custom
  properties for colour, type, spacing, radius and motion.
- **The frame follows the platforms in `README.md`:**

  | Platforms | Mockups |
  |---|---|
  | iOS or Android (any mobile) | Mobile-first: every screen in a 390 by 844 phone frame, with iOS or Android conventions for navigation and controls |
  | Web only | Desktop-first at 1440 wide, plus a 375 wide check of each screen |
  | Mobile and web | Phone frames for every screen first, then the web layouts of the same screens |
- Real content, never lorem ipsum: realistic names, amounts, dates, and the
  messy cases (a long name, a zero balance, a failed sync).
- Every screen shows its states: default, empty, loading, error, and any state
  specific to it.
- A light and dark toggle on every page.

Open them with `open <file>` so he sees them in the browser. If the session can
publish a private page, offer that too, so he can check them on his phone.

## 7. Drift

Drift is any colour, size, spacing, radius or font in a mockup or in app code
that does not come from the tokens. Find it with:

```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/drift.py <paths...>
```

It prints `file:line: value` for every raw hex, `rgb()`, pixel size and font
family outside the token files. Zero lines is the bar. A value that genuinely
needs to exist becomes a token first, then gets used.

## 8. What the other plugins read

- `eng` treats `DESIGN.md`, `tokens.json` and `ARCHITECTURE.md` as binding
  decisions, ahead of anything inferred from the code (its `SPEC.md` §6).
- `/tech-plan` adds a `## Product plan` block to the project's `CLAUDE.md`:
  read `docs/product/DESIGN.md` and `ARCHITECTURE.md` before UI or structural
  work, use only tokens, and flag drift.
- `/prd` and `/user-stories` in `product` read `IDEA.md` when present.
