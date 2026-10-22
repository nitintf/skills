---
name: idea
description: Office hours for a new product. Pressure-tests the idea with hard questions, challenges your assumptions, offers two or three approaches, and writes IDEA.md. Writes no code.
disable-model-invocation: true
argument-hint: "The idea, in a sentence or a ramble"
---

# idea: office hours before anything gets built

Find out whether the idea is worth building and what exactly the first version
is, then write it down. **The only output is `IDEA.md`.** No code, no scaffold,
no mockups: a product that is wrong in the doc is cheap, wrong in code is not.

Read [`STUDIO.md`](../../STUDIO.md) first: the file layout (§1), the question
format (§2) and the state file (§3).

## Step 1: Place the session

If the working directory already has `docs/product/IDEA.md`, offer to revise it
or start fresh. Otherwise this is a new product: ask for a working title, then
create `~/code/personal/<product-slug>/` with `git init` and `docs/product/`
(`STUDIO.md` §1), and work from there. If that folder already exists, stop and ask
before writing into it.

Ask one framing question: what is this for? A business he wants paying users for,
or something he is building for himself and to learn. The first gets the full
diagnostic in Step 2. The second gets the builder questions instead: what is the
coolest version, who would he show it to first, and what is the fastest path to
something he can share. Revenue or customers coming up later moves it to the full
diagnostic.

Also settle the platforms (iOS, Android, web) and write them in `README.md`.

## Step 2: The six questions

Ask **one at a time**. Push twice on a vague answer before moving on, and skip
any question his earlier answers already settled.

| # | Question | Push until you hear | Red flags |
|---|---|---|---|
| 1 | What is the strongest evidence that someone wants this? Not interested, not on a waitlist: genuinely upset if it disappeared tomorrow. | A named person or behaviour he has seen | "Everyone needs this", a survey, friends said it's cool |
| 2 | What do people do today to solve this, even badly? What does that cost them? | The real workaround: a spreadsheet, a notes app, nothing and the pain it causes | "Nothing, that's why it's a big opportunity" |
| 3 | Who needs this most? Describe one real person: their situation, what they are trying to do, what frustrates them. | One specific person, not a segment | "Millennials", "small businesses" |
| 4 | What is the smallest version someone would pay for, or use every day, this month? | A wedge that ships in weeks. Then push: what if they had to do nothing at all to get value, no setup, no login? | A platform, a list of ten features |
| 5 | Have you watched someone deal with this problem without helping them? What surprised you? | An observation | Only his own opinion |
| 6 | If the world is different in three years, does this matter more or less? | A reason tied to a real trend | "AI will change everything" with no mechanism |

After question 1, restate the idea in one sentence with any fuzzy word made
concrete ("seamless" becomes what actually happens), and name the one hidden
assumption it rests on.

**In a crowded category** (money trackers, habit apps, to-do lists, note apps),
say so plainly and change question 4 to: why would someone switch from the free
app they already use? Features rarely win here. Feel, speed and the interface
do, which is what `/niche` digs into next.

## Step 3: Premises

List the premises the idea stands on, numbered, each one testable:

```
PREMISES
1. People who track spending give up because logging takes too long. Agree?
2. ...
```

He agrees or disagrees with each. A disagreement changes the idea, not the
premise's wording: loop until every premise holds.

## Step 4: Approaches

Two or three ways to build the first version, always including:

- **Minimal**: the smallest thing that tests the riskiest premise.
- **Ideal**: the version he would build with no time limit.
- **Lateral** (when one exists): a different angle on the same problem.

Each with: summary, effort (S, M, L, XL), the biggest risk, what it gives up.
**Stop until he picks one.**

## Step 5: Write `IDEA.md`

Sections, in this order, one bullet per decision, empty sections omitted:

- **Problem**: one paragraph.
- **Evidence**: what he has actually seen.
- **Today's workaround** and its cost.
- **Who it is for**: the one person from question 3.
- **The wedge**: the first version, and what it deliberately leaves out.
- **Premises**: the agreed list.
- **Approaches**: all of them, the chosen one marked, each rejected one in a line.
- **Success**: what would prove it works in the first month, as numbers where
  possible.
- **How people find it**: the first 100 users, concretely.
- **Open questions**.
- **The assignment**: one real-world action before more planning, such as
  "watch two friends log a week of spending and note where they give up".
- **Scope**: left empty, `/founder-review` fills it.

Then have a fresh subagent read the doc cold and report blocking problems only:
a contradiction, a missing decision, a premise the approach ignores. Fix those,
then show him the whole doc in chat (tool output gets collapsed) and ask:
approve, revise, or start over.

Set the `idea` row and log the decisions in `README.md`.

## Done when

- Every premise is agreed, and one approach is chosen by him.
- `IDEA.md` has the sections above with no placeholders, and ends with one
  assignment.
- `README.md` shows `idea` done, with the platforms set.
- No code or project scaffold was written beyond the product folder, `git init` and
  `docs/product/`.
