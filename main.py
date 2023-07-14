import math


# Class to define point
class Point:

    # Minimum parameters this class must have. x, y are coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method, that counts if given coordinates are in rectangle
    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.x < upright[1]:
            return True
        else:
            return False

    # Method, that counts distance from current coordinates to any other point
    def distance_from_point(self, point):
        return math.sqrt(math.pow(self.x - point.x, 2) + math.pow(self.y - point.y, 2))
