import pyaudio
import wave
import random
import numpy as np
from scipy.io import wavfile

def pitchcorrect(smallsample, fractindex):
	if random.random() > fractindex:
		return smallsample[:-1] #temp
	else:
		return smallsample
		
def sqwave(sample):
	return np.array((sample > 0), dtype=bool)

def tremolo(sample, freq):
	length = (44100 / freq) / 2

	x = np.linspace(3 * np.pi / 2, 7 * np.pi / 2, length)
	sine = np.sin(x)
	sine += 1
	sine *= .5
	sine = sine.tolist()

	while len(sine) < len(sample):
		sine += sine
	sine = np.array(sine[0:len(sample)]).reshape(-1,1)
	sine_2d = np.concatenate((sine,sine), axis=1)
	return np.array(sample * sine_2d, dtype=np.int16)

def pan(sample, pan):
	panleft = 1 - pan
	panright = 1 + pan
	return sample * [panleft, panright]

def granulate(tone):
	# fill a rest as 0s
	if tone['note_freq'] == 0: 
		fullsample = [0] * (int(tone['length'] * 44100))
		fullsample = np.array(fullsample).reshape(-1,1)
		return np.concatenate((fullsample,fullsample), axis=1)
	
	# prepare data
	wf = wave.open(tone['sample'], 'rb') 
	sr, dat = wavfile.read(tone['sample'])
	samplelength = sr / tone['note_freq']
	smallsample = dat[:(int(samplelength)) + 1] 
	fractindex = samplelength - int(samplelength) # used to correct for non-integral frequency
	
	# convert to squarewave
	if True: 
		smallsample = sqwave(smallsample)

	# amplify and pan
	smallsample = smallsample * tone['volume'] 
	smallsample = pan(smallsample, tone['pan'])
	
	# construct the full sample, correcting for pitch
	fullsample = smallsample.tolist() 
	smallsample = smallsample.tolist()
	while len(fullsample) < sr * tone['length']:
		fullsample += pitchcorrect(smallsample, fractindex)
	fullsample = fullsample[0:int(sr * tone['length'])]
	fullsample = np.array(fullsample, dtype = np.int16)

	# tremolo
	if tone['tremolo'] != 0: 
		fullsample = tremolo(fullsample, tone['tremolo'])

	return fullsample