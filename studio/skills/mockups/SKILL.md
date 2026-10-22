---
name: mockups
description: Design every screen of the first version as HTML in the chosen direction, with every state, using only the design tokens, so building it is a matter of copying, not inventing.
disable-model-invocation: true
argument-hint: "Optional: one screen to (re)do"
---

# mockups: every screen, every state, one system

Turn the chosen direction into the complete set of screens for the first version.
**Every screen uses only `tokens.css`**, so screen ten looks like it belongs with
screen one, and the app built from these looks like them too.

Read [`STUDIO.md`](../../STUDIO.md) first: frames and content (§6), drift (§7).
Read `DESIGN.md`, `tokens.json`, `design/variants/DIRECTION.md`, and the scope in
`IDEA.md`. Missing direction: run `/design-variants` first.

## Step 1: The screen inventory

From the scope, list every screen and sheet the first version needs, in the order
a new user meets them: first launch and onboarding, permissions, the core loop,
settings, and the edges (empty, offline, error, paywall if any). For each: its
job in one line, what the user sees first, second and third, and its states.
Show the inventory and the navigation map (which screen leads where) and agree it
before drawing.

## Step 2: Shared parts first

Build the components every screen uses, from `DESIGN.md`'s component rules,
in one `design/screens/components.html`: navigation, header, list row, button
set, input, sheet, empty state, toast, and the domain parts (an amount, a
category chip, a chart). Screens reuse these, so a fix lands everywhere.

## Step 3: Build the screens

One file per screen, `design/screens/<NN>-<screen>.html`, in its frame:

- Every state from the inventory, shown side by side or behind a state switcher.
- Real content, including the awkward cases (`STUDIO.md` §6).
- Platform conventions for the target: safe areas, tab bar or navigation stack,
  native-feeling controls, 44 point touch targets.
- The interaction that matters on that screen works: the sheet opens, the entry
  logs, the signature moment from `DESIGN.md` plays.

Then `design/screens/index.html`: every screen as a thumbnail in flow order,
linking to each one, with the light and dark toggle.

## Step 4: Check drift as you go

Run `drift.py docs/product/design/` (`STUDIO.md` §7) after each batch of screens. Every hit is
fixed by using the token, or, when a new value is genuinely needed, by adding it
to `tokens.json`, regenerating `tokens.css`, and noting it in `DESIGN.md`'s
decisions table. Zero drift before handing over.

## Step 5: Walk him through

Open `index.html` and go through the flow with him screen by screen. Apply his
changes with targeted edits to the affected screens or components, never a
rewrite of a screen he has approved. Set the `mockups` row and log any design
decisions in `README.md`.

## Done when

- Every screen in the agreed inventory exists, with every listed state.
- `index.html` shows the whole flow in order.
- `drift.py docs/product/design/` reports zero values.
- He walked the flow and approved it.
