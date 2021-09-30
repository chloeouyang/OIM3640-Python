import random


def sum():
    c = 0
    for i in range(100):
        a = random.randint(1, 6)
        c += a
    return c


print(sum())


def total(m):
    d = []
    for i in range(m):
        d.append(sum())
    return d


print(total(10))


# function1: do one simulation


# function2: repeat simulation 10 times
