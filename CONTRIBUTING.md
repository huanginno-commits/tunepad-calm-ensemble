# Contributing

- Keep functions small; put tweakable params at the top of files.
- Respect TunePad constraints:
  - Only numeric velocities (0–127).
  - One note with positive `beats` advances time per grid step; stack others at `beats=0`.
- When changing musical behaviour, note what you changed (SWING, DENSITY, degree plan).
- Open a PR; attach a short clip if possible.
