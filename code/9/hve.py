import random

class Result:
    def __init__(self, hyper_vol, spread):
        self.hyper_vol = hyper_vol
        self.spread = spread

class HVE:
    def __init__(self, num_cans, num_gen):
        self.generations = []
        self.hyper_vol=0
        self.spread=[]
        self.num_candidates=num_cans
        self.num_generations=num_gen

    def add_data(self, generation):
        self.generations.append(generation)
    
    def pareto_last(self, pf):
        fron_cans = pf
        num_cans = self.num_candidates*self.num_generations
        if len(pf) == 0:
            return Result(1, [])
        spread = []
        for i in range(0, len(fron_cans[0].fitness)):
            fsorted = sorted(fron_cans, lambda x,y: x.fitness[i] < y.fitness[i])
            p25 = fsorted[len(fsorted)/4]
            p75 = fsorted[3*len(fsorted)/4]
            spread.append(abs(p75.fitness[i]-p25.fitness[i]))
        self.spread=spread
        self.hyper_vol = (num_cans-len(fron_cans))/float(num_cans)
        res = Result(self.hyper_vol, self.spread)
        return res