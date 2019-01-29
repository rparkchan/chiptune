import pyaudio
import wave
import random
import numpy as np
from scipy.io import wavfile

# constants
VIB_PATCH = 4. # adjusts for length of fullsample
PYAUDIO_CORR =4 # PyAudio, 4 for stereo, 2 for mono

def tremolo(sample, freq):
	x = np.linspace(3 * np.pi / 2, 7 * np.pi / 2, (44100 / freq))
	sine = ((np.sin(x) + 1) * .5).tolist()
	while len(sine) < len(sample):
		sine += sine
	sine = np.array(sine[0:len(sample)]).reshape(-1,1)
	sine_2d = np.concatenate((sine,sine), axis=1)
	return np.array(sample * sine_2d, dtype=np.int16)

def granulate(tone):
	# fill a rest as 0s
	if tone['note_freq'] == 0: 
		fullsample = [0] * (int(tone['length'] * 44100 * PYAUDIO_CORR))
		fullsample = np.array(fullsample).reshape(-1,1)
		return np.concatenate((fullsample,fullsample), axis=1)
	
	# prepare data
	sr, dat = wavfile.read(tone['sample'])
	samplelength = sr / tone['note_freq']
	smallsample = dat[:(int(samplelength)) + 1] 
	fractindex = samplelength - int(samplelength) # used to correct for non-integral frequency
	
	# threshold cast to squarewave
	smallsample = np.array((smallsample > 0), dtype = bool)

	# amplify
	smallsample = smallsample * tone['volume'] 

	# pan
	smallsample *= [1-tone['pan'], 1+tone['pan']]
	
	# construct the full sample, allowing floating point frequencies via random sampling
	i = 0
	j = 0
	fullsample = []
	smallsample = smallsample.tolist()
	tnf = tone['note_freq']
	while len(fullsample) < sr * tone['length'] * PYAUDIO_CORR:
		# vibrato (consider "ramping up," like the cool chiptune stuff or a violin)
		# if len(fullsample) >= sr * tone['length'] / (2. * VIB_PATCH): # when to begin vib
		if(tone['vib'] != 0): 
			if i%int(tnf / tone['vib']) == 0: # speed (user-adjustable * fq-dependent)
				if (j+2)%8 < 4: # depth (user-adjustable * fq-dependent)
					smallsample += [[0,0]]
				else:
					del smallsample[-1]
				j += 1
			i += 1

		# concatenate
		ind = -1 if random.random() > fractindex else len(smallsample)
		fullsample += smallsample[:ind]
		
	fullsample = fullsample[0:int(sr * tone['length'] * PYAUDIO_CORR)]
	fullsample = np.array(fullsample, dtype = np.int16)

	# tremolo
	if tone['tremolo'] != 0: 
		fullsample = tremolo(fullsample, tone['tremolo'])

	return fullsample