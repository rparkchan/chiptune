from instrument import *
import numpy as np
import math

GOAL_TIME = n = 10.0
STARTING_TEMPO = s = 60
GOAL_TEMPO = z = 120

NUM_NOTES = 22
NOTES_BEFORE = 2 ####
NOTES_AFTER = 200

NOTE = 'Gb4' #####

NR_RATIO = .3
RN_RATIO = 1 - NR_RATIO

a = (z-s)/(n-1)
b = (n*s - z)/(n-1)
c = (z-s)/math.log(n)
d = s
e = (z-s)/(math.exp(n) - math.exp(1))
f = (math.exp(n)*s - math.exp(1)*z)/(math.exp(n)-math.exp(1))

linear_lengthlist = []
log_lengthlist = []
exp_lengthlist = []

notelist = []

for i in range(NUM_NOTES):
	curr_time = 1 + i*(GOAL_TIME-1.0)/NUM_NOTES
	linear_lengthlist.append(60 * NR_RATIO / (a*curr_time + b))
	linear_lengthlist.append(60 * RN_RATIO / (a*curr_time + b))
	log_lengthlist.append(60 * NR_RATIO / (c*math.log(curr_time) + d))
	log_lengthlist.append(60 * RN_RATIO / (c*math.log(curr_time) + d))
	exp_lengthlist.append(60 * NR_RATIO / (e*math.exp(curr_time) + f))
	exp_lengthlist.append(60 * RN_RATIO / (e*math.exp(curr_time) + f))

	notelist.append(NOTE)
	notelist.append('r')

for j in range(NOTES_AFTER):
	linear_lengthlist.append(60 * NR_RATIO / GOAL_TEMPO)
	linear_lengthlist.append(60 * RN_RATIO / GOAL_TEMPO)

	log_lengthlist.append(60 * NR_RATIO / GOAL_TEMPO)
	log_lengthlist.append(60 * RN_RATIO / GOAL_TEMPO)

	exp_lengthlist.append(60 * NR_RATIO / GOAL_TEMPO)
	exp_lengthlist.append(60 * RN_RATIO / GOAL_TEMPO)

	notelist.append(NOTE)
	notelist.append('r')

for k in range(NOTES_BEFORE):
	linear_lengthlist.insert(0, 60 * RN_RATIO / STARTING_TEMPO)
	linear_lengthlist.insert(0, 60 * NR_RATIO / STARTING_TEMPO)

	log_lengthlist.insert(0, 60 * RN_RATIO / STARTING_TEMPO)
	log_lengthlist.insert(0, 60 * NR_RATIO / STARTING_TEMPO)

	exp_lengthlist.insert(0, 60 * RN_RATIO / STARTING_TEMPO)
	exp_lengthlist.insert(0, 60 * NR_RATIO / STARTING_TEMPO)

	notelist.insert(0, 'r')
	notelist.insert(0, NOTE)

print log_lengthlist

lengthlist = log_lengthlist ######

tremolofreq = [0] #in fq, repeating sequence
vollist = [1] #value of 1 is appropriate, repeating sequence
panlist = [0] #value of 0 for mono, -1 for left, 1 for right, repeating sequence

wavname = 'sounds/voice.wav'
sqwave = 1

r = instrument(notelist, lengthlist, vollist, tremolofreq, panlist, wavname, sqwave)