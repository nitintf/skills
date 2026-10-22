---
name: founder-review
description: Founder's review of the plan's scope. Pick expand, selective, hold or cut, then decide every feature one by one so nothing enters or leaves the first version silently.
disable-model-invocation: true
argument-hint: "Optional: expand, selective, hold or cut"
---

# founder-review: settle what the first version contains

Look at the idea the way a founder with limited time and a strong opinion would:
is this the right thing, is it ambitious enough, and what must go so it ships?
**Every feature gets an explicit add, defer or skip from him.** Nothing changes
scope without a decision on record.

Read [`STUDIO.md`](../../STUDIO.md) first, especially the question format (§2).
Read `IDEA.md` and, when present, `NICHE.md`.

## Step 1: Challenge the premise

Before scope, three questions, answered in your own words with a recommendation:

- Is this the right problem, or a symptom of a bigger one?
- What happens if he builds nothing? Who is worse off?
- Does the interface thesis (if `NICHE.md` exists) actually change why someone
  would switch, or is it decoration?

If any answer undermines `IDEA.md`, say so first and offer to go back to `/idea`.

Then the **12-month picture**: what does this product look like a year from now if
it works, and does the first version head straight there or into a dead end?
Name anything in the wedge that would have to be thrown away.

## Step 2: Choose the mode

| Mode | Use when | Posture |
|---|---|---|
| **Expand** | The idea is timid for the opportunity | Propose the bigger version and the additions that make it remarkable |
| **Selective** | The core is right, a few additions earn their place | Keep the core, propose a short list of additions, each justified |
| **Hold** | Scope is right | Pressure-test it and make it complete, add nothing |
| **Cut** | The first version will not ship in weeks | Find the smallest version that still tests the riskiest premise |

Recommend a mode from the wedge's size and his time (a solo builder with a day
job rarely needs Expand for a first version). He picks.

## Step 3: Decide every item

Build the list: everything in `IDEA.md`, the feature gap list from `NICHE.md`,
and anything the chosen mode proposes. Then ask about **one item at a time**:
add, defer, or skip, with your recommendation, the effort, and what the user
loses without it. Group trivial items only when he asks to move faster.

## Step 4: Check what the scope leaves broken

For the scope he settled, walk the first-run and daily journeys and list what
could go wrong: no data yet, a failed sync, lost connection, a wrong entry to
undo, a permission refused. Each one is either handled in scope or written down
as a known gap. A failure that is unhandled, untested and silent is not allowed
to stay unnamed.

Before writing, brief one subagent as a skeptical user of a competitor's app, with
`IDEA.md`, `NICHE.md` and the scope so far, and ask: what would make you switch,
and what in this scope would you never use? Show its answer next to the scope,
and let him adjust.

## Step 5: Write the Scope section

In `IDEA.md` under `## Scope`:

- **Mode**: the one he chose, and why.
- **In the first version**: each feature, one line, in build order.
- **Later**: deferred items, each with what would bring it back.
- **Not doing**: skipped items, each with the reason.
- **Known gaps**: from Step 4.

Log each decision in `README.md` and set the `founder-review` row. If scope
changed something `NICHE.md` or a later file assumed, mark that step
`needs rework`.

## Done when

- He chose the mode, and every item has his add, defer or skip.
- `IDEA.md` has a complete `## Scope` section with the four lists and the gaps.
- Every decision is in the `README.md` log.
