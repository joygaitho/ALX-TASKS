class Student:

    count = 0 # class variable
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # increments count class by 1 evrytime a new instance is created
        Student.total_gpa += gpa

        # INSTANCE METHOD
    def get_info(self):
        return f"{self.name}, {self.gpa}"
    
    # CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa is: {cls.total_gpa / cls.count:,.2f}"
    
student1 = Student("Sadie", 4.2)
student2 = Student("Aubrey", 4.4)
print(student1.get_info())
print(student2.get_info())
print(Student.get_count())
print(Student.get_average_gpa())