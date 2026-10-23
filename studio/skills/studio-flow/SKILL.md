---
name: studio-flow
description: Take a product from idea to a locked plan, running each studio step in order with your approval between them. Resumes wherever the last session stopped.
disable-model-invocation: true
argument-hint: "The idea, or nothing to resume"
---

# studio-flow: idea to buildable plan, one approved step at a time

Run the studio steps in order, stopping for his approval after each, so the
product arrives at code with the problem, niche, scope, brand, design and
architecture all decided. **The state lives in `docs/product/README.md`**, so the
flow resumes exactly where it stopped, across sessions.

Read [`STUDIO.md`](../../STUDIO.md) first.

## Step 1: Find where it stands

If the working directory has `docs/product/README.md`, read its step table and
resume at the first step that is not `done`, or that is `needs rework`. Otherwise
start a new product with `/idea`, which creates the folder. If he has no idea
yet, or several, run `/ideas` first.

## Step 2: Run the steps

In this order, each by following that skill's own `SKILL.md` in full:

| Step | Skill | Skip when |
|---|---|---|
| 1 | `/idea` | Never |
| 2 | `/niche` | Never for a product others will use; for a purely personal tool, he may skip it |
| 3 | `/founder-review` | Never |
| 4 | `/brand` | He already has a name and mark, or it is a personal tool |
| 5 | `/design-system` | Never when there is a UI |
| 6 | `/design-variants` | Never when there is a UI |
| 7 | `/mockups` | Never when there is a UI |
| 8 | `/design-review` | Never when there is a UI |
| 9 | `/tech-plan` | Never |
| 10 | `/launch-kit` | Until the first version is close to shipping; it can run later on its own |

Skipping a step is his decision: propose it with the reason, and record it in
the `README.md` log.

## Step 3: Gate between steps

After each step, show in a few lines what it decided and what the next step will
do, then ask: continue, revise this step, or stop here. Stopping is fine: the
README holds the state.

When a step changes an earlier decision (the design review reshapes scope, for
instance), mark the affected steps `needs rework` and offer to revisit them
before going on.

## Step 4: Finish

When `tech-plan` is done (and `launch-kit`, or its skip recorded), show the whole plan's summary: the thesis, the scope,
the name, the design direction, the stack, and the first tickets. The next step
is `/scope` on the first ticket.

## Done when

- Every step in the table is `done` or skipped with his reason on record.
- No step is marked `needs rework`.
- He has the summary and the first ticket to take into `/scope`.
