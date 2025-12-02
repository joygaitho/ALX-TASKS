class Employee:
    raise_amt = 1.05 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    @property # allows you to define a method in a class but access it like an attribute (a variable), without using parentheses (). eg emp.email
    def email(self):
        return f"{self.first}.{self.last}@email.com"
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)