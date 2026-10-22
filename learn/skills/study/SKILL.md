---
name: study
description: Plan today's study session, with DSA problems from your review queue and current topic, where you are in your book, and today's system design item.
disable-model-invocation: true
argument-hint: "Optional: light, or a topic to start"
---

# study: today's study plan, one screen

Tell him exactly what to work on today, so the hour goes on solving and reading
instead of deciding. **Every item comes from his own files**: a problem from the
bank, a bookmark from a hub note, a review the tracker scheduled. If a file does
not say it, the plan does not contain it.

**Read [`LEARN.md`](../../LEARN.md) first.** It defines the paths, the files, the
review schedule, the topic phases and the daily load. This skill applies it.

## Step 1: Load the state

Resolve the paths (`LEARN.md` §1), then read:

1. **`Learning Log.md`**, the last 30 days of entries. Note the last day anything
   was logged, and any day with a plan and no bullets (a missed night).
2. **`DSA Tracker.md`**: the current topic and its phase, and the review queue
   (every problem whose latest row has `Next` on or before today).
3. **`Problem Bank.md`**, the current topic's table.
4. **The reading hub notes** with `status: reading`, for each bookmark.

If yesterday's entry has a plan and no bullets, `/study-shutdown` did not run.
Say so in one line, and treat yesterday's problems as `skipped`: they come back
today.

## Step 2: Pick today's DSA

Apply the daily load for today's weekday (`LEARN.md` §4). If he said `light`,
use the light row.

1. **Unfinished first.** A `partial` or `skipped` problem from the last session
   leads the list.
2. **Due reviews**, oldest `Next` first, up to the cap. Say why each is back: "you
   read the solution on 21 Oct".
3. **New problems**: the next rows in the current topic's bank table that have no
   row in the tracker, in bank order.
4. **Topic transitions.** If the current topic meets the move-on rule, say so and
   start the next one in `learning`. On a `learning` day, name the concept to
   cover first: his existing note under `$LEARN/DSA/` if there is one (search for
   it), otherwise the topic to read up on. Then one easy problem.

Give each problem as a link with its difficulty and target time.

## Step 3: Pick reading and system design

- **Reading**: each `reading` source, with its bookmark: "Database Internals, from
  Ch 2, p. 41, 30 minutes". If nothing is `reading`, propose the first `queued`
  source in `Reading.md`, and say it is a proposal.
- **System design**: the concept reading on Monday, Wednesday and Friday, the
  practice question on Sunday (`LEARN.md` §6). On Sunday, propose one classic
  question he has not logged in `Practice.md`.

## Step 4: Show it

One screen:

```markdown
# Study, Friday 23 Oct

**DSA: 7. Binary Search (practising, 4 of 6, 2 mediums alone)**
- [ ] Review: [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) M, 25m. You read the solution on 21 Oct.
- [ ] New: [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) M, 25m
- [ ] New: [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) M, 25m

**Read**: Database Internals, from Ch 2, p. 41 (30m)
**System design**: DDIA, from Ch 1 (30m)
```

Add one line of context only when it changes what he does: three days without a
log, a topic about to finish, a review that keeps coming back.

## Step 5: Open today's log entry

Add today's heading and `Plan:` line to the top of `Learning Log.md`
(`LEARN.md` §9). If today's entry already exists, replace only its `Plan:` line,
and keep any bullets.

That is the only write. The tracker and the bookmarks change at night.

## Done when

- Today's plan has at least one DSA problem, and every problem is a bank row with
  its link.
- Every due review is in the plan or named as left out, with its reason for being
  back.
- Every `reading` source appears with its bookmark.
- Today's `Learning Log.md` entry exists with a `Plan:` line, and nothing else in
  the vault changed.
