def problem_1():
    number = 0
    for i in range(1, 11):
        number += i
    return number


# print(problem_1())


def problem_2():
    number = 0
    for i in range(1, 1001):
        number += i
    return number


# print(problem_2())


def problem_3(odd=True):
    number = 0
    for i in range(1, 1001):
        if odd:
            if i % 2 == 1:
                number += i
        else:
            if i % 2 == 0:
                number += i
    return number


print(problem_3(odd=True))
print(problem_3(odd=False))
