import pyaudio
from granulate import *

# construct dictionary mapping i.e. "A4" to 440
NOTES = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
FREQS = [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87]
notetofreq = {'r': 0}
for i,note in enumerate(NOTES):
	for j in range(20):
		notetofreq[note + str(j)] = FREQS[i] * pow(2,j)

# an instrument instance holds a tonelist: np array of 1s and 0s to be read through 
class instrument:
	def __init__(self, tonelist):
		p = pyaudio.PyAudio()
		self.stream = p.open(format=8,
						channels=2,
						rate=44100,
						output=True)
		self.granlist = [granulate(tone) for tone in tonelist]
	
	def play(self):
		while(True):
			for gran in self.granlist:
				self.stream.write(gran)