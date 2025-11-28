class Animal:
    Kingdom = 'Animalia' # class variable
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is alseep")
class Dog(Animal):
    def speak(self):
        print("WOOF! WOOF!")
class Cat(Animal):
    def speak(self):
        print("MEOW!")
class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog('Scooby', True)
cat = Cat('Garfield', True)
mouse = Mouse('Mickey', True)
dog.speak()
dog.sleep()