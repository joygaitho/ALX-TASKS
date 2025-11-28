class Animal(): # parent class
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
""" multilevel inheritance """
class Prey(Animal): # parent class inheriting from another parent class
    def flee(self):
        print(f"{self.name} is fleeing")
class Predetor(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
# CHILD CLASSES
class Rabbit(Prey):
    pass
class Hawk(Predetor):
    pass
class Fish(Prey, Predetor):
    """ multiple inheritance. child class fish is inheriting form prey and predetor parent classes """
    pass
rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")
fish.eat()
