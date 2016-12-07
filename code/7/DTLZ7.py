from __future__ import division
from random import uniform, randint, random
import sys
from math import pi, sin

from cdom import cdom       #Library for computing CDom loss

sys.dont_write_bytecode = True

def dtlz7(x):
    f1 = f_one(x)
    f2 = (1+g(x))*h(f1,g(x),2)
    return f1 + f2

def f_one(x):
    return x[0]

def f_two(x):
    f1 = f_one(x)
    f2 = (1+g(x))*h(f1,g(x),2)
    return f2

def g(x):
    res = sum(x)
    res = 1 + (9/len(x))*res
    return res

def h(f1,g,M):
    theeta = 3*pi*f1
    res = (f1/(1+g))*(1+sin(theeta))
    res = M - res
    return res

def type1(x,y):
    return cdom(x,y)

def calc_obj1(sol):
    res = [f_one(x) for x in sol]
    return res

def calc_obj2(sol):
    res = [f_two(x) for x in sol]
    return res

def median(lst):    #Approx for speed
    return sum(lst)/len(lst)