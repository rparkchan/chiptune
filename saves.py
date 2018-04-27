from instrument import *

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

notelist = 'E1 Gb 4'.split(' ') #notes or numbers
lengthlist = [.96, .12] #in seconds

tremolofreq = [10, 30] #in fq, repeating sequence
vollist = [4] #value of 1 is appropriate, repeating sequence
panlist = [-1, 1] #value of 0 for mono, -1 for left, 1 for right, repeating sequence

wavname = 'sounds/voice.wav'
sqwave = True

# notelist = randnotes(notelist, conctimes = 10, lower = 6, upper = 6) #random generators
# lengthlist = randnumlist(len(notelist), .06, .64)
vollist = randnumlist(len(notelist), 2, 6)
# tremolofreq = randnumlist(len(notelist), 1, 6)
# panlist = randnumlist(len(notelist), -.5, .5)

r = instrument(notelist, lengthlist, vollist, tremolofreq, panlist, wavname, sqwave)

# voice.wav has really grainy unsquared, really clean squared up to 6th octave
# dm.wav unsquared is too rough, pretty saw squared
# intoyou.wav unsquared is unusable, squared lower register is gnarly
# ct.wav unsquared is piercing, same with squared
# star.wav has rough unsquared, but super super fat squared

#2A
from instrument import *

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

notelist = 'D6 A5 B5 Gb5 A5'.split(' ') #notes or numbers
lengthlist = [.432, .432] #in seconds

tremlen = 10000
tremolofreq = [1/tremlen] #in fq, repeating sequence
vollist = [4, 5] #value of 1 is appropriate, repeating sequence
panlist = [-1, 1] #value of 0 for mono, -1 for left, 1 for right, repeating sequence

wavname = 'sounds/voice.wav'
sqwave = True

# notelist = randnotes(notelist, conctimes = 40, lower = 5, upper = 6) #random generators
# lengthlist = randnumlist(len(notelist), .06, .64)
# vollist = randnumlist(len(notelist), 1, 5)
# tremolofreq = randnumlist(len(notelist), 1, 6)
# panlist = randnumlist(len(notelist), -.5, .5)

r = instrument(notelist, lengthlist, vollist, tremolofreq, panlist, wavname, sqwave)

# voice.wav has really grainy unsquared, really clean squared up to 6th octave
# dm.wav unsquared is too rough, pretty saw squared
# intoyou.wav unsquared is unusable, squared lower register is gnarly
# ct.wav unsquared is piercing, same with squared
# star.wav has rough unsquared, but super super fat squared

#_________

#1A make two or three
from instrument import *

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

notelist = 'A B C D'.split(' ') #notes or numbers
lengthlist = [.24] #in seconds

tremolofreq = [0] #in fq, repeating sequence
vollist = [4] #value of 1 is appropriate, repeating sequence
panlist = [-1, 1] #value of 0 for mono, -1 for left, 1 for right, repeating sequence

wavname = 'sounds/voice.wav'
sqwave = True

notelist = randnotes(notelist, conctimes = 40, lower = 3, upper = 5) #random generators
# lengthlist = randnumlist(len(notelist), .06, .64)
vollist = randnumlist(len(notelist), 1, 3)
# tremolofreq = randnumlist(len(notelist), 1, 6)
# panlist = randnumlist(len(notelist), -.5, .5)

r = instrument(notelist, lengthlist, vollist, tremolofreq, panlist, wavname, sqwave)

# voice.wav has really grainy unsquared, really clean squared up to 6th octave
# dm.wav unsquared is too rough, pretty saw squared
# intoyou.wav unsquared is unusable, squared lower register is gnarly
# ct.wav unsquared is piercing, same with squared
# star.wav has rough unsquared, but super super fat squared

#1B make one or two
from instrument import *

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

notelist = 'A B C D E G'.split(' ') #notes or numbers
lengthlist = [.12] #in seconds

tremolofreq = [0] #in fq, repeating sequence
vollist = [4] #value of 1 is appropriate, repeating sequence
panlist = [-1, 1] #value of 0 for mono, -1 for left, 1 for right, repeating sequence

wavname = 'sounds/voice.wav'
sqwave = True

notelist = randnotes(notelist, conctimes = 40, lower = 3, upper = 5) #random generators
# lengthlist = randnumlist(len(notelist), .06, .64)
vollist = randnumlist(len(notelist), 1, 3)
# tremolofreq = randnumlist(len(notelist), 1, 6)
# panlist = randnumlist(len(notelist), -.5, .5)

r = instrument(notelist, lengthlist, vollist, tremolofreq, panlist, wavname, sqwave)

# voice.wav has really grainy unsquared, really clean squared up to 6th octave
# dm.wav unsquared is too rough, pretty saw squared
# intoyou.wav unsquared is unusable, squared lower register is gnarly
# ct.wav unsquared is piercing, same with squared
# star.wav has rough unsquared, but super super fat squared

#3A
from instrument import *

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

notelist = 'E5 r'.split(' ') #notes or numbers
lengthlist = [.96] #in seconds

tremlen = .03
tremolofreq = [1/tremlen] #in fq, repeating sequence
vollist = [4] #value of 1 is appropriate, repeating sequence
panlist = [-1, 1] #value of 0 for mono, -1 for left, 1 for right, repeating sequence

wavname = 'sounds/voice.wav'
sqwave = True

# notelist = randnotes(notelist, conctimes = 10, lower = 2, upper = 6) #random generators
# lengthlist = randnumlist(len(notelist), .06, .64)
# vollist = randnumlist(len(notelist), 1, 5)
# tremolofreq = randnumlist(len(notelist), 1, 6)
# panlist = randnumlist(len(notelist), -.5, .5)

r = instrument(notelist, lengthlist, vollist, tremolofreq, panlist, wavname, sqwave)

# voice.wav has really grainy unsquared, really clean squared up to 6th octave
# dm.wav unsquared is too rough, pretty saw squared
# intoyou.wav unsquared is unusable, squared lower register is gnarly
# ct.wav unsquared is piercing, same with squared
# star.wav has rough unsquared, but super super fat squared

#3B
from instrument import *

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

# notelist = 'Db5 Ab4 B4 Db4 B3 Ab4 B4 Db4 B3 Ab4 B4'.split(' ') #notes or numbers
# lengthlist = [.72, .36, .36, .72, .72, .36, .36, .72, .72, .72, .72] #in seconds

notelist = 'B5 Db5 r A5 B5 r'.split(' ') #notes or numbers
lengthlist = [.12] #in seconds

tremlen = 1000
tremolofreq = [1/tremlen] #in fq, repeating sequence
vollist = [8] #value of 1 is appropriate, repeating sequence
panlist = [-1, 1] #value of 0 for mono, -1 for left, 1 for right, repeating sequence

wavname = 'sounds/voice.wav'
sqwave = True

# notelist = randnotes(notelist, conctimes = 10, lower = 2, upper = 6) #random generators
# lengthlist = randnumlist(len(notelist), .06, .64)
# vollist = randnumlist(len(notelist), 1, 5)
# tremolofreq = randnumlist(len(notelist), 1, 6)
# panlist = randnumlist(len(notelist), -.5, .5)

r = instrument(notelist, lengthlist, vollist, tremolofreq, panlist, wavname, sqwave)

# voice.wav has really grainy unsquared, really clean squared up to 6th octave
# dm.wav unsquared is too rough, pretty saw squared
# intoyou.wav unsquared is unusable, squared lower register is gnarly
# ct.wav unsquared is piercing, same with squared
# star.wav has rough unsquared, but super super fat squared