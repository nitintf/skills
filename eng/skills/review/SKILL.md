---
name: review
description: >-
  Fast pre-commit review of your uncommitted working diff, in house style, before
  you commit. Reads staged + unstaged changes and new files, learns how the
  codebase already does things, and gives a high-signal gut-check: correctness,
  consistency with the codebase, obvious security/data issues, leftover debug/dead
  code, and missing tests, reporting only what would actually hurt. Standalone: does
  NOT touch `.plan` docs. Distinct from `/pr-review` (whole branch vs main, with
  GitHub context): this is the quick check on the working tree. Use right before
  committing. Triggers: "review my changes", "review the diff", "check this before
  I commit", "quick review", "review my working tree".
---

# review: a fast house-style check before you commit

This is the quick gut-check you run at the moment before `git commit`: *is what
I just wrote correct, and does it look like the rest of the codebase?* It's
lighter than `/pr-review` on purpose, no branch history, no `gh`, no exhaustive
audit. Fast and high-signal. For a full pre-merge review of a whole branch, point
the user at `/pr-review`.

## 1. Get the working diff

Review everything about to be committed, including brand-new files:

- `git status`, see the full picture (staged, unstaged, untracked).
- `git diff HEAD`: tracked changes (staged + unstaged) vs the last commit.
- `git diff --cached`: if you need to distinguish what's actually staged.
- **Read untracked new files directly**: they won't show in a diff but they're
  part of the change.

Read enough of the surrounding code to understand intent, not just the changed
lines: the bugs live where the new code meets the old.

## 2. Learn the house style (quickly)

**Read `.plan/_conventions.md` if it exists** (protocol in
`${CLAUDE_PLUGIN_ROOT}/SPEC.md` §6): on a fast pre-commit pass this is most of
the value, since it hands you the house style without any exploration. Check the
diff against it, especially the **existing primitives** table: a hand-rolled
helper that duplicates one already in the repo is the classic pre-commit catch.

Where the cache is silent, check how the codebase already does it before flagging
something as wrong. Find the existing pattern and cite `file:line`: API/handler
shape, component structure, error handling, logging, config access, naming, and
the existing **test style**. A change that diverges from house style is a finding
even if it "works".

## 3. Review: top-down, high-signal

This is a pre-commit pass, so move fast. Use these dimensions to find problems,
and the bar in `${CLAUDE_PLUGIN_ROOT}/REVIEW-FORMAT.md` to decide which ones get
written up:

1. **Correctness & edge cases**: does it do what you intended? Empty/null/
   boundary/malformed inputs, inverted conditions, off-by-ones, error paths that
   swallow failures.
2. **Consistency with the codebase**: reinvented helpers and divergences that
   will cause real harm. Cite the pattern to follow. A pattern that is merely
   different is a minor point.
3. **Obvious security / data safety**: injection, missing authz, secrets in
   code or logs, unvalidated input crossing a trust boundary (including LLM
   output). Only the clear stuff, this isn't a full audit.
4. **Leftovers**: stray debug logs, `console.log`/prints, commented-out blocks,
   TODOs you meant to resolve, dead code, a `.only` left on a test. These are
   cheap to catch now, so report them, but as one compact list (see §4), not a
   section each.
5. **Tests**: did the change need a test that isn't here? Do changed tests
   still prove something?

Skip the deep architecture and migration analysis `/pr-review` does, flag it
only if it's glaring. This pass is about catching what you'd be embarrassed to
commit, fast.

## 4. Deliver

Report in the shape defined by `${CLAUDE_PLUGIN_ROOT}/REVIEW-FORMAT.md`: verdict,
one section per finding with the current code, the suggested fix, and the reason,
then the skipped count. The verdict labels for this skill are ✅ good to commit,
🟡 commit after these, and 🔴 don't commit yet.

Leftovers go in a single `### Leftovers` section after the findings: one bullet
per item, `file:line` and what to remove, no code blocks.

Offer to apply the fixes. But committing is the user's call, you review, you
don't commit.

## Stay honest

- Don't pad. On a clean two-line change, "looks good, commit it" is the right
  review. Manufacturing findings wastes the user's time.
- If something's unclear, ask rather than guessing the intent.

## Done when

- The verdict line is first and matches the findings: don't commit yet if and
  only if at least one finding is `🔴 blocking`.
- Every finding has a `file:line`, the current code, a suggested fix (or a
  sentence saying what to do), and a **Why** naming the concrete failure.
- Leftovers sit in one list, and minor points appear only as the skipped count.
