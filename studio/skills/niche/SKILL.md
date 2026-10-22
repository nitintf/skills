---
name: niche
description: Deep research into the product's category. Reads competitors, their store listings and their worst reviews, maps what every app does the same, and ends in an interface thesis for how yours should feel different.
disable-model-invocation: true
argument-hint: "Optional: competitors you already know"
---

# niche: find the angle a crowded category is missing

Research the category until there is a clear, evidenced answer to one question:
**how should this product look, feel and behave so that people choose it even
when its features match the free apps?** The answer is the interface thesis
(`STUDIO.md` §4), and every design step after this one is measured against it.

**Observed, not remembered.** Every claim about a competitor comes from a page
fetched in this session, with its URL. What you merely recall about an app is
labelled as recall, or left out.

Read [`STUDIO.md`](../../STUDIO.md) first. Read `IDEA.md` for the problem, the
person and the wedge.

## Step 1: Find the field

Search the stores and the web: "best <category> app <year>", App Store and Play
Store listings for the category, Product Hunt launches, "<category> app" on
Reddit. List 8 to 12 competitors, from the leaders to the small and loved ones.
Show the list and let him add or cut before going deep.

When the session can spawn subagents, research competitors in parallel, one
subagent per two or three apps, each returning the fields in Step 2 with URLs.

## Step 2: Read each competitor

For each one, from its store listing, site and screenshots:

- Who it is for, its price and model (free, freemium, subscription).
- Its core loop: what the user does every day, and how many taps it takes.
- Its look: type, colour, density, tone of copy, what the screenshots lead with.
- **What people complain about**: read its 1 to 3 star reviews on both stores and
  in Reddit threads. Quote the recurring complaints. These are the best evidence
  in the whole skill, because they are needs nobody is meeting.
- What people love: the 5-star reasons, quoted.

## Step 3: Synthesise in three layers

| Layer | Question |
|---|---|
| **Expected** | What does every app in the category do? Users will miss it if it is absent. |
| **Trending** | What are the newer apps doing that the old leaders are not? |
| **Missing** | What do the complaints and the gaps say nobody does well? |

Then a **sameness map**: the visual and interaction habits the category shares
(the same dashboard, the same pie chart, the same colours), so the design steps
know what to depart from on purpose.

## Step 4: The interface thesis

Propose two or three candidate theses, each one sentence plus evidence. For
example: "Logging a spend takes one gesture from the lock screen, and the app
feels like a calm paper notebook, not a bank dashboard. Evidence: 14 of the 40
complaints read are about logging friction, and every leader opens on a chart."

For each: what it would make the product feel like in the first five seconds,
which complaints it answers, and what it costs to build. Recommend one, and let
him choose or merge.

Also give the **feature gap list**: the features worth adding because complaints
ask for them, and the ones every app has that his wedge can safely leave out.

## Step 5: Write `NICHE.md`

Sections: competitors (a table with name, platform, price, core loop, look, link),
complaints (grouped, quoted, with counts and links), the three layers, the
sameness map, the feature gap list, and **the interface thesis** he chose, last
and prominent. Update `README.md`.

## Done when

- At least 8 competitors are covered, each claim with a URL fetched this session.
- Complaints are quoted from real reviews, grouped, and counted.
- `NICHE.md` ends in one interface thesis he chose, with its evidence.
- `README.md` shows `niche` done and logs the thesis as a decision.
