moveTo(0)

import random
BARS, KEY, OCT, SEED, DENSITY = 8, 'A', 4, 11, 0.85
random.seed(SEED)

NOTE = {'C':0,'Cs':1,'Db':1,'D':2,'Ds':3,'Eb':3,'E':4,'F':5,'Fs':6,'Gb':6,'G':7,'Gs':8,'Ab':8,'A':9,'As':10,'Bb':10,'B':11}

def midi(n='A', o=4): 
    return 12*(o+1) + NOTE[n]

def pent_major(root):  
    return [root+i for i in (0,2,4,7,9)]

def deg(scale, d):     
    return scale[{1:0,2:1,3:2,5:3,6:4}[d]]

scale = pent_major(midi(KEY, OCT))
NEIGHBOURS = {1:[1,2,3,5], 2:[1,2,3,5], 3:[2,3,5,6], 5:[1,2,3,5,6], 6:[3,5,6,1]}
BAR_DYN = (-2, +2, +4, 0)

def main_note(prev_deg):
    return random.choice(NEIGHBOURS.get(prev_deg, [1,2,3,5,6]))

def grace_pair(target_deg):
    if target_deg in (1,2): 
        g = 1 if target_deg == 2 else 6
    elif target_deg in (5,6): 
        g = 6 if target_deg == 5 else 5
    else: 
        g = 2
    return g, target_deg

prev = 1
for bar in range(BARS):
    dyn = BAR_DYN[bar % 4]
    for step in range(8):
        strong = step in (0, 4)
        if random.random() < DENSITY or strong:
            d = main_note(prev)
            if strong:
                g, m = grace_pair(d)
                playNote(deg(scale, g), beats=0.25, velocity=62 + dyn)
                playNote(deg(scale, m), beats=0.25, velocity=70 + dyn)
            else:
                playNote(deg(scale, d), beats=0.5, velocity=66 + dyn)
            prev = d
        else:
            rest(0.5)
    cad = 1 if (bar % 4 in (1,3)) else 5
    playNote(deg(scale, cad), beats=0.25, velocity=68 + dyn)
    rest(0.25)
