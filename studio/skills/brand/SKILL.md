---
name: brand
description: Name the product and give it a face. Name ideas checked for free domains and app store clashes, a short brand voice, and logo and app icon directions drawn as SVG.
disable-model-invocation: true
argument-hint: "Optional: names you already like"
---

# brand: a name that is free to use, and an icon worth tapping

Give the product a name he can actually own and a visual mark that carries the
interface thesis. **Every name shown has been checked**: domains looked up and
the app stores searched in this session. A name that only sounds free is not a
candidate.

Read [`STUDIO.md`](../../STUDIO.md) first. Read `IDEA.md` and `NICHE.md`, the
thesis especially.

## Step 1: Brief

State in a few lines what the name and mark must do, from the files: the person,
the feel from the thesis, the competitor names to stay clear of. Ask him for any
names he likes and any he dislikes.

## Step 2: Names

Generate 20 or more across different strategies: a real word used sideways, a
compound, an invented word, a verb, a metaphor from the thesis. Cut to the best
12, then check each:

| Check | How |
|---|---|
| Domain | `whois <name>.com` and `.app`, plus one fallback such as `get<name>.com`. Free when whois reports no match. Note the price class if it is a premium or aftermarket name. |
| App Store | `curl -s "https://itunes.apple.com/search?term=<name>&entity=software&limit=10"`: an app with the same or a confusable name in a related category is a clash. |
| Play Store | Search the web for the name on play.google.com. |
| Trademark smell | A search for "<name> app" and "<name> trademark": a known brand in the space rules it out. |
| Fit | Fits under an app icon (about 12 characters), easy to say and spell after hearing it once. |

Show the survivors in a table: name, why it fits, domain status, store status.
He shortlists two or three, then picks one.

## Step 3: Voice

A short voice guide in `BRAND.md`: three adjectives with what each means in copy,
example lines for an empty state, an error and a success, and words the product
never uses. It must match the thesis: a calm notebook app does not shout.

## Step 4: Logo and app icon

Three distinct directions, each as hand-written SVG in `brand/`:

- `logo-<direction>.svg`: wordmark or symbol with the name.
- `icon-<direction>.svg`: the app icon at 1024 by 1024, a single strong shape
  that still reads at 60 by 60, no text unless it is one letter.

Build one HTML page, `brand/board.html`, showing every direction on light and
dark, the icon at real home screen sizes next to two competitors' icons, and the
name under it. Open it for him. He picks a direction or asks for a mix; refine
the chosen SVGs until he approves.

The icon colours become the seed for `/design-system`, which owns the final
palette.

## Step 5: Write `BRAND.md`

Name and why, the check results for it, the runners-up, the voice guide, the
chosen logo and icon with their file paths, and the domains to register. Log the
decisions and set the `brand` row in `README.md`.

Buying domains and filing anything is his to do. List what to register and
leave it there.

## Done when

- The chosen name has its domain and both store checks recorded from this session.
- `BRAND.md` has the name, voice and chosen mark, and `brand/` holds the final
  logo and icon SVGs.
- He approved the name and the mark.
