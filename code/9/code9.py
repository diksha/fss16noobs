from __future__ import division
__author__ = 'Dgohlya'
from models import Model
import dtlz
import random
import math
import hve
import cProfile
import glob
import pickle
from stats import rdivDemo

class candidate:
    num_objs = 10

    def __init__(self, decs):
        self.decs = decs
        self.fitness = None
        self.dom_count = 0

    def calc_fitness(self, fitness_family):
        self.fitness = fitness_family(self.decs, candidate.num_objs, len(self.decs))
        return

    def __gt__(self, other):
        if self.fitness == other.fitness:
            return False
        for i in xrange(candidate.num_objs):
            if other.fitness[i] < self.fitness[i]:
                return False
        return True

    def __repr__(self):
        return 'Candidate: ['+",".join([str(x) for x in self.decs])+']\n'


class population:
    num_candidates = 10;
    fitness_family = None
    prob_mut = 0.05
    num_decs = 2

    def __init__(self, num_candidates = 10, fitness_family = dtlz.dtlz1):
        self.candidates = []
        self.num_candidates = num_candidates
        self.fitness_family = fitness_family
        self.pop_pareto = []

    def randomize(self):
        for i in range(self.num_candidates):
            can = candidate([])
            for j in range(self.num_decs):
                can.decs.append(random.random())
            can.calc_fitness(self.fitness_family)
            self.candidates.append(can)
        self.ap_binary_dom()

    def crossover(self, candidate1, candidate2):
        crossover_point = random.randrange(0, self.num_decs)
        decs1 = []
        decs2 = []
        for i in xrange(crossover_point):
            decs1.append(candidate1.decs[i])
            decs2.append(candidate2.decs[i])
        for i in xrange(crossover_point, self.num_decs):
            decs1.append(candidate2.decs[i])
            decs2.append(candidate1.decs[i])
        can1 = candidate(decs1)
        can1.calc_fitness(self.fitness_family)
        can2 = candidate(decs2)
        can2.calc_fitness(self.fitness_family)
        return [can1, can2]

    def mutate(self, candidate):
        for i in xrange(self.num_decs):
            if random.random() < self.prob_mut:
                candidate.decs[i] = random.random()

    def __repr__(self):
        return ",".join([can.__repr__() for can in self.candidates])

    def ap_binary_dom(self):
        candidates = self.candidates
        n = self.num_candidates
        for candidate1 in candidates:
            can_dominates_all = True
            for candidate2 in candidates:
                if candidate2 > candidate1:
                    can_dominates_all = False
                    break
            if can_dominates_all:
                self.pop_pareto.append(candidate1)


class GA:
    fitness_family = None
    num_candidates = 100
    def __init__(self, fitness_family=dtlz.dtlz1, num_objs=2, num_decs=10, prob_mut=0.05, num_candidates=100, num_generations=1000):
        self.generations = []
        self.current_generation = 0
        self.num_candidates = int(num_candidates)
        self.fitness_family = fitness_family
        self.num_generations = int(num_generations)
        self.pareto_frontier = []
        candidate.num_objs = num_objs
        population.num_decs = num_decs
        population.prob_mut = prob_mut

    def randomize(self):
        gen1 = population(self.num_candidates, self.fitness_family)
        gen1.randomize()
        self.generations.append(gen1)
        self.pareto_frontier.extend(gen1.pop_pareto)
        return
    def update_pareto(self, new_pareto):
        add_new = []
        for new in new_pareto:
            for old in self.pareto_frontier:
                if new > old:
                    self.pareto_frontier.remove(old)
                if not old > new and not old==new:
                    add_new.append(new)
                    break
        self.pareto_frontier.extend(add_new)
    def next(self):
        curr_pop = self.generations[self.current_generation];
        next_pop = population(self.num_candidates, self.fitness_family)
        for i in range(0, self.num_candidates, 2):
            #print(self.pareto_frontier)
            pareto_idx=[0,0]
            if len(self.pareto_frontier) >= 2:
                pareto_idx = random.sample(xrange(len(self.pareto_frontier)), 2)
            can1 = self.pareto_frontier[pareto_idx[0]]
            can2 = self.pareto_frontier[pareto_idx[1]]
            #pick from frontier

            [crs1, crs2] = curr_pop.crossover(can1, can2)
            curr_pop.mutate(crs1)
            curr_pop.mutate(crs2)
            next_pop.candidates.append(crs1)
            next_pop.candidates.append(crs2)
        next_pop.ap_binary_dom()
        self.update_pareto(next_pop.pop_pareto)
        self.generations.append(next_pop)
        self.current_generation += 1
        return

    def statistics(self):
        curr_pop = self.generations[self.current_generation];
        best_fitness = sum(curr_pop.candidates[0].fitness)
        worst_fitness = sum(curr_pop.candidates[0].fitness)
        sum_fitness = 0
        for i in range(0, self.num_candidates):
            if(sum(curr_pop.candidates[i].fitness) < best_fitness):
                best_fitness = sum(curr_pop.candidates[i].fitness)
            if(sum(curr_pop.candidates[i].fitness) > worst_fitness):
                worst_fitness = sum(curr_pop.candidates[i].fitness)
            sum_fitness += sum(curr_pop.candidates[i].fitness)
        strStats = ""
        strStats += str(best_fitness) + ","
        strStats += str(worst_fitness) + ","
        strStats += str(sum_fitness / self.num_candidates)
        print strStats
        return

    def skdata(self):
        if self.current_generation % 100 != 99:
            return
        genStr = ""
        genStr += "gen" + str((self.current_generation+1)/100) + " "
        for pop in range(self.current_generation - 99, self.current_generation+1):
            curr_pop = self.generations[pop]
            for i in range(0, self.num_candidates):
                genStr += str(curr_pop.candidates[i].fitness[0]) + " "
        print genStr
        return

    def hvdata(self, hveCurr):
        hveCurr.add_data(self.generations[self.current_generation])
    
    def run(self):
        #self.initFile()
        self.randomize()
        #print 'Completed randomize'
        hveCurr = hve.HVE(self.num_candidates, self.num_generations)
        for i in range(0, self.num_generations):
            self.next()
            #print self.pareto_frontier
            self.hvdata(hveCurr)
            #self.writeToFile()
        hveCurr.pareto_last(self.pareto_frontier)
        return hveCurr
		


class Tuner_Model(Model):
    def __init__(self, lower=[0.01, 50, 100], upper = [0.2, 150, 1000], algo_model=dtlz.dtlz1, algo_num_obj=1, algo_num_decs=1):
        Model.__init__(self)
        #define upper and lower bounds for dec variables: Mutation rate, no of candidates and no of gens
        self.name = 'Tuner Model'
        self.lower_bounds = lower
        self.upper_bounds = upper
        self.no_of_decisions = len(lower)
        self.algo_model = algo_model
        self.algo_num_obj = algo_num_obj
        self.algo_num_decs = algo_num_decs
    def energy(self, s):
        ga = GA(self.algo_model, self.algo_num_obj, self.algo_num_decs, *s)
        hve1 = ga.run()
        return hve1.hyper_vol

def differential_evolution(model = Tuner_Model()):
        cr = 0.3
        f = 0.5
        kmax=3
        np = 15
        seed = model.get_decision()
        def mutate(these):
            sn=[]
            def smear(vals, idx):
                x1 = vals[0] + f*(vals[1]-vals[2])
                if x1 >= model.lower_bounds[idx] and x1<=model.upper_bounds[idx]:
                    return x1
                else:
                    return vals[random.randrange(0, len(vals)-1)]
            if cr < random.random():
                return these[0]
            for i in xrange(0,len(x)):
                sn = [smear(vals, i) for vals in zip(x,y,z)]
            return sn

        def create_frontier(seed):
            frontier = []
            frontier.append(seed)
            for i in xrange(1, np):
                frontier.append(model.get_decision())
            return frontier

        def generate_items(lst, avoid=None):
            def unique_item():
                x = avoid
                while id(x) in seen:
                  x = lst[  int(random.uniform(0,len(lst))) ]
                seen.append( id(x) )
                return x
            assert len(lst) > 4
            avoid = avoid or lst[0]
            seen  = [ id(avoid) ]
            return unique_item(), unique_item(), unique_item()
        frontier = create_frontier(seed)
        sb = seed
        eb = model.energy(seed)
        print eb
        print 'Best energy so far: '+str(eb)
        print 'Best solution so far: '+str(sb)
        no_change=0
        for k in xrange(kmax):
            for i,candidate in enumerate(frontier):
                e = model.energy(candidate)
                x, y, z = generate_items(frontier)
                sn = mutate((x,y,z)) #mutate function
                en = model.energy(sn)
                if en > e:
                    frontier[i] = sn
                if en > eb:
                    no_change=0
                    sb, eb = sn, en
                if eb > 0.999 and no_change > 10:
                    return sb
                print 'Best energy so far: '+str(eb)
                print 'Best solution so far: '+str(sb)
        return sb


def main():
    seed=[]
    models = [dtlz.dtlz1, dtlz.dtlz3, dtlz.dtlz5, dtlz.dtlz7]
    objs = [2, 4, 6, 8]
    decs = [10, 20, 40]
    lower = [0.01, 50, 500]
    upper = [0.5, 100, 1000]
    rdiv_ip=[]
    for model in models:
        for num_objs in objs:
            for num_decs in decs:
                run_name = model.__name__+' Objective '+str(num_objs)+' Decisions '+str(num_decs)
                print run_name
                tm = Tuner_Model(lower, upper, model, num_objs, num_decs)
                ga_params = differential_evolution(tm)
                tune = [run_name+'_t']
                untune = [run_name+'_u']
                for i in xrange(20):
                    ga_tuned = GA(model, num_objs, num_decs, *ga_params)
                    ga_untuned = GA(model, num_objs, num_decs, prob_mut=0.05, num_candidates=100, num_generations=100)
                    res_tuned = ga_tuned.run()
                    tune.append(res_tuned.hyper_vol)
                    res_untuned = ga_untuned.run()
                    untune.append(res_untuned.hyper_vol)
                rdiv_ip.append(tune)
                rdiv_ip.append(untune)
                print rdiv_ip
    rdivDemo(rdiv_ip)
if __name__ == "__main__":
    main()
