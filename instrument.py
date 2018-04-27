import pyaudio
import sys
import time
import random
import librosa
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from Tkinter import *
from scipy.io import wavfile

from effects import *
from randgen import *
from granulate import *

notetofreq = {'C': 16.35, 'Db': 17.32, 'D': 18.35, 'Eb': 19.45, 
			'E': 20.60, 'F': 21.83, 'Gb': 23.12, 'G': 24.50, 
			'Ab': 25.96, 'A': 27.50, 'Bb': 29.14, 'B': 30.87, 
			'r': 666.666}

basefreqs = {} # dictionary with octaves up to 20
for note, freq in notetofreq.iteritems():
	basefreqs[freq] = note
for freq in basefreqs:
	for j in range(21):
		notetofreq[basefreqs[freq] + str(j)] = freq * pow(2,j)

class instrument:
	def __init__(self, notelist, lengthlist, vollist, tremolofreq, panlist, wavname, sqwave):	
		p = pyaudio.PyAudio() # instantiate PyAudio 

		self.stream = p.open(format=8,
						channels=2,
						rate=44100,
						output=True)

		self.notelist = notelist
		self.lengthlist = lengthlist
		self.vollist = vollist
		self.tremolofreq = tremolofreq
		self.panlist = panlist

		self.wavname = wavname
		self.sqwave = sqwave

		self.tonelist = notelist #put all the shit together
		instrument.tonebank(self) 

	def tonebank(self): 
		LENGTH_CONST = 4 #4 for stereo, 2 for mono
		for i, note in enumerate(self.notelist):
			if not note.isdigit(): #for note names
				note = granulate(self.wavname, notetofreq[note], 
					self.lengthlist[i % len(self.lengthlist)] * LENGTH_CONST, 
					self.vollist[i % len(self.vollist)], self.sqwave, 
					self.panlist[i % len(self.panlist)])
			elif note.isdigit(): #for frequencies
				note = granulate(self.wavname, float(note), 
					self.lengthlist[i % len(self.lengthlist)] * LENGTH_CONST, 
					self.vollist[i % len(self.vollist)], self.sqwave, 
					self.panlist[i % len(self.panlist)])

			if self.tremolofreq[i % len(self.tremolofreq)] != 0: #tremolo
				note = tremolo(note, self.tremolofreq[i % len(self.tremolofreq)])

			self.tonelist[i] = note

		# 	if len(self.playline) == 0:
		# 		self.playline = note
		# 	else:
		# 		self.playline = np.vstack((self.playline, note)) #set up the playline from all of the constants! 
		# self.playline = np.array(self.playline)

	def play(self):
		while(True):
			for tone in (self.tonelist):
				self.stream.write(tone)
			# 	print(tone.shape)
			# self.stream.write(self.playline)
			# print(self.playline)

