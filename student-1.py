class Student:
    """ class variable definition """
    class_year = 2024
    num_students = 0 # student count
    def __init__(self, full_name, age):
        """ instance attributes definition and initialization """
        self.full_name = full_name
        self.age = age
        Student.num_students += 1 # modifying class variable
# create objects for class Student
student_1 = Student("Jenna Ortega", 23)
student_2 = Student("Isabel Merced", 24)
student_3 = Student("Mikey Maddison", 26)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students namely: ") # accessing class variables
# access the object attributes
print(student_1.full_name, student_1.age, student_1.class_year)
print("-" * 20)
print(student_2.full_name, student_2.age, Student.class_year) # we can also access class variables directly by the name of the class
print("-" *20)
print(student_3.full_name, student_3.age, Student.class_year)
print(f"Hi, i am {student_1.full_name}, class of {Student.class_year}")
print(f"Hi, i am {student_2.full_name}, class of {Student.class_year}")
print(f"Hi, i am {student_3.full_name}, class of {Student.class_year}")