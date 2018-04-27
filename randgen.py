import random

def randnotes(notelist, conctimes, lower, upper):
	notelist *= conctimes
	newlist = [note + str(random.randint(lower,upper)) for note in notelist]
	random.shuffle(newlist)
	return newlist

def randnumlist(length, lower, upper):
	newlist = [random.uniform(lower, upper) for i in range(length)]
	return newlist