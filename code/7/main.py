# Code for HW7 - Implement Differential Evolution, MaxWalkSat and Simulated Annealing
# and compare them using Type1, Type2 and Type3 comparators. Using these comparators
# determing compare the 3 types for early termination criterion.

# Use DTLZ7 model - 2 objectives and 10 decisions.
from __future__ import division
from random import uniform, randint, random
import sys
from stats import rdivDemo, a12, different

from DTLZ7 import *         # Library for the model being optimized

__author__ = 'rshah6'
sys.dont_write_bytecode = True

# Global Configurations

eras = 5
era_length = 100
MWS_maxtries = 500
MWS_maxchanges = 100
MWS_p = 0.5
MWS_threshold = 999
MWS_steps = 10
era_collection = []
DE_cr = 0.4
DE_f  = 0.5
DE_npExpand = 10
zeros10 = [0,0,0,0,0,0,0,0,0,0]
ones10 = [1,1,1,1,1,1,1,1,1,1]

class o():
    def __init__(self,lst,m,eq,lt,n):
        self.l = lst
        self.m = m
        self.eq = eq
        self.lt = lt
        self.n = n

def type2(era1,era2):
    """
    Based on effect size test - A12
    """
    a12_o1 = a12(calc_obj1(era1),calc_obj1(era2))
    a12_o2 = a12(calc_obj2(era1),calc_obj2(era2))
    if a12_o1 >= 0.56 or a12_o2 > 0.56:
        return 5
    else:
        return -1

def random10():
    x=[random() for i in range(0, 10)]
    return x

def SimulatedAnnealing (kmax, baseline, eras):
    """
    SimulatedAnnealing implementation
    """
    def P(en, e, t):
        try:
            return math.exp((e-en)/t)
        except:
            return 1

    def neighbor(x):
        xn = x[:]
        p = 0.25
        for n in xrange(len(x)):
            val = x[n]
            if random() > p:
                val = uniform(zeros10[n],ones10[n])
            xn[n] = val
        return xn

    k=0
    sb = baseline[:]
    s = sb[:]
    e, eb = dtlz7(s), dtlz7(s)
    emax = -1
    curr_era, prev_era, all_eras , all_best = [], [], [], []
    op = ""
    is_early = False
    while True:
        k +=1
        sn = neighbor(s)
        en = dtlz7(sn)

        if type1(sn,sb) == sn:  # Better solution
            sb = sn[:]
            eb =  en

        if type1(sn,s) == sn:   # Update current
            s = sn[:]
            e = en

        elif P(en, e, k/kmax) < random():   # Jump to worse?
            s = sn[:]
            e = en

        if k == 0 or k % era_length != 0:
            curr_era.append(s)
        else:
            if len(prev_era) > 0:
                eras = eras + type2(prev_era,curr_era)
            prev_era = curr_era[:]
            curr_era = []
            if k > kmax or eras < 1:
                if eras < 1:
                    is_early = True     # Early termination detected
                break

    return is_early, sb, prev_era
  
def MaxWalkSat(p,baseline,eras):
    """
    MaxWalkSat implementation 
    """
    evals = 0
    sb = random10()
    total_evals = 0
    cprob = [0,0,0,0,0,0,0]
    curr_era = []
    prev_era = []

    def change_random_c(x,c):
        x_new = x[:]
        x_new[c] = random()
        res = type1(x,x_new)
        return res

    def change_c_to_minimize(x,c, MWS_steps):
        x_best = x[:]
        x_curr = x[:]
        dx = 1.0/float(MWS_steps)
        for i in xrange(0, MWS_steps):
            x_curr[c] = ones10[c] - dx*i
            if type1(x_curr,x_best) == x_curr:
                x_best = x_curr[:]
        res = type1(x,x_best)
        return res

    sb = baseline[:]
    solution = baseline[:]
    print_sol_sb = []
    print_sol = []
    op = ""
    is_early = False
    all_eras = []
    all_best = []
    for i in xrange(0, MWS_maxtries):
        if i != 0:
            solution = random10()

        for j in xrange(0, MWS_maxchanges):
            if dtlz7(solution) > MWS_threshold:
                return solution

            c = randint(0,9)
            if p < random():
                solution = change_random_c(solution,c)

            else:
                solution = change_c_to_minimize(solution,c, MWS_steps)

        if type1(solution,sb) == solution :
            sb = solution[:]

        if i==0 or i % era_length != 0:
            curr_era.append(solution)
        else:
            if len(prev_era) > 0:
                eras = eras + type2(prev_era,curr_era)
            prev_era = curr_era[:]
            curr_era = []
            if eras < 1:
                is_early = True
                break

    return is_early, sb, prev_era

def DifferentialEvolution (cr, f, k_max,baseline, eras):
    """
    DifferentialEvolution implementation
    """
    np = era_length
    k = 0
    eras = 10
    is_early = False
    def update(x,y,z):
        sn=[]
        def smear((x1, y1, z1)):
            xi = x1
            if cr <= random():
                xi = x1
            else:
                xi = xi + f*(y1-z1)
            if xi>0 and xi<1:
                return xi
            else:
                return x1
        for i in xrange(0,len(x)):
            sn = [smear(these) for these in zip(x,y,z)]
        return sn

    def create_frontier(baseline):
        frontier = []
        frontier.append(baseline)
        for i in xrange(1, np):
            frontier.append(random10())
        return frontier

    def generate_items(population,cur):
        found = []
        while len(found) < 3:
            rand_index = randint(0, np-1)
            if rand_index == cur:
                continue
            if rand_index not in found:
                found.append(rand_index)
        return population[found[0]], population[found[1]], population[found[2]]

    def era_energy(final_frontier):
        res = []
        for i in xrange(0,len(final_frontier)):
            res.append(dtlz7(final_frontier[i]))
        return res

    frontier = create_frontier(baseline)
    s = baseline[:]
    sb = baseline[:]
    e = eb = dtlz7(baseline)

    all_eras, prev_era, curr_era = [], [], []
    while True:
        for i,candidate in enumerate(frontier):
            x, y, z = generate_items(frontier,i)
            sn = update(x,y,z)
            en = dtlz7(sn)

            if type1(sb,sn) == sn:
                sb = sn[:]
                eb = en

            if type1(candidate,sn) == sn:
                frontier[i] = sn

            k = k + 1
        curr_era = frontier[:]
        if len(prev_era) > 0:
            eras = eras + type2(prev_era,curr_era)
        prev_era = curr_era[:]
        all_eras.extend(prev_era)

        if k > k_max or eras < 1:
            if eras < 1:
                is_early = True
            break

    return is_early, sb, prev_era

def main():
    kmax = 6000
    DE_eras = ["DE"]
    mws_eras = ["MWS"]
    sa_eras = ["SA"]
    et_counter = {'SA':0,'MWS':0,'DE':0}
    for i in xrange(20):
        print "---------------------------"
        print "Current Repetition: ", i + 1
        baseline = random10()
        
        # Get MWS results
        mws_ET, MWS_sol, MWS_era = MaxWalkSat (MWS_p,baseline,eras)
        print "MWS solution: ", round(dtlz7(MWS_sol),2)
        res = [dtlz7(x) for x in MWS_era]
        res.insert(0,"MWS"+str(i+1))
        era_collection.append(res)
        if mws_ET:
            et_counter['MWS'] += 1
        MWS_era = []

        # Get SA results
        sa_ET,sa_sol, sa_era = SimulatedAnnealing(kmax,baseline,eras)
        print "SA solution: ", round(dtlz7(sa_sol),2)
        
        res = [dtlz7(x) for x in sa_era]
        res.insert(0,"SA" + str(i+1))
        era_collection.append(res)
        
        if sa_ET:
            et_counter['SA']+=1
        sa_era = []
        
        # Get DE results
        de_ET, DE_sol, DE_era = DifferentialEvolution( DE_cr, DE_f,12000,baseline,eras)
        print "DE solution", round(dtlz7(DE_sol),2)
        res = [dtlz7(x) for x in DE_era]
        res.insert(0,"DE" + str(i+1))
        era_collection.append(res)
        if de_ET:
            et_counter['DE'] += 1
        DE_era=[]

    rdivDemo(era_collection)

if __name__ == "__main__":
    main()
