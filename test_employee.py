import unittest
from employee import Employee # import Employee class from employee module
class TestEmployee(unittest.TestCase):
    def test_email(self):
        """ create instances of Employee class """
        emp_1 = Employee("Mikey", "Ortega", 50000) 
        emp_2 = Employee("Melissa", "Merced", 60000)
        self.assertEqual(emp_1.email, 'Mikey.Ortega@email.com')
        self.assertEqual(emp_2.email, 'Melissa.Merced@email.com')
        emp_1.first = 'Jenna'
        emp_2.first = 'Isabela'
        self.assertEqual(emp_1.email, 'Jenna.Ortega@email.com')
        self.assertEqual(emp_2.email, 'Isabela.Merced@email.com')
    def test_fullname(self):
        """ create objects again because we can not access instances in email method since they are a sepreate namespace """
        emp_1 = Employee("Mikey", "Ortega", 50000) 
        emp_2 = Employee ("Melissa", "Merced", 60000)
        self.assertEqual(emp_1.full_name, 'Mikey Ortega')
        self.assertEqual(emp_2.full_name, 'Melissa Merced')
        emp_1.first = 'Jenna'
        emp_2.first = 'Isabela'
        self.assertEqual(emp_1.full_name, 'Jenna Ortega')
        self.assertEqual(emp_2.full_name, 'Isabela Merced')
    def test_applyraise(self):
        emp_1 = Employee("Mikey", "Ortega", 50000)
        emp_2 = Employee("Melissa", "Merced", 60000)
        emp_1.apply_raise()
        emp_2.apply_raise()
        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)
if __name__ == "__main__":
    unittest.main(exit=False)
