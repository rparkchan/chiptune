import pyaudio
import wave
import sys
import time
import random
import numpy as np
from Tkinter import *
from scipy.io import wavfile

# dictionary from str to float
notetofreq = {'A': 55.00, 'Bb': 58.27, 'B': 61.74, 'C': 65.41, 'Db': 69.30, 'D': 73.42, 'Eb': 77.78, 'E': 82.41, 'F': 87.31, 'Gb': 92.50, 'G': 98.00, 'Ab': 103.83, 'r': 666.666}

# dictionary from float to str 
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

def granulate(wavName, tonefreq, playlength):

	poo = time.time()
	# open wav file and calculate sample length and times to play
	wf = wave.open(wavName, 'rb')
	sr, dat = wavfile.read(wavName)

	samplelength = sr / tonefreq
	grantimes = playlength * tonefreq

	# open stream 
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True)

	smallsample = dat[:int(samplelength) * 4]
	# fullsample = smallsample

	# for i in range(int(grantimes)):
	# 	fullsample = np.concatenate((fullsample, smallsample))

	# test for rests
	amp = 1
	if tonefreq == 666.666:
		amp = 0
	# fullsample = fullsample * amp

	# stream.write(fullsample)



	for i in range(int(grantimes)):
		stream.write(smallsample)

	poo2 = time.time()
	print poo2-poo

def tremolo(wav, size):
	x = np.linspace(-np.pi, np.pi, size)
	sine = np.sin(x)
	sine += 1
	sine *= .5
	sine = list(sine)

	for i, piece in enumerate(wav):	
		piece = map(float, piece)
		piece = [sine[i % size]*piece[j] for j in range(2)]

	return wav

notelist = 'A4 B4'.split(' ')

while True: 
	for note in notelist:
		granulate('dm.wav', notetofreq[note], 1)





