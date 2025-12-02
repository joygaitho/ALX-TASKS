class Animal:
    def eat(self):
        print("the animal is eating")
    def sleep(self):
        print("the animal is sleeping")
class Dog(Animal):
    def bark(self):
        print("the dog is barking")

a = Animal()
a.eat()
a.sleep()

d = Dog()
d.bark()
d.eat()
d.sleep()