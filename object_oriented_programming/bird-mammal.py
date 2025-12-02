class Bird:
    def fly(self):
        print("this bird is flying.")
class Mammal:
    def run(self):
        print("this mammal is running.")
class Bat(Bird, Mammal):
    def fly(self):
        print("the bat is flying using wings.")
    def run(self):
        print("the bat can run but not as fast as other mammals.")
bat = Bat()
bat.fly() # uses Bat's version
bat.run() # uses Bat's version