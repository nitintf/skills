# Review output format

How `/pr-review` and `/review` report findings. Both skills point here so the two
reviews read the same.

## What earns a finding

Report a finding only when the change actually hurts something:

- a security hole: injection, missing authz, secrets in code or logs, untrusted
  input (including LLM output) crossing a trust boundary unchecked
- data loss or corruption
- a broken feature or a wrong result, including edge cases real users will hit
- a broken API, schema, or event contract, or a migration with no rollback path
- a missing test for logic that could plausibly break
- a house-style divergence that causes real harm, such as a hand-rolled copy of an
  existing helper that will drift from it

Everything else (naming, formatting, small readability preferences, a pattern
that is merely different) is a minor point. Count minor points, do not write them
up.

## Shape of the review

1. **Verdict**: one line with the emoji and label the skill defines, plus one
   sentence on what the change does and how solid it is.
2. **What's good**: one line, only if something is genuinely worth reinforcing.
3. **One section per finding**, most severe first, numbered:

   ````markdown
   ### 1. <what goes wrong, in plain words> 🔴 blocking
   `path/to/file.ts:42`

   **Current code**
   ```ts
   <the exact lines from the diff, trimmed to what matters>
   ```

   **Suggested fix**
   ```ts
   <the replacement code>
   ```

   **Why:** <two or three plain sentences: the concrete scenario that breaks and
   what the user or system sees when it does>
   ````

   The tag is `🔴 blocking` (must fix before it lands) or `🟡 should fix` (real
   but does not gate the merge). When the fix is not a code swap (a missing test,
   a design question), replace **Suggested fix** with a sentence saying what to
   do.
4. **Open questions**: a short list of things only the author can answer.
   Omit when empty.
5. **Skipped**: one closing line, "Skipped N minor points, ask if you want
   them." Omit when N is zero. List them only if the user asks.

No findings is a valid review: the verdict line plus "Nothing blocking, ship it."
