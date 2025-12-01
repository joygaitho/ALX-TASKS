# super() = Function used in a child class to call methods from a parent class(superclass)
# allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled
        """ extend the functionality the inherited methods """
    def describe(self):
        print(f"it is {self.colour} and {'filled' if self.is_filled else 'not filled'}") # ternary expression exists to let you choose between two values in a single, compact expression, instead of writing a full if/else block.
class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled) # calls super class' constructor
        self.radius = radius
    def describe(self): # function overriding; when a child class shares a similar method with the parent class
        super().describe()
        print(f"the area of this circle is: {3.14 * self.radius ** 2} cm^2") 
class Square(Shape):
    def __init__(self, colour, is_filled, length):
        super().__init__(colour, is_filled)
        self.length = length
    def describe(self):
        super().describe()
        print(f"the are of this square is: {self.length * self.length} cm^2") 
class Triangle(Shape):
    def __init__(self, colour, is_filled, base, height):
        super().__init__(colour, is_filled)
        self.base = base
        self.height = height
    def describe(self):
        super().describe()
        print(f"the are of this triangle is: {1/2 * self.base * self.height} cm^2") 
circle = Circle("red", True, 7)
square = Square("blue", True, 10)
triangle = Triangle("green", False, 12, 6)
circle.describe() # prints both statements from class Shape and Circle after adding super().describe()
square.describe()
triangle.describe()