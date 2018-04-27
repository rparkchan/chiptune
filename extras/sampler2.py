import pyaudio
import wave
import time
import random
import numpy as np
import random
import os
import sounddevice
from scipy.io import wavfile

NUM_DRUMS = 10
NUM_RESTS = 10
BEAT_LENGTH = 44100
MULT_CONSTANT = 4
kit = [] #build a kit

all_paths = []
rootdir = '../Samples/drums/'
for subdir, dirs, files in os.walk(rootdir):
	for k, file in enumerate((files)):
		if file.endswith(".wav"):
			all_paths.append(subdir + '/' + file)

zeros = np.zeros(BEAT_LENGTH, dtype=np.int16)
for i in range(NUM_DRUMS):
	sr, dat = wavfile.read(random.choice(all_paths))
	kit.append(np.append(dat, zeros))
	kit[i] = kit[i][0:BEAT_LENGTH]
for i in range(NUM_RESTS):
	kit.append(np.zeros(BEAT_LENGTH))

p = pyaudio.PyAudio() # instantiate PyAudio 
stream = p.open(format=8,
				channels=2,
				rate=44100,
				output=True)

while(True):
	sample = random.choice(kit)
	sample = sample[0:len(sample) * MULT_CONSTANT]
	stream.write(sample)