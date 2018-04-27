import pyaudio
import wave
import sys
import time
import random
import effects
import synthesis
import numpy as np
import matplotlib.pyplot as plt
from Tkinter import *
from scipy.io import wavfile

p = pyaudio.PyAudio()

x = np.linspace(0, 2 * np.pi, 440)
sine = np.sin(x)
sinear = np.array(sine)

y = np.linspace(0, 2 * np.pi, 500)
sine2 = np.sin(y)
sine2 = sine2[0:440]
sinear2 = np.array(sine2)

stream = p.open(format=8,
				channels=1,
				rate=44100,
				output=True)

while True:
	stream.write(sinear + sinear2)