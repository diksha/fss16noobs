from __future__ import division, print_function
from random import *
import math

seed(10)

def energy(x):
    """
    Returns energy of given solution 
    """
    f1 = x**2           # Function 1 of Schaffer
    f2 = (x-2)**2       # Function 2 of Schaffer
    max_x = 10**15
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
    s = uniform(10**(-15), 10**(15))
    e = energy(s)
    sb = s
    eb = e
    k = 1
    kmax = 1000
    max_x = 10**15
    emax = energy(max_x) - 1.01
   
    while k < kmax and e > emax:
        if k == 1 or k % 25 == 0: 
            print("\n%d, %.2f, " % (k, eb), end="")     #Print the evaluation
        sn = uniform(10**(-15), 10**(15))   # Pick some neighbour
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
    return sb

sa()