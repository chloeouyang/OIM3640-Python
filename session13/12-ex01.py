def sumall(*args):
    accumulate = 0
    for arg in args:
        accumulate += arg
    return accumulate


t = (1, 3, 5)
print(sumall(*t))