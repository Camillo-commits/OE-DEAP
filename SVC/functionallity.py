import random

from deap import base
from deap import creator
from deap import tools
# from deap.benchmarks import tools
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC


def SVCparameters(numberOfFeatures, icls):
    genome = list()

    # kernel
    listKernel = ["linear", "rbf", "poly", "sigmoid"]
    genome.append(listKernel[random.randint(0, 3)])

    # c
    k = random.uniform(0.1, 100)
    genome.append(k)

    # degree
    genome.append(random.uniform(0.1, 5))

    # gamma
    gamma = random.uniform(0.001, 5)
    genome.append(gamma)

    # coeff
    coeff = random.uniform(0.01, 10)
    genome.append(coeff)

    return icls(genome)


def SVCParametersFitness(y, df, numberOfAtr, individual):
    split = 5
    cv = StratifiedKFold(n_splits=split)
    mms = MinMaxScaler()
    df_norm = mms.fit_transform(df)
    if individual[2] < 0:
        individual[2] = 0.1
    estimator = SVC(kernel=individual[0], C=individual[1], degree=individual[2], gamma=individual[3],
                    coef0=individual[4], random_state=101)
    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        tn, fp, fn, tp = metrics.confusion_matrix(expected, predicted).ravel()
        result = (tp + tn) / (tp + fp + tn + fn)
        resultSum = resultSum + result
    return resultSum / split,


def mutationSVC(individual):
    numberParamer = random.randint(0, len(individual) - 1)
    if numberParamer == 0:
        # kernel
        listKernel = ["linear", "rbf", "poly", "sigmoid"]
        individual[0] = listKernel[random.randint(0, 3)]
    elif numberParamer == 1:
        # C
        k = random.uniform(0.1, 100)
        individual[1] = k
    elif numberParamer == 2:
        # degree
        individual[2] = random.uniform(0.1, 5)
    elif numberParamer == 3:
        # gamma
        gamma = random.uniform(0.01, 5)
        individual[3] = gamma
    elif numberParamer == 4:
        # coeff
        coeff = random.uniform(0.1, 20)
        individual[2] = coeff


###   SELEKCJA CECH   ###
def SVCParametersFeatures(numberFeatures, icls):
    genome = list()
    # kernel
    listKernel = ["linear", "rbf", "poly", "sigmoid"]
    genome.append(listKernel[random.randint(0, 3)])
    # c
    k = random.uniform(0.1, 100)
    genome.append(k)
    # degree
    genome.append(random.uniform(0.1, 5))
    # gamma
    gamma = random.uniform(0.001, 5)
    genome.append(gamma)
    # coeff
    coeff = random.uniform(0.01, 10)
    genome.append(coeff)
    for i in range(0, numberFeatures):
        genome.append(random.randint(0, 1))
    return icls(genome)


def SVCParametersFeatureFitness(y, df, numberOfAtributtes, individual):
    split = 5
    cv = StratifiedKFold(n_splits=split)

    listColumnsToDrop = []  # lista cech do usuniecia
    for i in range(numberOfAtributtes, len(individual)):
        if individual[i] == 0:  # gdy atrybut ma zero to usuwamy cechę
            listColumnsToDrop.append(i - numberOfAtributtes)

    dfSelectedFeatures = df.drop(df.columns[listColumnsToDrop], axis=1, inplace=False)

    mms = MinMaxScaler()
    df_norm = mms.fit_transform(dfSelectedFeatures)
    estimator = SVC(kernel=individual[0], C=individual[1],degree=individual[2],gamma=individual[3],
                    coef0=individual[4],random_state=101)
    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        tn, fp, fn, tp = metrics.confusion_matrix(expected, predicted).ravel()
        result = (tp + tn) / (tp + fp + tn + fn)
        resultSum = resultSum + result
    return resultSum / split,


def mutationSVCWithSelection(individual):
    numberParamer = random.randint(0, len(individual) - 1)
    if numberParamer == 0:
        # kernel
        listKernel = ["linear", "rbf", "poly", "sigmoid"]
        individual[0] = listKernel[random.randint(0, 3)]
    elif numberParamer == 1:
        # C
        k = random.uniform(0.1, 100)
        individual[1] = k
    elif numberParamer == 2:
        # degree
        individual[2] = random.uniform(0.1, 5)
    elif numberParamer == 3:
        # gamma
        gamma = random.uniform(0.01, 5)
        individual[3] = gamma
    elif numberParamer == 4:
        # coeff
        coeff = random.uniform(0.1, 20)
        individual[2] = coeff
    else:  # genetyczna selekcja cech
        if individual[numberParamer] == 0:
            individual[numberParamer] = 1
        else:
            individual[numberParamer] = 0

#############


def solve(is_min, selector, crosser, mutator, size_population, probability_mutation,
          probability_crossover,
          number_iteration, number_elitism, numberOfAttr, y, df, evaluate, individual):
    if is_min:
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

    else:
        creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register('individual', individual, numberOfAttr, creator.Individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evaluate, y, df, numberOfAttr)
    toolbox.register("select", selector, tournsize=3)
    toolbox.register("mate", crosser, alpha=0.5)
    toolbox.register("mutate", mutator)  # , mu=5, sigma=10, indpb=probability_mutation)

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
