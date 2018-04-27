import random
import numpy as np
import time

def sqwave(sample):
	return np.array((sample > 0) * 2000, dtype=np.int16)

def pitchcorrect(smallsample, fractindex):
	det = random.random()
	if det > fractindex:
		return smallsample[:len(smallsample) - 1] #temp
	else:
		return smallsample

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

	poo = np.concatenate((sine,sine), axis=1)

	return np.array(sample * poo, dtype=np.int16)

def pan(sample, pan):
	panleft = 1 - pan
	panright = 1 + pan

	return sample * [panleft, panright]
