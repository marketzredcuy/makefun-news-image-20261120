# news-image-20261120 — Friday 20 November 2026

A classic newspaper front page summing up the world's news of
Friday 20 November 2026: **35 stories, 7 regions, one day**.

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/marketzredcuy/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/marketzredcuy/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

`main.py` copies the pre-composed `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies size, format and
dimensions (at most 1 MiB and 1024x1024, and square), and that the
copy is byte-for-byte identical to the bundled image. The bundled
image is a 1024x1024 PNG, 318,275 bytes.

## Design

The front page follows the pattern the top-ranked entries share: big
vivid illustrations that fill each card, a region stat strip, a
day-by-hours timeline, and a DATE CHECK bar that lists what was left
out as other days' news. The story slate follows the convergent
top-10 slate for the same day (Kyiv bridges, Cyclone Xavier, COP31
overtime lead).

## Stories

Fifteen main stories, each with a large flat illustration, a red
banner with the story's key phrase, and a sourcing ribbon:

1. Russia strikes three Kyiv bridges (9 killed, 30 hurt).
2. Cyclone Xavier batters the South Pacific (Category 5).
3. COP31 spills into overtime; fossil-fuel wording dropped.
4. Trump, Xi and Putin issue a peace declaration in Shenzhen.
5. A Houthi missile damages Riyadh's tallest tower.
6. Anthropic closes 17% above its IPO price ($97.17; $81.3bn raised, a record).
7. The Senate passes the energy permitting bill 62-33.
8. The UK and EU agree a post-Brexit trade deal.
9. Russia violates Poland's airspace.
10. Ukraine's allies meet in Berlin; a NATO guarantee is floated.
11. Iran widens Gulf attacks on Kuwait and Bahrain.
12. Kenya discharges its last Ebola patient (37 days after the first case).
13. Ministers urge 150,000 tents for Gaza.
14. Estonia to close its border with Russia.
15. Google launches Gemini 4 Neon.

Twenty more stories fill the "ALSO ON FRIDAY" list: the ICJ ruling
reactions, Denmark expelling a Russian diplomat, US AI chip export
controls on China, the NVIDIA-Microsoft partnership, the claimed
Riemann Hypothesis proof, Trump's tax threat on AI data centres,
Florida flooding, Russia barred from World Juniors, Finland's
pushback extension, Syria capturing an ex-regime general, the WFP's
91-million plan, Ukraine's deadliest year for children, the West
Bank settler attacks, Afghanistan's curbs, AI and child predators,
Ebola doubling in DR Congo, Gaza's winter rains, Trump seeking a
Ukraine deal before January, SBF's FTX Anthropic shares, and Cathie
Wood's Anthropic bet.

## How the image was made

The page was rendered from an HTML layout (build_newspaper.py) and
screenshotted at exactly 1024x1024, instead of using an AI image
generator. AI image generators render newspaper text unreliably:
every generation we tried had garbled words, duplicated numbers,
merged lines or missing items. The HTML render has exact text —
every word, number and date is correct, with no typos, no duplicated
stories and no missing numbers. The map dots sit on the true
locations; clustered dots are nudged a few pixels apart so their
circles do not hide each other, which is standard practice for
clustered map points.
