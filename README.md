# Calm Pentatonic Ensemble (TunePad)

Code is split one file per cell so you can paste into TunePad and keep instruments consistent.

## What’s included
- `tunepad/01_drums.py` — soft kit with additive accents (3–3–2 / 2–3–2–3), light swing.
- `tunepad/02_bass.py` — gong–zhi support (1,2,3,5,6), four-beat bar shape.
- `tunepad/03_arp_pads.py` — guzheng-like 3–3–2 picking with pedal anchors.
- `tunepad/04_lead.py` — singable pentatonic melody with short grace notes.
- `tunepad/05_strings_stinger.py` — brief closing stinger.

## Quick start
1. Create five Code cells in a new TunePad project.
2. Set instruments in order: Drums, Bass, Keys (harp/pizz/soft), Lead (flute or soft square), Strings.
3. Paste each `tunepad/*.py` file into the matching cell.
4. Run cells top to bottom, then press Play. Use Mute and Solo to audition.
5. Export audio via Share → Download.

## Key things to tweak
- Project header: tempo, meter, key.
- Drums: `SWING`, `ROLL_P`, base velocities.
- Bass/Arp: `KEY`, `OCT`, pedal or degree plans.
- Lead: `DENSITY`, `SEED`, cadence targets.
- Stinger: `MAJOR = True` for a brighter end.

## Reliability notes
- Use a single numeric velocity per note (0–127).
- Let hats or arp advance time with positive durations; stack other hits at the same timestamp with `beats=0`.
- Keep arps monophonic; light layers help browser timing.

