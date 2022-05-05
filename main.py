from deap import tools
from binary.binary_representation import solve_binary_representation


is_min = True
selector = tools.selTournament
crosser = tools.cxOnePoint
mutator = tools.mutShuffleIndexes
size_of_population = 10
probability_mutation = 0.3
probability_crossover = 0.5
number_iteration = 10
number_elitism = 1
solve_binary_representation(is_min, selector, crosser, mutator, size_of_population, probability_mutation,
            probability_crossover, number_iteration, number_elitism)
print("Done!")
