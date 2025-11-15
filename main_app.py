# main_app.py content
import my_helpers # import statements links my_helpers.py and main_app.py modules
# use the functions from the module
message = my_helpers.greet("isabela")
result = my_helpers.calculate_square(7)
print(message)
print(f"7 squared is: {result}")