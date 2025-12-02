class Shape:
    def calculate_area(self):
        return 0
    """ base method meant to be overriden """
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    """ overrides methods to compute rectangle area """
shape = Shape()
print("shape area is:", shape.calculate_area())
rect = Rectangle(20, 15)
print("area of rectangle is:", rect.calculate_area())