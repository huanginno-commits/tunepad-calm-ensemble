
moveTo(0)
from random import random
KICK, SNARE, HAT = 0, 2, 4

BARS = 8
SWING = 0.028
KICK_V, SNARE_V, HAT_V, ROLL_P = 82, 74, 48, 0.40

def v(x):
    x = int(x)
    return 0 if x < 0 else (127 if x > 127 else x)

ACCENT_PATTERNS = [(0, 6, 12), (0, 4, 10, 14), (0, 6, 10)]
BAR_DYN = (-6, 0, +4, -4)

for bar in range(BARS):
    heavy   = ACCENT_PATTERNS[bar % len(ACCENT_PATTERNS)]
    medium  = tuple(((h + 3) % 16) for h in heavy if ((h + 3) % 16) not in heavy)
    predrag = tuple((h - 1) % 16 for h in heavy)
    do_roll = (bar % 2 == 1) and (random() < ROLL_P)
    dyn     = BAR_DYN[bar % 4]
    pending_strong = False

    for s in range(16):
        dur = 0.25 + (SWING if (s % 2 == 0) else -SWING)

        # schedule simultaneous hits first (no time advance)
        if s in predrag:
            playNote(SNARE, beats=0, velocity=v(SNARE_V - 26 + dyn))
        if s in heavy:
            playNote(SNARE, beats=0, velocity=v(SNARE_V - 12 + dyn))
            pending_strong = True
        elif pending_strong:
            playNote(SNARE, beats=0, velocity=v(SNARE_V + 4 + dyn))
            pending_strong = False
        if s in medium:
            playNote(SNARE, beats=0, velocity=v(SNARE_V - 6 + dyn))
        if do_roll and s in (13, 14, 15):
            playNote(SNARE, beats=0, velocity=v(60 + (s - 13) * 12 + dyn))
        if s in (0, 8):
            playNote(KICK, beats=0, velocity=v(KICK_V - 2 + dyn))
        if s in predrag and s != 5:
            playNote(KICK, beats=0, velocity=v(KICK_V - 46 + dyn))
        if s == 5:
            playNote(KICK, beats=0, velocity=v(KICK_V - 42 + dyn))

        # hats advance time (visible grid)
        if s % 2 == 0:
            hat_boost = 12 if s in heavy else 0
            hat_dip   = -8 if s in predrag else 0
            playNote(HAT, beats=dur, velocity=v(HAT_V + dyn + hat_boost + hat_dip))
        else:
            rest(dur)
