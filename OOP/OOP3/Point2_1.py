class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        """return a Point object in a human-readable format"""
        return f'({self.x}, {self.y})'

    def __add__(self, another_point):
        """Operator Overloading
        
        Overloads the "+" operator
        """
        new_x = self.x + another_point.x
        new_y = self.y + another_point.y
        return Point(new_x, new_y)


    def __sub__(self, another_point):
        """Operator Overloading
        
        Overloads the "-" operator
        """
        new_x = self.x - another_point.x
        new_y = self.y - another_point.y
        return Point(new_x, new_y)

    def __eq__(self, another_point):
        return self.x == another_point.x
    
    def __gt__(self, another_point):
        """Overloads ">" operator """
        return self.x > another_point.x and self.y > another_point.y

    def __contains__(self, value):
        return value == self.x or value == self.y


p1 = Point(3, 4)
# print(p1.x, p1.y)
print(p1)

p2 = Point(5, 5)
print(p2)

# new_point = p1.__add__(p2)
new_point = p1 + p2
print(new_point)
print(p2 - p1)

p3 = Point(3, 3)
print(p2 == p1)
print(p3 == p1)
print(p2 > p1)

print(3 in p1)