# news-image-20261118 — 18 November 2026 in one image

One original image summing up the world news of **Wednesday 18 November
2026**, drawn as a newspaper front page (HTML + headless-Chromium render;
`poster.html` is the source that produced `entry.png`).

## Stories covered

1. **APEC, Shenzhen** — Xi Jinping and Vladimir Putin meet; Donald Trump
   lands for the first-ever three-way summit the next day.
2. **Gulf** — Iran says its drones struck US sites in Kuwait and Bahrain
   after the US hit Qeshm Island in the Strait of Hormuz.
3. **US Senate** — Democrat Mary Peltola wins Alaska, giving Democrats a
   projected 56–44 majority.
4. **Health** — The US loses its measles-free status after a year of
   continuous spread.
5. **Tech** — Nvidia beats forecasts: $115.8B revenue, +103% year over
   year, in its first results since Jensen Huang's exit.
6. **Also:** Israel opens a new operation in three areas of central Gaza;
   Cyclone Akvan nears India's Odisha coast.

All stories were verified against reporting dated 18 November 2026
(AP, Reuters, AFP, BBC, PAHO and others via same-day briefs). Nothing
shown happened before 13 November 2026.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
repository's `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. The copy is
byte-for-byte, so repeated runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verification (local, 19 Nov 2026)

- `entry.png`: 1024×1024 PNG, 186,539 bytes (limit: 1 MiB, 1024×1024).
- `main.py` run twice into two different output dirs: outputs
  byte-identical (`sha256sum` match).
- Image inspected visually: date prominent, all seven stories legible,
  no garbled text, no text clipped by tile borders.
