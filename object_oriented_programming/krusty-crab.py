# Static methods = A method that belong to a class rather than any object from that class
#                = usually used for general utility functions
# Instance methods = best for operations on instances of the class (objects)
# Static methods = best for utility functions that do not need access to class data


class Employee:

    def __init__(self, full_name, position):
        self.name = full_name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugene Krabs", "Manager")
employee2 = Employee("Squidward Tentacles", "Cashier")
employee3 = Employee("Spongebob SquarePants", "Cook")
employee4 = Employee("Patrick Star", "Janitor")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())

print(Employee.is_valid_position("Cook")) # use the class to call the function