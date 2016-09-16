from __future__ import division, print_function
from random import *
import math
seed(10)

def energy(x):
    f1 = x**2
    f2 = (x-2)**2
    max_x = 10**15
    max = (max_x)**2 + (max_x-2)**2
    min_x = 1
    min = (min_x)**2 + (min_x-2)**2
    return ((f1+f2) - min)/(max-min)

def P(e, en, t):
    return math.exp((e-en)/t)

def sa():
    s = uniform(10**(-15), 10**(15))
    e = energy(s)
    sb = s
    eb = e
    k = 1
    kmax = 1000
    max_x = 10**15
    emax = energy(max_x) - 0.01
   
    while k < kmax: # and e > emax:
        sn = uniform(10**(-15), 10**(15))
        en = energy(sn)
        if en < eb:
            sb = sn
            eb = en
            print("!", end="")
        if en < e:
            s = sn
            e = en
            print("+", end="")
        elif P(e, en, k/kmax) < random():
            s = sn
            e = en
            print("?", end="")
        else:
            print(".", end="")
        k += 1
        if k % 25 == 0:
            print("\n", eb)
    return sb
        
    
sa()