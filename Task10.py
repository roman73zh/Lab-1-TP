from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "X = " + str(self.x) + " Y = " + str(self.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        return Point(self.x * other, self.y * other)

    def __len__(self):
        return int(sqrt(self.x ** 2 + self.y ** 2))

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)


p1 = Point(1, 2)
p2 = Point(5, 6)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")
