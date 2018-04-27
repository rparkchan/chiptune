import pyaudio
import wave
import sys
import time
import random
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from scipy.io import wavfile

import effects

def granulate(wavname, tonefreq, playlength, volume, sqwave, pan):	
	if tonefreq % 666.666 == 0: #test for rests
		fullsample = [0] * (int(playlength * 44100))
		fullsample = np.array(fullsample).reshape(-1,1)
		return np.concatenate((fullsample,fullsample), axis=1)
	
	wf = wave.open(wavname, 'rb') #open wav file and calculate sample length and times to play
	sr, dat = wavfile.read(wavname)

	samplelength = sr / tonefreq
	smallsample = dat[:(int(samplelength)) + 1] #temp
	fractindex = samplelength - int(samplelength)
	
	if sqwave: #turn to squarewaves
		smallsample = effects.sqwave(smallsample)

	smallsample = smallsample * volume #amplify
	smallsample = effects.pan(smallsample, pan)

	# x = np.linspace(0, 2 * np.pi, sr/vibfreq) #vibrato
	# vibber = np.sin(x)

	# fullsample = smallsample.tolist() #HAHHAHAHAHAHAHAH
	# while len(fullsample) < sr * playlength:
	# 	for i in range(20):
	# 		fullsample += dat[:(int(samplelength)) - 10].tolist()
	# 	for i in range(20):
	# 		fullsample += dat[:(int(samplelength))].tolist()
	# 	for i in range(20):
	# 		fullsample += dat[:(int(samplelength)) + 10].tolist()
	
	fullsample = smallsample.tolist() #construct fullsample in ratio for more exact frequency/pitch
	smallsample = smallsample.tolist()
	while len(fullsample) < sr * playlength:
		fullsample += effects.pitchcorrect(smallsample, fractindex)
	fullsample = fullsample[0:int(sr * playlength)]
	
	return np.array(fullsample, dtype = np.int16) #cut to length	

		






