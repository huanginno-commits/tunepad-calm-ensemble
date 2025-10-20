moveTo(0)

NOTE = {'C':0,'Cs':1,'Db':1,'D':2,'Ds':3,'Eb':3,'E':4,'F':5,'Fs':6,'Gb':6,'G':7,'Gs':8,'Ab':8,'A':9,'As':10,'Bb':10,'B':11}

def midi(n='A', o=4): 
    return 12*(o+1) + NOTE[n]

KEY, OCT, MAJOR = 'A', 4, False
ton = midi(KEY, OCT)
thr = midi('C', OCT) if not MAJOR else midi('Cs', OCT)
fif = midi('E', OCT)

playNote(ton, beats=0.5, velocity=80)
playNote([ton, fif], beats=0.5, velocity=78)
playNote([ton, thr, fif], beats=1.0, velocity=82)
