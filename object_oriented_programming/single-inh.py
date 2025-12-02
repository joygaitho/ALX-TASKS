from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod 
    def calculate_area(self):
        pass
    """ base method meant to be overriden """
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    """ overrides methods to compute rectangle area """
rect = Rectangle(20, 15)
print("area of rectangle is:", rect.calculate_area())