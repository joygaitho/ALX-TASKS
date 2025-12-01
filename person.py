class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"person object created for {self.name}, age {self.age}")
    def __del__(self):
        print(f"farewell! person object for {self.name} is being deleted")

p1 = Person("Jenna", 23)
del p1