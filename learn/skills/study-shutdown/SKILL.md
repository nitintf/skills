---
name: study-shutdown
description: Close today's study session. Logs what you solved and read, schedules problems to come back, moves your bookmarks, and turns what you learned into notes.
disable-model-invocation: true
argument-hint: "Optional: tell it what you did today"
---

# study-shutdown: record the day so tomorrow's plan is right

Turn a quick spoken account of the day into exact records: one result per
problem, a moved bookmark per source, and a log entry. **Tomorrow's `/study` is
only as good as tonight's results**, so every problem gets one of the six results
in [`LEARN.md`](../../LEARN.md) §4, and anything he struggled with is scheduled to
come back.

**Read `LEARN.md` first.** It defines the files, the results table and the
templates. This skill fills them in.

## Step 1: Load today

Resolve the paths (`LEARN.md` §1). Read today's `Learning Log.md` entry (its
`Plan:` line is the list to account for), the tracker, and the `reading` hub
notes. If there is no entry for today, `/study` did not run: build the record
from what he tells you anyway.

If `learning-repo` is set, read today's commits and changed files there
(`LEARN.md` §8), and match file names against problem IDs.

## Step 2: Ask, once

If he did not already say it with the command, ask in one message:

1. Which problems did you work on, and how did each go? Rough minutes are fine.
2. What did you read, where did you stop, and what did you learn?
3. Any system design today?

He will answer loosely ("did koko in 20 min, the matrix one I had to look at the
solution after an hour"). Map each problem to a result yourself. Ask a follow-up
only when a result is genuinely unclear, such as solved but unsure whether a hint
was used.

A planned problem he does not mention is `skipped`. One the repo shows he touched
but he did not mention: ask.

## Step 3: Write the tracker

For each problem, add a row to `## Problems` with today's date, the result,
the minutes, the new `Solo` count and `Next`, all per the results table. Then
check the current topic against the move-on rule and update `## Topics` and the
frontmatter if it moved on. A problem the bank does not hold (he picked one
himself) still gets a row, with its link in the `Problem` cell.

## Step 4: Move the bookmarks

For each source he read: set `bookmark` to where he stopped and `last-read` to
today. Tick each chapter he finished in the hub note's checklist. When he
finished the whole source, set `status: done` and say which `queued` source is
next.

## Step 5: Turn what he learned into notes

When he described something he learned, hand it to `/note` with the source and
the chapter. `/note` searches for an existing note and adds to it rather than
writing a duplicate, which is why this skill does not write notes itself.
Skip this step when he only said where he stopped.

## Step 6: Complete the log entry

Fill today's entry in `Learning Log.md` with the bullets in the `LEARN.md` §9
shape: one DSA line listing each problem with its result, minutes, and next date
when it comes back, then reading, system design and minutes. A system design
practice question also gets a row in `Practice.md`.

Then set the journal minutes (`LEARN.md` §7).

## Step 7: Commit on weekends

On weekdays the work `/shutdown` commits the vault, so leave it. On Saturday and
Sunday, commit and push the vault yourself: stage everything, write a message in
the repo's existing terse lowercase style (`2026-10-24 study`), and push. No
`Co-Authored-By`, and no model named anywhere in the message. If the push is
rejected, `git pull --rebase` once and push again. If that fails, stop and say so.

## Step 8: Tell him

Three lines: what got solved, what comes back and when, where each bookmark now
sits. If a problem has now come back three times or more, say so once.

## Done when

- Every problem from today's plan, and every one he mentioned, has a tracker row
  with one of the six results and a `Next` from the results table.
- Every source he read has a moved `bookmark` and today's `last-read`.
- Today's log entry has its bullets, and the journal minutes are set when the
  journal note exists.
- Anything he described learning went to `/note`.
- On a weekend, the vault is committed and pushed, or the reason it is not was
  said plainly.
