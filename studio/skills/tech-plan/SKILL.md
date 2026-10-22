---
name: tech-plan
description: Engineering and developer-experience review of the product plan. Picks the stack with reasons, designs the system and data model, fixes the folder structure and coding rules, wires the design tokens into code, and hands off to /scope.
disable-model-invocation: true
argument-hint: "Optional: a stack you already prefer"
---

# tech-plan: decide how it is built before anyone builds it

Make every structural decision the code will otherwise make by accident: the
stack, the architecture, the data model, the folder layout, the rules for writing
code, and how the design system becomes code. **Written as rules a coding agent
can follow and a reviewer can check**, because the `eng` skills treat this file
as binding.

Read [`STUDIO.md`](../../STUDIO.md) first. Read everything in `docs/product/`:
`IDEA.md` (scope, platforms, known gaps), `NICHE.md`, `DESIGN.md`, `tokens.json`,
the screen inventory in `design/screens/`, and `REVIEW.md`.

## Step 1: Requirements that drive the stack

From the files, list what the code must handle: platforms, offline use, sync,
accounts or none, data that must never be lost, notifications, payments,
widgets or lock screen surfaces, performance needs (a list of ten thousand
entries), privacy. Each one becomes a constraint on the choices below.

## Step 2: Choose the stack

One decision at a time (`STUDIO.md` §2), each with a recommendation, the real
alternative, and the cost of changing it later:

- App framework (for mobile his default is Expo and React Native with
  TypeScript; say plainly when a requirement argues for native instead).
- Navigation, state, local storage and sync, backend or none, auth.
- Styling: how components read the tokens.
- Testing: unit, component, and end to end, and what runs in CI.
- Build and release: EAS or equivalent, environments, crash reporting, analytics.

Use `pick-ui-library` when installed (`STUDIO.md` §9) for the UI pieces: charts,
number formatting, sheets, toasts, lists. For motion, name `animate-expo` (or
`animate` on the web) as the skill to build `DESIGN.md`'s motion with. Check each
library this session: current version, maintenance, and that it
supports the platforms. A library you only remember is labelled as unverified.

## Step 3: System design

- **Architecture**: the layers and how data flows from a tap to storage to the
  screen, as a diagram in text.
- **Data model**: every entity, its fields and types, relations, and how it
  changes over time (migrations from day one).
- **Failure handling**: for each known gap in `IDEA.md`, how the code handles it.
- **Scale and limits**: realistic numbers for this product, or "unknown", never
  invented benchmarks.

## Step 4: Code structure and rules

- The **folder layout**, every top-level folder with one line on what belongs
  there, and where a new screen, component, hook, store and test go.
- **Naming and file rules**: one component per file, co-located tests, and so on.
- **Patterns**: how screens get data, how errors are shown (using the empty and
  error states from the mockups), how forms validate.
- **The design rules for code**: tokens come from `src/theme/tokens.ts`, generated
  with `tokens.py --ts` (`STUDIO.md` §5); components are built once from
  `design/screens/components.html`; no raw colour, size or font anywhere, checked
  with `drift.py src/`.

## Step 5: Developer experience

How a fresh clone runs: the commands from clone to app on a phone, target under 10
minutes. Lint, format and type-check config, the pre-commit or CI check including
`drift.py`, and a short README outline.

## Step 6: Write it down and hand off

- **`ARCHITECTURE.md`**: Steps 1 to 5 as decisions and rules, with a decisions
  table (decision, alternatives, why).
- **The project `CLAUDE.md`**: create or extend it with a `## Product plan` block:
  read `docs/product/DESIGN.md` and `docs/product/ARCHITECTURE.md` before UI or
  structural work, take every design value from the tokens, put new code where
  the folder rules say, and flag drift instead of working around it.
- **First tickets**: the build order for the first version, one line each, from
  project scaffold to the last screen.

Set the `tech-plan` row in `README.md`. The next step is the `eng` pipeline:
`/scope` on the first ticket, which reads these files as binding.

## Done when

- Every choice in Step 2 is his decision, with the libraries checked this session.
- `ARCHITECTURE.md` has the architecture, data model, folder layout, code rules,
  design rules for code, and the run commands.
- The project `CLAUDE.md` carries the `## Product plan` block.
- The first tickets are listed in build order.
