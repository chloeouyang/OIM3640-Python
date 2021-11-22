class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        """
        return the representation of the object in a human-readable format
        """
        return f'(x: {self.x}, y:{self.y})'

    def __add__(self, another_point):
        """Operator Overloading
        Overloads the "+" operator
        """
        new_x = self.x + another_point.x
        new_y = self.y + another_point.y
        return Point(new_x, new_y)

    def __sub__(self, another):
        return Point(self.x - another.x, self.y - another.y)

    def __eq__(self, another):
        """In my definitation, two points are equal when the x's are equal"""
        return self.x == another.x

    def __gt__(self, another):
        return self.x > another.x 

    def __contains__(self, value):
        return value == self.x or value == self.y

p1 = Point(3, 4) # create a new object of Point 
# print(p1.x, p1.y)
print(p1)

p2 = Point(1, 2)
p3 = p1 + p2
print(p3)

print(p1 - p2)
p4 = Point(3, 3)
print(p1 == p4)

print(3 in p1)