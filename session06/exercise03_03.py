import turtle

leo = turtle.Turtle()


# def triangle(t, length):
#     for i in range(3):
#         t.fd(length)
#         t.lt(120)


# def growth_triangle(t, n, length, growth, angle):
#     for i in range(n):
#         triangle(t, length + i * growth)
#         t.rt(angle)


# growth_triangle(leo, 60, 30, 4, 5)


def star(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def growth_degree_star(t, n, length, growth, angle):
    for i in range(n):
        star(t, 5, length + i * growth, 216)
        t.rt(angle)


growth_degree_star(leo, 60, 30, 4, 5)

turtle.mainloop()
