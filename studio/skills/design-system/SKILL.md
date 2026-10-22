---
name: design-system
description: Design consultation. Turns the interface thesis into a complete, distinctive design system (type, colour, spacing, shape, motion), previews it as HTML, and locks it in DESIGN.md and tokens.json so every screen matches.
disable-model-invocation: true
argument-hint: "Optional: a direction or reference you like"
---

# design-system: one system, decided once, used everywhere

Propose a complete design system that makes the interface thesis visible, preview
it, and lock it. **Distinctive on purpose**: in a crowded category the look is a
reason to switch, so "clean and modern" is a failure, not a safe choice. And
**locked**: after this, every screen uses only `tokens.json`.

Read [`STUDIO.md`](../../STUDIO.md) first, especially tokens (§5) and mockups
(§6). Read `IDEA.md`, `NICHE.md` (the thesis and the sameness map) and `BRAND.md`
(voice, icon colours) when present. If `DESIGN.md` exists, offer to update it or
start fresh.

## Step 1: The anchor question

Ask: **what is the one thing someone should remember after using this for the
first time?** Every choice below must serve that answer and the thesis. Restate
both in one line before proposing anything.

## Step 2: Look at the field

Use the competitors in `NICHE.md`: open their store screenshots and sites
(fetched this session), and note their type, palette, density and shape. Add 3
to 5 references from outside the category that carry the feel the thesis wants
(a paper notebook, a camera app, a well-designed transit app). Name what to
borrow from each, and what the category does that this product will
deliberately not do (the sameness map).

## Step 3: Propose the system

Decide in this order, each choice with a one-line reason tied to the anchor:

1. **Mode and scene.** Where and when is it used (on a bus at night, at a desk
   on payday)? Light or dark first follows the scene, never the category.
2. **Aesthetic direction**: one named direction (calm editorial, warm tactile,
   precise instrument, playful, and so on), and its decoration level: minimal,
   intentional, or expressive.
3. **Typography by procedure, not by favourite.** For each role (display, body,
   numbers or mono), shortlist three faces that fit the audience's world, then
   verify each on Google Fonts or Fontshare this session: exact name, weights,
   licence, URL. Avoid the faces every app already uses as display (Inter,
   Roboto, Poppins, Montserrat, SF Pro as a statement face, Space Grotesk, DM
   Sans). Numbers matter in most apps: choose a face with good tabular figures.
   Then a type scale: display, title, body, label, number, with size, line height,
   weight and tracking.
4. **Colour strategy**: restrained (one accent), committed (one hue owns the
   product), or full palette. Every colour by role: bg, surface, text,
   text-muted, primary, on-primary, border, positive, negative, warning, plus
   any domain roles (chart series, categories). Light and dark. Check contrast:
   body text at least 4.5:1, large text 3:1.
5. **Space and shape**: a base unit and the scale, density, radius scale (an
   inner radius is the outer radius minus the gap), borders versus shadows.
6. **Motion and feel**: durations, easing, the **one signature moment** (what
   happens when a spend is logged, for instance), and haptics on mobile. When
   installed, follow `apple-design` for springs, gestures and sheets, and hold
   the components to the `emil-design-eng` polish bar (`STUDIO.md` §9).

Then split it out loud:

- **Safe choices** (2 or 3): where it matches what users of the category expect,
  and why that is right.
- **Risks** (at least 2): deliberate departures from the category, each with
  what it is, why it fits the thesis, what it gains, and what it costs.

Before showing it, check it against the generic looks AI lands in by default:
cream with a serif and terracotta; near-black with neon and glow; purple
gradients; a card grid of icons in coloured circles; everything centred. If the
proposal is one of those and the thesis did not ask for it, start again.

## Step 4: Preview

Write `tokens.json` (draft), generate `tokens.css` (`STUDIO.md` §5), and build
`design/system.html`: the type scale with real product content, every colour
role as a named swatch with its contrast ratio, buttons, inputs, list rows and
an empty state in every state (default, pressed, disabled, error), and two or
three realistic screens of this product in its frame (`STUDIO.md` §6), with a
light and dark toggle. Open it.

He reacts. Change the tokens, regenerate, reload, until he approves. A request
that breaks the anchor or the thesis gets one sentence saying so, then his call.

## Step 5: Lock it

- **`tokens.json`**: final, and `tokens.css` regenerated from it.
- **`DESIGN.md`**: the anchor and thesis; mode and scene; aesthetic; type with
  roles and verified sources; colour strategy and roles; space and shape; motion
  and the signature moment; components (button, input, list row, card, sheet,
  navigation) described by the tokens they use; **Do and Don't** as checkable
  rules ("numbers always in the number style", "never more than one primary
  button on a screen"); the safe choices and risks; a decisions table.

Log the decisions and set the `design-system` row in `README.md`. If later steps
were done, mark them `needs rework`.

## Done when

- He approved the system from the rendered preview, not from a description.
- `tokens.json` has every group from `STUDIO.md` §5, and `tokens.css` is generated
  from it.
- Every font in it was verified with a source URL this session.
- `DESIGN.md` covers the sections above, with at least two risks and checkable
  Do and Don't rules.
