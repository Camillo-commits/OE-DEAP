import random


def blx_a_crosser(first, second):
    alfa = random.random()
    d = abs(first - second)
    smaller = min(first, second)
    bigger = max(first, second)

    new_first = random.uniform(smaller - alfa * d, bigger + alfa * d)
    new_second = random.uniform(smaller - alfa * d, bigger + alfa * d)

    return new_first, new_second


def blx_a_b_crosser(first, second):
    alfa = random.random()
    beta = random.random()
    d = abs(first - second)
    smaller = min(first, second)
    bigger = max(first, second)

    new_first = random.uniform(smaller - alfa * d, bigger + beta * d)
    new_second = random.uniform(smaller - alfa * d, bigger + beta * d)

    return new_first, new_second

