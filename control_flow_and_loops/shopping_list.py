shopping_list = ["apples", "bread", "milk", "cheese"]

while True: # The purpose of while True in programming, particularly in Python, is to create an infinite loop. It causes a block of code to repeat indefinitely until a specific condition is met inside the loop that explicitly forces it to stop.
  item = input("Search for an item in your list (or 'q' to quit): ")
  if item.lower() == "q":
    break  # Exit the loop if user enters 'q'
  if item in shopping_list:
    print(f"{item} is on your shopping list.")
  else:
    print(f"{item} is not on your list.")