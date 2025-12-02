# abstract class: A class that cannot be instatiated (ie we can not create objects of that class() on it's own; meant to be subclassed

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    """ we are able to instantiate class Car because we have defined abstract methods go and stop """
    def go(self):
        print("you drive the car")
    def stop(self):
        print("you stop the car")
    pass
car = Car()
car.go()
car.stop()
class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")
    def stop(self):
        print("you stop the motorcycle")
bike = Motorcycle()
bike.go()
bike.stop()
class Boat(Vehicle):
    def go(self):
        print("you sail the boat")
    def stop(self):
        print("you anchor the boat")
boat = Boat()
boat.go()
boat.stop()