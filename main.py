import numpy
from deap import tools
from binary.binary_representation import solve_binary_representation
from real.real_representation import solve_real_representation
import matplotlib.pyplot as plt
from utils import plot3d, plotStdAvg

is_min = True
selector = tools.selTournament
crosser = tools.cxOnePoint
mutator = tools.mutShuffleIndexes
size_of_population = 10
probability_mutation = 0.3
probability_crossover = 0.5
number_iteration = 100
number_elitism = 1
x1, x2, y, std, avg = solve_binary_representation(is_min, selector, crosser, mutator, size_of_population, probability_mutation,
                            probability_crossover, number_iteration, number_elitism)
print("Done!")
plot3d(x1, x2, y, colorbar=True)
plotStdAvg(std,avg)

is_min = True
selector = tools.selTournament
crosser = tools.cxBlend
mutator = tools.mutGaussian
size_of_population = 10
probability_mutation = 0.3
probability_crossover = 0.5
number_iteration = 100
number_elitism = 1
x1, x2, y, std, avg = solve_real_representation(is_min, selector, crosser, mutator, size_of_population, probability_mutation,
                                      probability_crossover, number_iteration, number_elitism)
print("Done!")
plot3d(x1, x2, y, colorbar=True)
plotStdAvg(std,avg)