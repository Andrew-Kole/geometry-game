import math
from random import randint


# Class to define point
class Point:

    # Minimum parameters this class must have. x, y are coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method, that counts if given coordinates are in rectangle
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x\
                and rectangle.lowleft.y < self.x < rectangle.upright.y:
            return True
        else:
            return False

    # Method, that counts distance from current coordinates to any other point
    def distance_from_point(self, point):
        return math.sqrt(math.pow(self.x - point.x, 2) + math.pow(self.y - point.y, 2))


# class that gets left lower point and right upper point and draws rectangle
class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)


rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                      Point(randint(10, 19), randint(10, 19)))

print("Rectangle coordinates: ",
      rectangle.lowleft.x, ",",
      rectangle.lowleft.y, "and",
      rectangle.upright.x, ",",
      rectangle.upright.y)

user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)
