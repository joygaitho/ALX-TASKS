# main_app.py content
import my_helpers # import statements help us access functions defined in my_helpers.py module
# use the functions from the module
message = my_helpers.greet("isabela") # this is a standard way in python to call a function that has been imported from a module
result = my_helpers.calculate_square(7)
print(message)
print(f"7 squared is: {result}")