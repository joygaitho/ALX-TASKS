marks = int(input("enter your marks:")) 
result = ""
if marks <= 30:
   result = "Failed"
elif marks >= 75:
   result = "Passed with distinction"
else:
   result = "Passed"

print(result)