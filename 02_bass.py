moveTo(0)

BARS, KEY, OCT = 8, 'A', 2
NOTE = {'C':0,'Cs':1,'Db':1,'D':2,'Ds':3,'Eb':3,'E':4,'F':5,'Fs':6,'Gb':6,'G':7,'Gs':8,'Ab':8,'A':9,'As':10,'Bb':10,'B':11}

def midi(n='A', o=2): 
    return 12*(o+1) + NOTE[n]

def pent_major(root):  
    return [root+i for i in (0,2,4,7,9)]

def deg(scale, d):     
    return scale[{1:0,2:1,3:2,5:3,6:4}[d]]

root  = midi(KEY, OCT)
scale = pent_major(root)
BAR_DYN = (-4, 0, +4, -2)

roots = [deg(scale,1), deg(scale,1), deg(scale,6), deg(scale,1)]
plan  = (roots * ((BARS+3)//4))[:BARS]

for i, r in enumerate(plan):
    dyn = BAR_DYN[i % 4]
    playNote(r,            beats=1.0, velocity=66 + dyn)
    playNote(deg(scale,2), beats=0.5, velocity=60 + dyn)
    playNote(deg(scale,3), beats=0.5, velocity=62 + dyn)
    playNote(deg(scale,5), beats=1.0, velocity=64 + dyn)
    playNote(deg(scale,6), beats=0.5, velocity=61 + dyn)
    playNote(r,            beats=0.5, velocity=66 + dyn)
