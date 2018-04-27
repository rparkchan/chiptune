# gui nonsense

#setup GUI
# master = Tk()
# w1 = Scale(master, from_=1, to=10)
# w1.pack()
# w2 = Scale(master, from_=1, to=200)
# w2.pack()

# in a loop
# master.update()

# list comprehension for fullsample
# sizefull = playlength * sr
# fullsample = np.array([smallsample[i%len(smallsample)] for i in range(sizefull)])
# pair = [sine[i % len(x)]*pair[j] for j in range(2)]

# def sqwave(sample):
# 	for pair in sample:
# 		for j in range(2):
# 			if pair[j] > 0:
# 				pair[j] = 2000
# 			else:
# 				pair[j] = 0	
# 	return sample

# square = lambda d: 2000 if d > 0 else 0
# return sample.map(square)

# poo = (sample > 0) * 2000

# notetofreq = {'C': 16.35, 'Db': 17.32, 'D': 18.35, 'Eb': 19.45, 
# 			'E': 20.60, 'F': 21.83, 'Gb': 23.12, 'G': 24.50, 
# 			'Ab': 25.96, 'A': 27.50, 'Bb': 29.14, 'B': 30.87, 
# 			'r': 666.666}

# # dictionary with octaves up to 10
# basefreqs = {}
# for note, freq in notetofreq.iteritems():
# 	basefreqs[freq] = note
# for freq in basefreqs:
# 	for j in range(20):
# 		notetofreq[basefreqs[freq] + str(j)] = freq * pow(2,j)
