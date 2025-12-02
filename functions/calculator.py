def add(num1, num2):
    """
    returns the sum of two numbers

    """
    return num1 + num2
def subtract(num1, num2):
    """
    returns the difference of two numbers
    
    """
    return num1 - num2
def multiply(num1, num2):
    """
    returns the product of two numbers
    
    """
    return num1 * num2
def divide(num1, num2):
    """
    returns the quotient of two numbers
    handles division by zero error

    """
    if num2 == 0:
        return f"cannot divide by zero."
    return num1 / num2