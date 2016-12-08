from nsgaii import NSGAII

import dtlz

from models import MODEL

from hypervolume import *
from stats import rdivDemo as sk

def print_generation(population, generation_num):
    print("Generation: {}".format(generation_num))

models1 = [dtlz.dtlz1, dtlz.dtlz3, dtlz.dtlz5, dtlz.dtlz7]
print 'NSGAII RUNNING: agupta25'
for models in models1:
    for num_obj in [2, 4, 6, 8]:
        hv_stats = []
        run_stats = []
        for num_dec in [10, 20, 40]:
            for dom in ["bdom", "cdom"]:
                avg_vol = 0
                avg_runs = 0
                repeats = 20
                info_hv = [models.__name__ + " " + str(num_obj) + " " + str(num_dec) + " " + dom]
                info_runs = [models.__name__ + " " + str(num_obj) + " " + str(num_dec) + " " + dom]
                for x in range(repeats): #repeats
                    problem = MODEL(models, num_dec, num_obj, dom)

                    #Evolution(problem, max_iterations, pop_size)
                    nsga = NSGAII(problem, 100, 100, dom)

                    hypervolume, runs = nsga.run()

                    info_hv.append(hypervolume)
                    info_runs.append(runs)

                    avg_runs += runs
                hv_stats.append(info_hv)
                run_stats.append(info_runs)

        sk(hv_stats)
        sk(run_stats)
        print