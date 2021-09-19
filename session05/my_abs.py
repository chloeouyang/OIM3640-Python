def absolute(number):
    if number >= 0:
        print(number)
    else:
        print(-number)


absolute(182)
absolute(-999)


def my_abs(number):
    if number < 0:
        return -number
    else:
        return number


print(my_abs(777))


def my_abs_filter(whatever):
    if isinstance(whatever, (int, float)) == True:
        return abs(whatever)
    else:
        print("It is not integer or float.")


print(my_abs_filter(-237.748))
print(my_abs_filter("chloe"))


# import math
# def move(x, y, step, angle):
#   nx = x + step * math.cos(angle)
#   ny = y - step * math.sin(angle)
#  return nx, ny

# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

import math


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2


x11, x22 = quadratic(1, 1, -2)
print(x11, x22)
print(quadratic(1, 1, -2))
