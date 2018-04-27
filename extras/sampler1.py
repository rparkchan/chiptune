import pyaudio
import wave
import time
import random
import numpy as np
import random
import pyglet
from scipy.io import wavfile
import sounddevice as sd

def ADSR(a, d, s, r, length):
	assert s <= 1, "too loud! yuck!!"
	assert a + d + r <= length, "too long, ugh!"

	attack = np.linspace(0, 1, a)
	decay = np.linspace(1, s, d)
	sustain = np.zeros(length - a - d - r) + s
	release = np.linspace(s, 0, r)
	return np.concatenate((attack, decay, sustain, release))

if __name__ == "__main__":
	p = pyaudio.PyAudio() # instantiate PyAudio 
	stream = p.open(format=8,
					channels=2,
					rate=44100,
					output=True)

	MULT_CONSTANT = 4 #4 for stereo, 2 for mono
	rl = 44100 #real, desired length
	sl = MULT_CONSTANT * rl #actual, fucked up length
	sr, dat = wavfile.read("fall d'emure.wav")

	# while(True):
	start_point = random.randint(0, len(dat) - sl)
	sample = dat[start_point:start_point + sl]
	env = ADSR(a = rl/8, d = rl/8, s = .5, 
		r = rl/4, length = rl)
	env = np.append(env, np.zeros(sl-rl))
	mult_env = np.array([env,]*2)
	res = np.array(sample * np.transpose(mult_env), dtype = np.int16)
	
	while(True):
		stream.write(res)
