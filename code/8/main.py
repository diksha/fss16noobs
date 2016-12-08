from nsgaii import NSGAII

import dtlz

from init import MODEL

from hypervolume import *
from stats import rdivDemo as stat

def print_generation(population, generation_num):
    print("Generation: {}".format(generation_num))

models1 = [dtlz.dtlz1, dtlz.dtlz3, dtlz.dtlz5, dtlz.dtlz7]
print 'NSGAII RUNNING: agupta25'
for models in models1:
    for num_obj in [2, 4, 6, 8]:
        hvol = []
        repeat = []
        for num_dec in [10, 20, 40]:
            for dom in ["bdom", "cdom"]:
                vol = 0
                rep = 0
                repeats = 20
                hvDisplay = [models.__name__ + " " + str(num_obj) + " " + str(num_dec) + " " + dom]
                runsDisplay = [models.__name__ + " " + str(num_obj) + " " + str(num_dec) + " " + dom]
		print hvDisplay
                for x in range(repeats): #repeats
                    problem = MODEL(models, num_dec, num_obj, dom)
		    print 'Model defined entering nsgaii'

                    #Evolution(problem, max_iterations, pop_size)
                    nsga = NSGAII(problem, 100, 100, dom)

                    hypervolume, runs = nsga.run()
		    print 'Printing hypervolume'
		    print hypervolume
		    print runs

                    hvDisplay.append(hypervolume)
                    runsDisplay.append(runs)

                    rep += runs
                hvol.append(info_hv)
                run_stats.append(info_runs)
		print hvDisplay
		print runsDisplay

        stat(hvol)
        stat(repeat)
        print
