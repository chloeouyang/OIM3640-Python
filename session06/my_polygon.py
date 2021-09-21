import turtle
import math

leo = turtle.Turtle()
print(leo)
# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)

# for i in range(4):
#     leo.fd(100)
#     leo.lt(90)

# 1.


def square(t):
    """this function takes a parameter named t, which is a turtle. It should use the turtle to draw a square."""
    for i in range(4):
        t.fd(100)
        t.lt(90)


# square(leo)

chloe = turtle.Turtle()
# square(chloe)

# 2.


def square(t, length):
    """this function takes a parameter named t, which is a turtle, and another parameter length, which is float. It should use the turtle to draw a square."""
    for i in range(4):
        t.fd(length)
        t.lt(90)


# square(chloe,500)

# 3.


def polygon(t, length, n):
    """draws an n-sided regular polygon"""
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


# polygon(t=chloe, length=100, n=5)

# 4.
def circle(t, r):
    """draws a approximate circle"""
    # import math
    circumference = 2 * math.pi * r
    length = circumference / 50
    polygon(t, length, 50)


# circle(leo, 200)

# 5.
def arc(t, r, angle):
    """draws an arc with angle"""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


# arc(leo, 200, 90)

# the process of refactoring


def polyline(t, n, length, angle):
    """draws n line segments with given length and angle (in degrees) between them. t is a turtle."""
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# polyline(leo, n=3, length=100, angle=90)


def polygon(t, length, n):
    """draws a n-sided polygon with given length. t is a turtle."""
    angle = 360 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """draws an arc with angle"""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    """draws a approximate circle"""
    arc(t, r, 360)


turtle.mainloop()
