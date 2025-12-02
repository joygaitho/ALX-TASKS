rows = 5
i = 1 # row counter
while i <= rows: # It continues to run as long as the current row number i is less than or equal to the total number of rows (5). It controls moving from one row to the next.
    spaces = rows - i # calculte the number of spaces required for the current row (5-1=4)
    j = 1 #space counter 
    while j <= spaces:
        print(" ", end="")
        j += 1 #increment the number of spaces
    asterisks = 2 * i - 1 # calculates the number of asterisks in each.
    k = 1 #counter asterisks
    while k <= asterisks:
        print("*", end="")
        k += 1 #increment the number of asterisks
    print()
    i += 1 #increment the number of rows
