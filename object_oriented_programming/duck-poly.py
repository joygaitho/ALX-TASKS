# 'duck typing' = another way to achieve polymorphism besides inheritance
# objects must have the mininum necessary attriutes/methods
# "if it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True #class variable
class Dog(Animal):
    def speak(self):
        print("WOOF! WOOF!")
class Cat(Animal):
    def speak(self):
        print("MEOW! HISS!")
class Car:
    alive = False
    def speak(self):
        print("HONK! HONK!")
animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)