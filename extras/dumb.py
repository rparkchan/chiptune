import pyaudio
import wave
import sys
import time
import random
import effects
import numpy as np
import matplotlib.pyplot as plt
from Tkinter import *
from scipy.io import wavfile

# dictionary from str to float
notetofreq = {'A': 55.00, 'Bb': 58.27, 'B': 61.74, 'C': 65.41, 
	'Db': 69.30, 'D': 73.42, 'Eb': 77.78, 'E': 82.41, 
	'F': 87.31, 'Gb': 92.50, 'G': 98.00, 'Ab': 103.83, 
	'r': 666.666}

# dictionary with octaves
basefreqs = {}
for note, freq in notetofreq.iteritems():
	basefreqs[freq] = note
for freq in basefreqs:
	for j in range(10):
		if j < 1:
			notetofreq[basefreqs[freq] + str(j)] = freq * pow(2,j)
		else:
			notetofreq[basefreqs[freq] + str(j)] = freq * pow(2,j - 1)

# instantiate PyAudio 
p = pyaudio.PyAudio()

def granulate(wavName, tonefreq, playlength, squares):
	# open wav file and calculate sample length and times to play
	wf = wave.open(wavName, 'rb')
	sr, dat = wavfile.read(wavName)

	samplelength = sr / tonefreq
	reptimes = playlength * tonefreq

	fractindex = samplelength - int(samplelength)
	smallsample = dat[:(int(samplelength))]
	smallsamplex = dat[:(int(samplelength)) + 1]

	if squares == 1:
		smallsample = effects.sqwave(smallsample)
		smallsamplex = effects.sqwave(smallsamplex)
	
	# construct fullsample in ratio for more exact frequency :: pitch
	fullsample = smallsample
	for i in range(int(reptimes)):
		det = random.random()
		if det > fractindex:
			fullsample = np.concatenate((fullsample, smallsample))
		else:
			fullsample = np.concatenate((fullsample, smallsamplex))

	fullsample = fullsample[0:sr * playlength]

	# test for rests
	if tonefreq == 666.666:
		fullsample = fullsample * 0

	return fullsample			

def tonebank(notelist):
	tonelist = []
	for note in notelist:
		note = granulate('voice.wav', notetofreq[note], 2, 1)
		note = effects.tremolo(note, 8)
		tonelist.append(note)

	return tonelist

mynotes = 'A4 D4 E4 Gb4 r'.split(' ')
mytones = tonebank(mynotes)

stream = p.open(format=8,
				channels=1,
				rate=44100,
				output=True)

while True:
	for tone in mytones:
		stream.write(tone)
		






