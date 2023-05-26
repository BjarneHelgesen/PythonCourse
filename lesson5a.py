import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass

class Circle(Shape): 
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        return math.pi*self.radius*self.radius
    
    def circumference(self):
        return 2*math.pi*self.radius

class Square(Shape):
    def __init__(self, center_x, center_y, side_length): 
        self.center_x = center_x
        self.center_y = center_y
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

    def circumference(self):
        return 4 * self.side_length

def distance(a, b):
    """Returns the center distance between a and b"""
    x_diff = a.center_x - b.center_x
    y_diff = a.center_y - b.center_y
    return math.sqrt(x_diff*x_diff + y_diff*y_diff)     

square1 = Square(10, 20, 24)
circle1 = Circle(2, 23, 10)
print(distance(circle1, square1))
print("Circle 1 area", circle1.area())
print("Circle 1 circumference", circle1.circumference())
