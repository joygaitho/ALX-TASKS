# polymorphism means: many forms - the same method name works differently depending on the object


from abc import ABC, abstractmethod

class Shape(ABC):
   """ What is an abstract method?

A method that has no implementation in the base class.
It is only a requirement for subclasses. Meaning 'every child class must provide it's own version of this method' """
   @abstractmethod 
   def area(self): 
       pass
   
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2 # implement the area method
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 1/2 * self.base * self.height

class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings

shapes = [Circle(3.5), Square(9), Triangle(4, 8), Pizza("pepperoni", 7)] # classes are already instantiated inside the list. this is done to demostrate polymorphism
for shape in shapes:
    print(f"{shape.area()}cm²")
# The loop does not care what type each object is. It simply calls .area() on each one. Python automatically picks the correct version of area()

# SUMMARY
# pizza has three forms, our pizza is considered a pizza, it also considered a circle and it is also considered a shape.
# it will make sense for it to fit in the list of shapes[] because it identifies as a shape!