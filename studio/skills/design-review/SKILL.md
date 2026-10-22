---
name: design-review
description: Review the mockups (or the built app) like a senior product designer. Six scored passes, a drift check against the tokens, and a fix-and-re-rate loop until every pass reaches 8.
disable-model-invocation: true
argument-hint: "Optional: mockups (default) or app"
---

# design-review: score it, find the gaps, close them

Review the design the way a demanding product designer would, and improve it with
him until it is ready to build. **The overall score is the lowest pass**, so one
weak area cannot hide behind strong ones. The result is better screens, not a
report about them.

Read [`STUDIO.md`](../../STUDIO.md) first. Read `NICHE.md` (the thesis),
`DESIGN.md`, `tokens.json`, `DIRECTION.md` and the screens in `design/screens/`.
Pass `app` to review the running app's screens or source instead; the passes are
the same.

## Step 1: Drift

Run `drift.py` (`STUDIO.md` §7) over the mockups, or over the app's source with
`app`. List every hit with `file:line`. Drift is fixed before scoring, because a
review of an inconsistent design scores noise.

## Step 2: Six passes, each 0 to 10

For each pass: the score, "it is a N because...", and **what a 10 would look like
for this product**, specifically.

| # | Pass | What it checks |
|---|---|---|
| 1 | Hierarchy | On each screen, what is seen first, second, third. Is that the right order for the screen's job? |
| 2 | States | Every feature in loading, empty, error, success and partial. What does the user actually see in each? |
| 3 | Journey | First launch to first value, and the daily loop: steps, taps, and how it feels at each step |
| 4 | Thesis and distinctiveness | Would a stranger recognise this product from one screen? Does it do what `NICHE.md` promised, or has it drifted back to the category's sameness? Any of the generic AI looks (`/design-system` Step 3)? |
| 5 | System fit | Do screens use the components and rules in `DESIGN.md`? Are its Do and Don't rules kept? Same thing, same look, everywhere? |
| 6 | Accessibility and platform | Contrast, dynamic type, 44 point targets, VoiceOver and TalkBack labels, safe areas, reduced motion, platform conventions |

Then an unscored list: **decisions still open**, each with what happens if it is
left to whoever builds it ("the engineer ships 'No items found.'").

## Step 3: Fix and re-rate

Take the lowest pass first. For each issue: the fix you recommend, his call
(`STUDIO.md` §2), then a targeted edit to the screen or component, then the new
score. Continue until every pass is at least 8 or he calls it good enough for a
pass, and record which.

## Step 4: Write `REVIEW.md`

The before and after scores per pass, the drift count, what changed, what he
accepted below 8 and why, and the open decisions with his answers. Set the
`design-review` row in `README.md`.

## Done when

- Drift is zero.
- All six passes have a score with "what a 10 looks like", before and after.
- Every pass is at 8 or above, or he accepted it lower on record.
- `REVIEW.md` is written and the open decisions are answered or listed.
