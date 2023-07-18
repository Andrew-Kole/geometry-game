import math
from random import randint
import turtle


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


class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


# class that gets left lower point and right upper point and draws rectangle
class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)


class GuiRectangle(Rectangle):

    def draw(self,canvas):
        # go to point1
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)
        # width and height
        width = self.upright.x - self.lowleft.x
        height = self.upright.y - self.lowleft.y
        # drawing rectangle
        canvas.pendown()
        canvas.forward(width)
        canvas.left(90)
        canvas.forward(height)
        canvas.left(90)
        canvas.forward(width)
        canvas.left(90)
        canvas.forward(height)


rectangle = GuiRectangle(Point(randint(0, 40), randint(0, 40)),
                      Point(randint(40, 80), randint(40, 80)))

print("Rectangle coordinates: ",
      rectangle.lowleft.x, ",",
      rectangle.lowleft.y, "and",
      rectangle.upright.x, ",",
      rectangle.upright.y)

user_point = GuiPoint(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

myTurtle = turtle.Turtle()
rectangle.draw(canvas=myTurtle)
user_point.draw(canvas=myTurtle)
turtle.done()
