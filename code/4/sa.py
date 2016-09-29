from __future__ import division, print_function
from random import *
import math

seed(10)

# Set min and max values of x
max_x = 10**5
min_x = -10**5

def energy(x):
    """
    Returns normalized energy of given solution 
    """
    f1 = x**2           # Function 1 of Schaffer
    f2 = (x-2)**2       # Function 2 of Schaffer
    max = (max_x)**2 + (max_x-2)**2
    min_x = 1
    min = (min_x)**2 + (min_x-2)**2
    return ((f1+f2) - min)/(max-min)

def P(e, en, t):
    """
    Returns probability for jumping to worse solution
    """
    return math.exp((e-en)/t)

def sa():
    """
    Runs simulated annealing for Schaffer model
    """
    s = uniform(min_x, max_x)
    e = energy(s)
    
    print ("Initial x = %f and energy = %f" % (s, e))
    
    sb = s
    eb = e
    k = 1
    kmax = 1000
    epsilon = 1.01
    emax = energy(max_x) - epsilon
   
    while k < kmax and eb > emax:
        if k == 1 or k % 25 == 0: 
            print("\n%d, %f, " % (k, eb), end="")     #Print the evaluation
        sn = uniform(min_x, max_x)   # Pick some neighbour
        en = energy(sn)                     # Compute its energy
        if en < eb:                         # New best found, update best
            sb = sn
            eb = en
            print("!", end="")
        if en < e:                          # Should we just to better?
            s = sn
            e = en
            print("+", end="")
        elif P(e, en, k/kmax) < random():       # Jump to something worse with low probability
            s = sn
            e = en
            print("?", end="")
        else:
            print(".", end="")
        k += 1
    print("\n\nBest solution by simulated annealing x = %f with normalized energy = %f ." % (sb, eb))
    return sb

sa()