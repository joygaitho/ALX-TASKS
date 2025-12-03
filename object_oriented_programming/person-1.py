# class methods = When you want to create factory methods to create instances of the class with specific configurations.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name} Age: {self.age})"
    
    @classmethod
    def create_child(cls, name):
        """
        Factory class method to create a specialized instance of Person 
        where age is automatically set to 0 (a child/newborn).

        The 'cls' parameter refers to the class itself (Person).
        """
        # Call the standard constructor (__init__) using 'cls'
        return cls(name, age=0)

child = Person.create_child("Bubba")
print(f"factory instance {child}") # When the print() function receives an object, it checks if that object has a __str__
# method. If it does, print() calls this method and outputs the string it returns.