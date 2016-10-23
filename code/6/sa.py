from __future__ import division, print_function
from random import *
import random
import math
from schaffer import Schaffer
from osyczka2 import Osyczka2
from kursawe import Kursawe

seed(10)

# Set min and max values of x
max_x = 0
min_x = 0
iters = 100


def setMaxMin(m):
	"""
	Sets max and min energies for mapping energy
	"""
	global iters
	global max_x, min_x
	ss = []
	for i in xrange(iters):
		ss.append(m.evaluate(m.any()))
	max_x = max(ss)
	min_x = min(ss)


def sa(m):
    """
    Runs simulated annealing for Schaffer model
    """
    print("Running simulated annealing for ", m.name)
    setMaxMin(m)
    s = m.any()
    e = m.evaluate(s)

    print ("Initial x = %s and energy = %s" % (str(s), str(e)))

    sb = s
    eb = e
    k = 1
    kmax = 1000
    epsilon = 1.01

    while k < kmax and eb > min_x:
        if k == 1 or k % 25 == 0:
            print("\n%d, %f, " % (k, eb), end="")     #Print the evaluation
        sn = neighbour(m,s)   # Pick some neighbour
        en = m.evaluate(sn)                     # Compute its energy
        if en < eb:                         # New best found, update best
            sb = sn
            eb = en
            print("!", end="")
        if en < e:                          # Should we just to better?
            s = sn
            e = en
            print("+", end="")
        elif P(e, en, k/kmax) < random.random():       # Jump to something worse with low probability
            s = sn
            e = en
            print("?", end="")
        else:
            print(".", end="")
        k += 1
    print("\n\nBest solution by simulated annealing x = %s with normalized energy = %s ." % (str(sb), str(eb)))
    print("SimulatedAnnealing ends here \n\n")
    return sb


def P(e, en, t):
    """
    Returns probability for jumping to worse solution
    """
    return math.exp((e-en)/t)

def neighbour(m, s):
	"""
	Generates neighbour solutions within +/- 10 percent of the decision bounds till a valid solution is found
	"""
	valid, sn = act_neighbour(m, s)
	while not valid:
		valid, sn = act_neighbour(m, s)
	return sn

def act_neighbour(m, s):
	"""
	Actual neighbour generation solution
	"""
	sn = []
	for i in xrange(len(m.decisions)):
		d = m.decisions[i]
		dc = (d.high-d.low)/10
		if(random.randint(0,1) == 0):
			dn = s[i] - dc
			if(dn < m.decisions[i].low):
				dn = m.decisions[i].low
		else:
			dn = s[i] + dc
			if(dn > m.decisions[i].high):
				dn = m.decisions[i].high
		sn.append(dn)
	return m.ok(sn), sn
