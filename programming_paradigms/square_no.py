def square(x):
    """
    this is an intentional bug
    
    """
    #BUG: this should be x * x
    return x + x
print(square(5))