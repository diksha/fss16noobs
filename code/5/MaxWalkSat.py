from __future__ import division, print_function
import sys
from random import *

RANGES = [(0,10),(0,10),(1,5),(0,6),(1,5),(0,10)]

def maxwalksat(tries, changes, p):
    """
    Runs MaxWalkSat algorithm to minimize Osyczka2 model
    """
    best = randomx()
    for i in xrange(tries):
        current = randomx()
        for j in xrange(changes):
            if(score(current) < score(best)):
                say("!")
                best = current[:]
            if p < random():
                prev = current[:]
                current = mutate_any(current)
            else:
                prev = current[:]
                current = mutate_x(current)
            if(score(current) < score(best)):
                say("!")
                best = current[:]
            elif(score(current) < score(prev)):
                say("+")
            else:
                say(".")
        print(", ", round(score(best), 5))
    print("#iterations:", tries)
    print("best solution:",  best)
    print("best score:", score(best))


def mutate_any(x):
    """
    Mutates a random decision in the solution
    """
    i = randint(0, len(x)-1)
    x[i] = randint(RANGES[i][0], RANGES[i][1])
    while not ok(x):
        x[i] = randint(RANGES[i][0], RANGES[i][1])
    return x
    
def mutate_x(x):
    """
    Mutates the entire decision
    """
    
    def mutate_ith(x, i):
        """
        Mutates the i-th decision
        """
        xi = x[i]
        delta = (RANGES[i][1]-RANGES[i][0])/10
        if(random() < 0.5):
            xi = max (xi - delta, RANGES[i][0])
        else:
            xi = min (xi + delta, RANGES[i][1])
        return xi
    
    for i in xrange(len(x)):
        x[i] = mutate_ith(x, i)
        while not ok(x):
            x[i] = mutate_ith(x, i)
    return x

def randomx():
    """
    Returns a valid decision satisfying constraints
    """
    x = [-1, -1, -1, -1, -1, -1]
    while not ok(x):
        for i in range(len(x)):
            x[i] = randint(*RANGES[i])
    return x
    
def ok(x):
    """
    Returns true if values in decision satify all constraints
    """
    g1 = 0 <= x[0] + x[1] - 2
    g2 = 0 <= 6 - x[0] - x[1]
    g3 = 0 <= 2 - x[1] + x[0]
    g4 = 0 <= 2 - x[0] + 3*x[1]
    g5 = 0 <= 4 - (x[2] - 3)**2  - x[3]
    g6 = 0 <= (x[4] - 3)**3 + x[5] - 4
    return (g1 and g2 and g3 and g4 and g5 and g6)

def f1(x):
    val = -(25*(x[0]-2)**2 + (x[1]-2)**2 + ((x[2]-1)*(x[3]-4))**2 + (x[4]-1)**2)
    return val

def f2(x):
    val = x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 + x[4]**2
    return val  

def score(x):
    """
    Returns a normalized score for given decision
    """
    return (f1(x) + f2(x) - min_score) / (max_score - min_score);
    
def say(x):
    print(x, end="")

def get_min_max():
    x = randomx()
    max_score = min_score = f1(x) + f2(x)
    iterations = 10000
    for _ in range(iterations):
        x = randomx()
        max_score = max(max_score, f1(x) + f2(x))
        min_score = min(min_score, f1(x) + f2(x))
    return (min_score, max_score)

min_score, max_score = get_min_max()       
maxwalksat(20, 50, 0.5)