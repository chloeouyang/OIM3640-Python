import turtle

leo = turtle.Turtle()


def archimedean_spiral(t, n, length, growth, angle):
    for i in range(n):
        t.fd(length + i * growth)
        t.lt(angle)


archimedean_spiral(leo, 500, 1, 0.1, 5)

turtle.mainloop()
