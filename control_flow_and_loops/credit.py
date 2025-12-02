high_income = False
good_credit = True
student = True
if (high_income or good_credit) and not student: # if condition is false
    print("eligible") # Runs when the if condition is True. It prints the string eligible.
else:
    print("not eligible") # Runs when the if condition is False. It prints not eligible.
# with and operator if both conditions are true then the result will be true in contrast with or operator as long as at least one conditions is true the result will be true
# not → reverses a boolean (not True → False, not False → True).