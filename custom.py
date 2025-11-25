class ValueTooHighError(Exception):
    """
    this pass statement:
    It’s a placeholder.
    It tells Python the class exists but has no additional content.
    It keeps the class syntactically valid (Python doesn’t allow an empty class body).

    """
    pass 
def val_too_high():
    try:
        number = int(input("Enter a number not exceeding 100: "))
        if number > 100:
            raise ValueTooHighError("This number is too high!")
        print(f"number is: {number}")
    except ValueTooHighError as e:
        print(e)
    except ValueError as e:
        print(e)
val_too_high()