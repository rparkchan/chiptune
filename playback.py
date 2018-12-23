from instrument import *

# PyAudio quirky constant, 4 for stereo, 2 for mono
PYAUDIO_CORR = 4

# input for tones
notelist = 'E4 r 440 r Db5'.split(' ') #notes or numbers
lengthlist = [1] #in seconds=
tremolofreq = [0, 0, 4, 0, 0] #in fq, repeating sequence
vollist = [1000] #value of 1000 is appropriate, repeating sequence
panlist = [0, 1, -1] #value of 0 for mono, -1 for left, 1 for right, repeating sequence
samplelist = ['sounds/ct.wav']

# construct instrument
tonelist = []
for i in range(len(notelist)):
  note = notelist[i%len(notelist)]
  note_freq = notetofreq[note] if not note.isdigit() else note
  note_freq = float(note_freq)
  tonelist.append({'note_freq' : note_freq,
                   'length' : lengthlist[i%len(lengthlist)] * PYAUDIO_CORR,
                   'tremolo' : tremolofreq[i%len(tremolofreq)],
                   'volume' : vollist[i%len(vollist)],
                   'pan' : panlist[i%len(panlist)],
                   'sample' : samplelist[i%len(samplelist)]})
r = instrument(tonelist)

# voice.wav has really grainy unsquared, really clean squared up to 6th octave
# dm.wav unsquared is too rough, pretty saw squared
# intoyou.wav unsquared is unusable, squared lower register is gnarly
# ct.wav unsquared is piercing, same with squared
# star.wav has rough unsquared, but super super fat squared