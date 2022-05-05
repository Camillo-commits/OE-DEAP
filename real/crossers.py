import random

from real.fitness import get_fitness


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


def linear_crosser(first, second):
    z = []
    v = []
    w = []

    for i in range(len(first)):
        z.append(0.5 * (first[i] + second[i]))
        v.append(1.5 * (first[i] - 0.5 * second[i]))
        w.append(1.5 * (second[i] - 0.5 * first[i]))

    z_fit = get_fitness(z)
    v_fit = get_fitness(v)
    w_fit = get_fitness(w)

    minimal = min(min(z_fit, v_fit, w_fit))
    if z_fit == minimal:
        return v, w
    elif v_fit == minimal:
        return z, w
    elif w_fit == minimal:
        return z, v
