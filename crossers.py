import random


def blx_a_crosser(first, second):
    alfa = random.random()
    new_first = []
    new_second = []

    for i in range(len(first)):
        d = abs(first[i] - second[i])
        smaller = min(first[i], second[i])
        bigger = max(first[i], second[i])

        new_first.append(random.uniform(smaller - alfa * d, bigger + alfa * d))
        new_second.append(random.uniform(smaller - alfa * d, bigger + alfa * d))

    return new_first, new_second


def blx_a_b_crosser(first, second):
    alfa = random.random()
    beta = random.random()
    new_first = []
    new_second = []

    for i in range(len(first)):
        d = abs(first[i] - second[i])
        smaller = min(first[i], second[i])
        bigger = max(first[i], second[i])

        new_first.append(random.uniform(smaller - alfa * d, bigger + beta * d))
        new_second.append(random.uniform(smaller - alfa * d, bigger + beta * d))

    return new_first, new_second


def average_crosser(first, second):
    new_entity = []
    for i in range(len(first)):
        new_entity.append((first[i] + second[i]) / 2)

    return new_entity


def arithmetic_crosser(first, second):
    k = random.random()
    new_first = []
    new_second = []

    for i in range(len(first)):
        new_first.append(k * first[i] + (1 - k) * second[i])
        new_second.append(k * second[i] + (1 - k) * first[i])

    return new_first, new_second


