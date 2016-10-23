from __future__ import division, print_function
import sys
from random import *
from schaffer import Schaffer
from osyczka2 import Osyczka2
from kursawe import Kursawe

RANGES = [(0,10),(0,10),(1,5),(0,6),(1,5),(0,10)]
def mws(m):
    """
    Runs MaxWalkSat algorithm to minimize Osyczka2 model
    """
    print("Running max walk sat for ", m.name)
    tries = 15;
    changes = 75;
    p = 0.5
    best = m.any()
    for i in xrange(tries):
        current = m.any()
        for j in xrange(changes):
            if(m.evaluate(current) < m.evaluate(best)):
                say("!")
                best = current[:]
            if p < random():
                prev = current[:]
                current = mutate_any(m,current)
            else:
                prev = current[:]
                current = mutate_x(m,current)
            if(m.evaluate(current) < m.evaluate(best)):
                say("!")
                best = current[:]
            elif(m.evaluate(current) < m.evaluate(prev)):
                say("+")
            else:
                say(".")
        print(", ", round(m.evaluate(best), 5))
    print("#iterations:", tries)
    print("best solution:",  best)
    print("best score:", m.evaluate(best))
    print("MaxWalkSat ends here\n\n")


def mutate_any(m,x):
    """
    Mutates a random decision in the solution
    """
    i = randint(0, len(x)-1)
    x[i] = randint(RANGES[i][0], RANGES[i][1])
    while not m.ok(x):
        x[i] = randint(RANGES[i][0], RANGES[i][1])
    return x

def mutate_x(m,x):
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
        while not m.ok(x):
            x[i] = mutate_ith(x, i)
    return x


def say(x):
    print(x, end="")
