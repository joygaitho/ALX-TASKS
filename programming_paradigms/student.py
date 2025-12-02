class Student: #class definition
    def __init__(self, name, age, year): #constructor definition
        self.name = name # object/instance attribute definition and initialization
        self.age = age # object/instance attribute definition and initialization
        self.year = year # object/instance attribute definition and initialization
    def display_info(self): # instance method
        print(f"my name is {self.name}, i am {self.age} years old and i am in year {self.year}")
stud = Student("isabela", 24, 4) #object created automatically invokes the init constructor
print("\n display details for stud")
print("-" * 20)
stud.display_info() # function call
stud1 = Student("jenna", 22, 3)
print("\n display details of stud2")
print("_" * 20)
stud1.display_info()