import turtle

leo = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def multiple_degree_square(t, n, length, angle):
    for i in range(n):
        square(t, length)
        t.rt(angle)


multiple_degree_square(leo, 60, 100, 5)

turtle.mainloop()
