def zero_div_error():
    try:
        num1 = int(input("enter a number: "))
        num2 = int(input("enter another number: "))
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = num1 / num2
        print(result)
    except ZeroDivisionError as e:
        print(e)
    except ValueError:
        print("Error: please enter an integer")
zero_div_error()