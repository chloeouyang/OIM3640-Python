# problem 1
# 1-1,12
# 1-2,24
# 1-3,36
# 1-4,48
# 1-5,60

# 2-1,12
# 2-2,12
# 2-3,12
# 2-4,12
# 2-5,12

# 3-1,5
# 3-2,4
# 3-3,12
# 3-4,1

# I get the numbers directly from cmd.exe without totally understanding them. Will you go over them on the next class?


def problem_1():
    number = 0
    i = 1
    while i < 11:
        number += i
        i += 1
    return number


# print(problem_1())


def problem_2():
    number = 0
    i = 1
    while i < 1001:
        number += i
        i += 1
    return number


# print(problem_2())


def problem_3(odd=True):
    number = 0
    i = 1
    while i < 1001:
        if odd:
            if i % 2 == 1:
                number += i
        else:
            if i % 2 == 0:
                number += i
        i + 1
    return number


print(problem_3(odd=True))
print(problem_3(odd=False))
# somehow this function can't run
