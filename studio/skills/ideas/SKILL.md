---
name: ideas
description: Find the product worth building. A conversation that mines your own problems and edge, generates ideas from several angles, checks each against real evidence, scores them, and hands the winner to /idea.
disable-model-invocation: true
argument-hint: "Optional: what you want from the product, or ideas you already have"
---

# ideas: from "I want to build something" to one idea worth a session

Help him choose what to build, by talking it through, not by handing him a list.
**The best first idea is one he would use himself every week**, that ships in
weeks next to a day job, and that has a real reason to beat what already exists.
Everything here serves finding that one.

Read [`STUDIO.md`](../../STUDIO.md) first: the question format (§2), independent
voices (§2), the taste file (§10). The ideas list is the `ideas` row of
`$VAULT/99 Meta/Paths.md` (`$VAULT` from `$OBSIDIAN_VAULT`); when it is missing,
ask where to keep it.

## Step 1: What the product is for

Read the ideas list and `~/.claude/studio-taste.md`. Then ask, one at a time:

1. **Why build this one?** To learn mobile properly, to ship something real, to
   earn on the side, to have a portfolio piece, or because something annoys him.
   The answer sets the weights in Step 5.
2. **How much time, honestly?** Hours a week, and for how many weeks before he
   wants it in the store.
3. **Platforms**: iOS, Android, or both, and which phone he carries.

## Step 2: Mine his life for problems

The strongest first ideas come from his own days. Ask, one at a time, and dig
into anything with feeling behind it:

- What did you do on your phone this week that annoyed you, or took more taps
  than it should?
- What do you track in a spreadsheet, a notes app, a chat with yourself, or not
  at all and wish you did?
- What do friends, family or colleagues complain about that an app could fix?
- What do you do at work again and again that feels like it should be a tool?
- Which apps do you open every day, and what would you change in each?

Then name **his edge**, from his answers and what he already knows: his stack, his
domain (energy and device data at AMPD, for instance), his country and the needs
it has that global apps ignore, the communities he belongs to. An idea where he
has an edge beats a bigger idea where he has none.

## Step 3: Generate from several angles

Produce 12 to 15 ideas, at least two from each angle:

| Angle | The question |
|---|---|
| **Own itch** | What from Step 2 would he use himself, every week? |
| **Better interface, crowded category** | Which category has free apps that all feel the same, where feel alone could win? |
| **New platform capability** | What do widgets, Live Activities, App Intents, on-device AI or the share sheet make possible that apps have not caught up with? |
| **Local and underserved** | What do people around him need that global apps do badly or ignore? |
| **Small community** | Which group he knows has no good app of its own? |
| **His edge** | What can he build that few others could, from his domain or skills? |

Use independent voices (`STUDIO.md` §2): brief two subagents with his answers from
Steps 1 and 2, not your list, and merge their ideas in, credited. Each idea is one
line: what it is, for whom, and why now.

Show the list grouped by angle. He reacts: kill what does not excite him, add
his own, star the ones he likes. **Taste first, analysis second**: an idea he does
not care about will not survive the months it takes to build.

## Step 4: Check the shortlist against reality

For each starred idea, at most six, gather evidence this session:

- **Who already does it**: App Store search (`curl -s "https://itunes.apple.com/search?term=<words>&entity=software&limit=10"`
  for names, ratings, review counts) and a web search for Android and the web.
- **What users of those apps complain about**: their 1 to 3 star reviews, quoted.
- **Demand signals**: Reddit threads, forum posts, searches where people ask for
  it or describe the workaround.

Label anything you only recall as recall. An idea with no competitors and no one
asking for it is a warning, not an opportunity: say which it looks like.

## Step 5: Score and discuss

Score each shortlisted idea from 1 to 5 on these, weighted by his answer to
Step 1 (for a first app, use and shippability count double):

| Criterion | 5 means |
|---|---|
| **He would use it** | Every week, starting the day it works |
| **Shippable** | A useful first version in 4 to 8 weeks at his real hours |
| **Evidence** | Real people complain about the gap, with quotes |
| **Edge** | He knows something or has access others lack |
| **Room to be different** | The interface or approach can clearly beat what exists |
| **Learning** | Teaches what he wants to learn (native feel, sync, notifications) |
| **Money** (when it matters to him) | A clear path to someone paying |

Show the table, then **argue**: for the top two, the strongest case for and the
strongest case against, plainly. Ask him which he would be sad not to build. He
picks one, and one backup.

## Step 6: Record and hand off

Update the ideas list: every idea from this session with its angle and one line,
the scored shortlist with evidence links, and the pick and backup marked with
today's date. Append the angles and kinds of idea he loved or killed to the taste
file (`STUDIO.md` §10).

Then hand off: give him the one-paragraph brief for the winner (what it is, for
whom, the evidence, his edge) and the command to start it, `/studio-flow` with
that brief, which creates the product folder.

## Done when

- His reasons, time and platforms are known, and his edge is named.
- At least 12 ideas across the six angles were shown, and he reacted to them.
- Every shortlisted idea has evidence gathered this session, with links.
- He chose one idea and a backup, and the ideas list records the session.
