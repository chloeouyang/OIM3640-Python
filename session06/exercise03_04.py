import turtle

leo = turtle.Turtle()


def triangle(t, length):
    for i in range(3):
        t.fd(length)
        t.lt(120)


def growth_triangle(t, n, length, growth, angle):
    for i in range(n):
        triangle(t, length + i * growth)
        t.rt(angle)


growth_triangle(leo, 60, 30, 4, 5)

turtle.mainloop()
