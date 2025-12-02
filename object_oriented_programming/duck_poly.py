class Dog:
    def make_sound(self):
        return "Woof! Woof!"

class Cat:
    def make_sound(self):
        return "Meow..."

class Bird:
    def make_sound(self):
        return "Chirp! Chirp!"

# The polymorphic function
def let_them_speak(animals):
    """
    This function accepts a list of objects.
    It doesn't care what class the object belongs to,
    only that it has a .make_sound() method.
    """
    print("--- The Animals are Speaking ---")
    for animal in animals:
        # Polymorphism in action: calling the same method name
        # results in different behaviors depending on the object.
        print(animal.make_sound())

# --- Main Execution ---

# 1. Create instances of the classes
dog = Dog()
cat = Cat()
bird = Bird()

# 2. Add them to a list
zoo = [dog, cat, bird]

# 3. Pass the list to the function
let_them_speak(zoo)