---
name: launch-kit
description: Everything the product needs to be found and installed. App Store and Play Store listings with researched keywords, store screenshots designed from the mockups, a landing page, and a plan for the first hundred users.
disable-model-invocation: true
argument-hint: "Optional: listing, screenshots, landing or plan"
---

# launch-kit: make it findable, then make the first screen sell it

Turn the plan into what a stranger sees before installing: the store listings,
the screenshots, the landing page, and how the first users find it. **The store
page is the product's first screen**, so it carries the interface thesis exactly
like the app does, in the same tokens and voice.

Read [`STUDIO.md`](../../STUDIO.md) first. Read `IDEA.md` (who, the wedge, how
people find it), `NICHE.md` (competitors, complaints, thesis), `BRAND.md` (name,
voice, icon), `DESIGN.md` and `tokens.json`, and the screens in
`design/screens/`. An argument limits the run to one part.

## Step 1: Keywords

Find the words people search, from evidence gathered this session: competitor
titles and subtitles (the iTunes lookup used in `/niche`), the phrases
in their reviews, and web searches for the problem in plain words. Group them by
intent, and mark each as owned by the leaders or open. Pick the set for the
title, subtitle and keyword field, favouring open phrases that match the wedge.

## Step 2: Listings

For each store in `README.md`'s platforms, in the voice from `BRAND.md`:

| Field | Limit |
|---|---|
| App Store name | 30 characters |
| App Store subtitle | 30 characters |
| App Store keywords | 100 characters, comma separated, no repeats of the name |
| Promotional text | 170 characters |
| Description | Opens with the thesis in one line, then what it does, then why it is different, plainly |
| Play title / short description | 30 / 80 characters |

Count the characters. Use `eas-app-stores` when installed (`STUDIO.md` §9) for
where each field lives in `eas.json` and the store metadata files.

## Step 3: Store screenshots

Design 5 or 6 screenshots, first one strongest: each is a real screen from
`design/screens/` with one short caption that sells one benefit, in the brand's
type and colours. Build them as HTML at the store sizes (iPhone 6.9 inch,
1290 by 2796; Android phone, 1080 by 1920), render with `shots.sh` and look at
every one (`STUDIO.md` §6). They should read at thumbnail size in a search
result, next to the competitors' screenshots saved during `/niche`. Use
`canvas-design` for any feature graphic or poster-style frame when installed.

## Step 4: Landing page

One page in `launch/site/index.html`, in the brand's tokens: the thesis as the
headline, the app shown in its best screen, three reasons it is different, the
store badges, and a way to get notified before launch. This surface persuades,
so it can be bolder than the app: follow `impeccable` (its persuade mode) or
`frontend-design` when installed, then render at web sizes with
`shots.sh --web`, run the `impeccable` detector, and fix what it finds.

## Step 5: First hundred users

From `IDEA.md`'s "how people find it" and the communities in `NICHE.md`'s
research: where the person from `/idea` already spends time, what to post there
and when, who to ask for a first review, the launch day sequence (TestFlight
friends, then the store, then the communities), and the one number to watch in
week one. Concrete places and dates, not "use social media".

## Step 6: Write `LAUNCH.md`

The keyword research and chosen set, both listings with character counts, the
screenshot list with captions and file paths, the landing page path, the
first-hundred plan, and what he must do himself: developer accounts, privacy
policy URL, support email, domain set up from `BRAND.md`. Run the fresh-eyes
review (`STUDIO.md` §2), and set the `launch-kit` row in `README.md`.

Submitting builds, buying anything and posting publicly are his to do.

## Done when

- Every listing field is within its character limit, and its keywords come from
  evidence gathered this session.
- The store screenshots exist at store size, were rendered and looked at, and use
  only the tokens.
- The landing page was rendered at web sizes, and detector findings are fixed or
  justified when `impeccable` is installed.
- `LAUNCH.md` lists what he must do himself.
