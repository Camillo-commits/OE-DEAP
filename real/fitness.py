def get_fitness(entity):
    result = 0
    for i in range(len(entity)):
        result = result + entity[i]

    return result
