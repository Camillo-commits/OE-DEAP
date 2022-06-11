def get_fitness(individual):
    result = ((individual[0] + 2 * individual[1] - 7) ** 2 + (2 * individual[0] + individual[1] - 5) ** 2,)
    return result

def get_fitness2(individual):
    result = ((individual[0] + 2 * individual[1] - 7) ** 2 + (2 * individual[0] + individual[1] - 5) ** 2)
    return result