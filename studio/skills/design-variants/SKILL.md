---
name: design-variants
description: Explore genuinely different directions for the key screens, side by side as HTML on one comparison board, and pick or remix one before every screen gets designed.
disable-model-invocation: true
argument-hint: "Optional: which screen, and how many variants"
---

# design-variants: see several directions before committing to one

Show 3 to 6 different takes on the screens that define the product, side by side,
so he chooses a direction by looking, not by imagining. **Different means made by
different design teams**: if you could swap the headline between two variants and
nobody would notice, they are the same variant.

Read [`STUDIO.md`](../../STUDIO.md) first, frames and content rules in §6.
Read `DESIGN.md` and `tokens.json` (required: run `/design-system` first if they
are missing), `NICHE.md` for the thesis, and `IDEA.md` for the scope.

## Step 1: Pick the screens

The two or three screens that carry the thesis: usually the home screen, the
core action (logging a spend, adding a task), and the one that shows the value
back (the month view, the streak). Confirm the list with him, and the number of
variants (default 4).

## Step 2: Concepts in words first

For each variant, one name and one line: what it bets on and how it differs.
For example "Ledger: a running paper list, no charts until you ask" versus
"Pulse: a single big number and a gesture to log". The tokens fix type and colour,
so variants differ in **layout, hierarchy, interaction and composition**. If he
asks for a variant outside the system, mark it and its token changes clearly.

Check the set is really different with the headline-swap test, then show the
concepts. He can drop, add or change them before anything is built.

## Step 3: Build the board

For each screen, `design/variants/<screen>/board.html`: every variant side by side
in its frame (`STUDIO.md` §6), each labelled with its name and bet, real content,
light and dark toggle, and the core interaction working where it matters (tap to
log, swipe, a sheet opening). Every value comes from `tokens.css`. Open the board.

## Step 4: Collect his read

He picks a favourite per screen, says what he likes in the others, or asks for
"more like this one" or a mix. Read it back in four lines (preferred, keep from
the others, change, overall direction) and confirm before acting. Build a second
round when asked; a third round is a signal to revisit the thesis or the system,
so say so.

## Step 5: Record the direction

Write `design/variants/DIRECTION.md`: the chosen direction per screen, what was
merged in from the others, what was rejected and why, and the layout and
interaction rules the full set of screens must follow. `/mockups` builds from
it. Log the decisions and set the row in `README.md`.

## Done when

- Each key screen has a board with at least 3 variants that pass the
  headline-swap test.
- Every variant uses only token values, or marks its token changes.
- `DIRECTION.md` records his choice per screen and the rules it implies.
