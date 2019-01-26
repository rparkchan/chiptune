from granulate import *

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