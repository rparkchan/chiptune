from instrument import *

# construct dictionary mapping i.e. "A4" to 440
NOTES = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
FREQS = [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87]
notetofreq = {'r': 0}
for i,note in enumerate(NOTES):
	for j in range(20):
		notetofreq[note + str(j)] = FREQS[i] * pow(2,j)

# PyAudio constant, 4 for stereo, 2 for mono
PYAUDIO_CORR = 4

# input for tones
notelist = '440 r E5 Db4'.split(' ') # notes or numbers
lengthlist = [1.28] # in seconds
tremolofreq = [0, 0, 0, 0, 0] # in fq, repeating sequence
viblist = [50, 0, 25, 0] # 25 is appropriate
vollist = [1000] # 1000 is appropriate, repeating sequence
panlist = [0, 0, -1, 1] # 0 for mono, -1 for left, 1 for right, repeating sequence
samplelist = ['sounds/voice.wav']
freqlist = [float(note) if note.isdigit() else float(notetofreq[note]) for note in notelist]

# construct instrument
tonelist = []
for i in range(len(notelist)):
  tonelist.append({'note_freq' : freqlist[i],
                   'length' : lengthlist[i%len(lengthlist)] * PYAUDIO_CORR,
                   'tremolo' : tremolofreq[i%len(tremolofreq)],
                   'vib' : viblist[i%len(viblist)],
                   'volume' : vollist[i%len(vollist)],
                   'pan' : panlist[i%len(panlist)],
                   'sample' : samplelist[i%len(samplelist)]})
r = instrument(tonelist)

# playback upon enter
try:
  input("Press enter to play instrument!")
except SyntaxError:
  pass
r.play()