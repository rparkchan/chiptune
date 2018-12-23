#1B make one or two
from instrument import *

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

notelist = 'B4 r D4 r'.split(' ') #notes or numbers
lengthlist = [.96] #in seconds

tremlen = 1000
tremolofreq = [1/tremlen] #in fq, repeating sequence
vollist = [3] #value of 1 is appropriate, repeating sequence
panlist = [-1, 1] #value of 0 for mono, -1 for left, 1 for right, repeating sequence

wavname = 'sounds/voice.wav'
sqwave = True

# notelist = randnotes(notelist, conctimes = 40, lower = 3, upper = 5) #random generators
# lengthlist = randnumlist(len(notelist), .06, .64)
# vollist = randnumlist(len(notelist), 3,5)
# tremolofreq = randnumlist(len(notelist), 1, 6)
# panlist = randnumlist(len(notelist), -.5, .5)

r = instrument(notelist, lengthlist, vollist, tremolofreq, panlist, wavname, sqwave)

# voice.wav has really grainy unsquared, really clean squared up to 6th octave
# dm.wav unsquared is too rough, pretty saw squared
# intoyou.wav unsquared is unusable, squared lower register is gnarly
# ct.wav unsquared is piercing, same with squared
# star.wav has rough unsquared, but super super fat squared