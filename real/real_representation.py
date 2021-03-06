from deap import base
from deap import creator
from deap import tools
from numpy import random

from real.fitness import get_fitness


def individual(icls):
    genome = list()
    genome.append(random.uniform(-10, 10))
    genome.append(random.uniform(-10, 10))

    return icls(genome)


def solve_real_representation(is_min, selector, crosser, mutator, size_population, probability_mutation,
                probability_crossover,
                number_iteration, number_elitism):
    if is_min:
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

    else:
        creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register('individual', individual, creator.Individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", get_fitness)
    toolbox.register("select", selector, tournsize=3)
    toolbox.register("mate", crosser, alpha = 0.5)
    toolbox.register("mutate", mutator, mu = 5, sigma=10, indpb=probability_mutation)

    pop = toolbox.population(n=size_population)
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    x1_list = []
    x2_list = []
    y_list = []
    std_list = []
    avg_list = []
    g = 0
    while g < number_iteration:
        g = g + 1
        print("-- Generation %i --" % g)
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        listElitism = []
        for x in range(0, number_elitism):
            listElitism.append(tools.selBest(pop, 1)[0])

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            # cross two individuals with probability CXPB
            if random.random() < probability_crossover:
                toolbox.mate(child1, child2)
                # fitness values of the children
                # must be recalculated later
                del child1.fitness.values
                del child2.fitness.values
        for mutant in offspring:
            # mutate an individual with probability MUTPB
            if random.random() < probability_mutation:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        print(" Evaluated %i individuals" % len(invalid_ind))
        pop[:] = offspring + listElitism
        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5
        print(" Min %s" % min(fits))
        print(" Max %s" % max(fits))
        print(" Avg %s" % mean)
        print(" Std %s" % std)
        best_ind = tools.selBest(pop, 1)[0]
        print("Best individual is %s, %s" % (best_ind,
                                             best_ind.fitness.values))
        x1_list.append(best_ind[0])
        x2_list.append(best_ind[1])
        y_list.append(best_ind.fitness.values[0])
        std_list.append(std)
        avg_list.append(mean)
    #
    print("-- End of (successful) evolution --")
    return x1_list, x2_list, y_list, std_list, avg_list

