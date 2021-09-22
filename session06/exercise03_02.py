import turtle

leo = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def growth_degree_square(t, n, length, growth, angle):
    for i in range(n):
        square(t, length + i * growth)
        t.rt(angle)


growth_degree_square(leo, 60, 30, 4, 5)
turtle.mainloop()
