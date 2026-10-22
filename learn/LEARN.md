# Study loop contract: what `/study` and `/study-shutdown` read and write

`/study` plans the day in the morning. `/study-shutdown` records it at night.
Tomorrow's `/study` builds on what the night wrote. Both skills follow this file,
and neither invents a file, a field, or a problem that is not described here.

**State lives in a few long-lived files, never in a note per day.** The log keeps
history, the tracker keeps DSA progress, and each source's own note keeps the
reading bookmark. Losing your place in a book is the failure this design exists
to stop.

---

## 1. Paths

Resolve `$VAULT` from `$OBSIDIAN_VAULT`, else the directory containing
`.obsidian/`, else ask. **Never write to a guessed path.**

Then read `$VAULT/99 Meta/Paths.md`, a two-column table of key and path. Paths
are relative to `$VAULT` unless they start with `~` or `/`.

| Key | Meaning | When missing |
|---|---|---|
| `learn` | `$LEARN`, the learning folder | `$VAULT/Learn` |
| `journal` | Personal journal folder, for the habit minutes (§7) | Skip §7 |
| `learning-repo` | Git repo where solutions are written, read for evidence (§8) | Skip §8 |

## 2. The files

| File | Owner | What it holds |
|---|---|---|
| `$LEARN/DSA/Problem Bank.md` | Nobody edits it during the loop | Every problem the skills may assign, by topic, in learning order |
| `$LEARN/DSA/DSA Tracker.md` | `/study-shutdown` writes, `/study` reads | Topic progress, every attempt, the review queue |
| `$LEARN/Learning Log.md` | `/study` opens today's entry, `/study-shutdown` completes it | One short entry per day, newest first |
| Each source's hub note | `/study-shutdown` moves the bookmark | Where you are in that book, paper or article (§5) |
| `$LEARN/System Design/Practice.md` | `/study-shutdown` appends | System design questions you have worked through |

If a file is missing on a run, create it from §9 and say so in chat.

## 3. The problem bank

A table per topic, `| ID | Problem | Diff | Sources | Link |`, under `## <n>. <Topic>`
headings in learning order, easy to hard within each topic. **Assign only rows
from this file, by ID, with its link.** A problem the bank does not hold is never
assigned, which is how every link stays real.

## 4. The DSA tracker

Frontmatter: `current-topic` (the bank heading, such as `7. Binary Search`) and
`topic-started` (a date).

**`## Topics`**: `| # | Topic | Status | Started | Done |`. Status is one of
`next`, `learning`, `practising`, `done`. Exactly one topic is `learning` or
`practising` at a time.

**`## Problems`**: one row per attempt, newest first.

`| Date | ID | Problem | Topic | Diff | Result | Min | Solo | Next |`

`Solo` counts solo solves since the last time the problem needed help. `Next` is
the date it comes back, or `done`. The review queue is every problem whose
latest row has a `Next` date on or before today.

### Results and when a problem comes back

`/study-shutdown` sets `Result` from what he says and `Next` from this table.
These are the only six results.

| Result | Meaning | Next | Solo becomes |
|---|---|---|---|
| `alone` | Solved without help within the target time | +14 days, or `done` if Solo reaches 2 | Solo + 1 |
| `slow` | Solved without help, over the target time | +3 days | Solo + 1 |
| `hint` | Needed a hint or a nudge | +2 days, then +7 on the next `hint` | 0 |
| `solution` | Read the solution, or never got there | +1 day after 60+ minutes of struggle, +2 days otherwise | 0 |
| `partial` | Started, not finished | Tomorrow, as the first problem | unchanged |
| `skipped` | Not attempted | Tomorrow, no penalty | unchanged |

Target time: E 15 min, M 25 min, H 40 min. A problem is finished only at `done`:
two solo solves in a row, the last one in time. Anything that needed help stays in
the queue, from a blank file each time, until then.

### Moving through topics

| Phase | What happens | Moves on when |
|---|---|---|
| `learning` | Day one of a topic. A concept first: the matching chapter or section, or his existing note in `$LEARN/DSA/`. Then at least one easy problem. | The concept is covered (usually one day) |
| `practising` | New problems from this topic in bank order, easy first, then medium, then hard | At least 6 attempted, at least 3 mediums `alone`, and one hard attempted |

When a topic is `done`, the next `next` topic becomes `learning`. Reviews from
older topics keep coming back on schedule.

### Daily load

| Day | DSA |
|---|---|
| Normal | Due reviews, oldest first, at most 2, then new problems to make 3 in total (always at least 1 new) |
| Light (he says so) | 1 problem: the oldest due review, else one new |
| Saturday | Revision: every problem due this week, plus every `hint` or `solution` from the last 7 days, from a blank file. No new problems unless the queue is empty. |
| Sunday | 1 problem, plus the weekly system design question (§6) |

**The minimum is one problem, every day.** Never plan zero.

## 5. Reading bookmarks

Every source the loop tracks has a hub note with this frontmatter:

```yaml
type: book | paper | article
track: reading | system-design
status: queued | reading | done
bookmark: "Ch 2, p. 41"      # where to start next time
last-read: 2026-10-23
```

At most one source per `type` and `track` is `reading` at a time. A book's hub
note keeps its chapter checklist, and `/study-shutdown` ticks a chapter when he
finishes it. The queue is the `queued` sources, in the order they appear in
`$LEARN/Reading/Reading.md`. When nothing is `reading`, `/study` proposes the
first queued one. Daily reading is time-boxed, 25 to 30 minutes, not a chapter
count.

Downloaded PDFs live outside the vault. The hub note links to the file path or
URL.

## 6. System design

Concept reading (the `reading` source on `track: system-design`, DDIA by default)
on Monday, Wednesday and Friday, 30 minutes. One practice question a week, on
Sunday by default, talked through out loud, logged in `Practice.md` as
`| Date | Question | Min | Notes |`.

## 7. Journal minutes

When `journal` is set and `<journal>/<YYYY-MM-DD> Journal.md` exists, set its
`Learning minutes` (DSA plus system design) and `Reading minutes` frontmatter
properties. Touch nothing else in that note, and never create it.

## 8. The solutions repo

When `learning-repo` is set and exists, `/study-shutdown` reads `git log --since`
midnight and `git status` there. A changed file whose name contains a problem's ID
is evidence that he worked on it. Evidence only: the skills never write to,
commit, or push this repo.

## 9. Templates

**`Learning Log.md`**: frontmatter `type: learning-log`, a one-line description,
then entries newest first:

```markdown
### 2026-10-23 Fri
Plan: review two-sum; new valid-anagram, group-anagrams. Read Database Internals from Ch 2. DDIA Ch 1.
- DSA: two-sum (alone, 12m); valid-anagram (hint, 30m, next 25 Oct)
- Read: Database Internals, Ch 2 p. 41 to 58 (30m)
- System design: DDIA Ch 1, reliability vs fault tolerance (30m)
- Minutes: learning 72, reading 30
```

`/study` writes the heading and the `Plan:` line. `/study-shutdown` adds the
bullets. An entry with only a plan is a day nothing was logged.

**`DSA Tracker.md`** and **`Practice.md`**: the frontmatter and tables in §4 and
§6, with no rows yet.
