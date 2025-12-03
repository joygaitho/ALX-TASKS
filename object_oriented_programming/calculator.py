class Calculator:
    
    @staticmethod
    def add(x, y):
        print(f"add {x} and {y}....")
        return x + y
    
    @staticmethod
    def multiply(x, y):
        print(f"multiply {x} and {y}...")
        return x * y

#  Calling Static Methods via the Class (Recommended)
print("--- Calling Methods via the Class Name ---")

print("The sum is:", Calculator.add(10,15)) 
print("^" * 30)

print("The product is:", Calculator.multiply(4, 9))