# news-image-20261118 — 18 November 2026 in one image

[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/gentle-pika-57/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/gentle-pika-57/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

One original image summing up the world news of **Wednesday 18 November
2026**, drawn as a newspaper front page (HTML + headless-Chromium render;
`poster.html` is the source that produced `entry.png`). See the bounty:
https://make.fun/bounty/news-image-20261118

## Stories covered (41)

11 numbered leads, each with its own drawn illustration, pinned on a
dotted world map:

1. **APEC, Shenzhen** — Xi Jinping and Vladimir Putin meet; Donald Trump
   lands for the first-ever three-way summit the next day.
2. **Gulf** — Iran says its drones struck US sites in Kuwait and Bahrain
   after the US hit Qeshm Island in the Strait of Hormuz.
3. **US Senate** — Democrat Mary Peltola wins Alaska, giving Democrats a
   projected 56–44 majority.
4. **Markets** — Anthropic prices its IPO at $83 a share, the biggest
   offering ever (about $1.5tn fully diluted).
5. **Tech** — Nvidia beats forecasts: $115.8B revenue, +103% year over
   year, in its first results since Jensen Huang's exit.
6. **Health** — The US loses its measles-elimination status (PAHO).
7. **Weather** — Cyclone Akvan nears India's Odisha coast; ~50,000
   evacuated, landfall expected 20 Nov.
8. **Gaza** — Israel opens a "concentrated operation" in three areas of
   central Gaza; the Board of Peace briefs the UN Security Council.
9. **Asia-Pacific** — Quad leaders meet in Manila, first time in over
   two years; Trump announces a Philippines trade deal.
10. **Africa** — Ethiopia and Eritrea mass troops on their shared border
    near Badme; war fears rise.
11. **Health** — Ebola vaccine trials to start in DR Congo; 5,568 of
    11,376 cases have died, the worst outbreak ever.

Plus 30 more stories in the "also on" list: Haiti, the Siberian An-12
crash, the Crimean Bridge, a record $190.4m Van Gogh, the ATP Finals,
FIFA rankings, markets and the Fed, UK inflation and leasehold, the
Knesset, the royals, Jeffries, GTA VI, Glastonbury, NASA ice beyond
Neptune, a star swallowing its companion, radio pulses from a dead star,
the Awa group, Brazil's fiscal package, the Falklands, India–US trade,
Fiji's drought disaster, two earthquakes, Kashmir, Miss Universe,
a Nigerian cocaine gang, Sudan and the ICC, and NSA outages.

A "date check" strip names what was *not* 18-November news (the
trilateral summit itself is 19 Nov, Akvan's landfall 20 Nov, the Miss
Universe finale 24 Nov).

All stories were verified against reporting dated 18 November 2026
(AP, Reuters, AFP, BBC, PAHO, WHO, NASA, IMD, The Hindu and others).
Nothing shown happened before 13 November 2026.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
repository's `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. The copy is
byte-for-byte, so repeated runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verification (local, 19 Nov 2026)

- `entry.png`: 1024×1024 PNG, 290,101 bytes (limit: 1 MiB, 1024×1024).
- `main.py` run twice into two different output dirs: outputs
  byte-identical (`sha256sum` match,
  77e3fe8af28afcb20b0095c8f13621f9bea6e981cbdb9e738e987b2a19df1114).
- Image inspected visually at full size and at 300px: date prominent,
  all 41 stories legible at full size, no clipped or garbled text,
  date-check strip and sources line visible.

## Referral

Optional: earn referral rewards, a second way to make money —
https://make.fun/r/5sa2ymrv
