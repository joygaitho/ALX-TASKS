# Mad Libs Story Generator with Conditional Twists

print("Welcome to the Mad Libs Story Generator!")
print("Please provide the words as prompted below.\n")

# Step 1: Prompt the user for words
adjective1 = input("Enter an adjective (e.g., sunny, bright): ")
adjective2 = input("Enter another adjective (e.g., funny, lazy): ")
adjective3 = input("Enter one more adjective (e.g., majestic, fierce): ")
adjective4 = input("Enter a final adjective (e.g., wild, exciting): ")
animal1 = input("Enter an animal (e.g., monkey, elephant): ")
animal2 = input("Enter another animal (e.g., lion, tiger): ")
verb = input("Enter a verb (e.g., run, jump, sleep): ")

# Step 2: Conditional variations based on user input
if adjective1.lower() in ["rainy", "stormy", "cloudy"]:
    weather_comment = "Even though the weather wasn't perfect, the adventure was unforgettable!"
else:
    weather_comment = "The weather made everything feel magical and full of life!"

if animal1.lower() == "monkey":
    monkey_action = "swinging from tree to tree like a gymnast!"
else:
    monkey_action = f"doing some {verb} moves that made everyone laugh!"

if adjective4.lower() in ["boring", "dull"]:
    ending = "Maybe next time will be more exciting!"
else:
    ending = "What a wild and unforgettable experience!"

# Step 3: Build the story
story = f"""
On a beautiful {adjective1} day, I went to the zoo. 
I saw a {adjective2} {animal1} {monkey_action} 
Then, I spotted a {adjective3} {animal2} lounging in the sun. 
{weather_comment} {ending}
"""
# Step 4: Display the final story
print("\n--- Your Mad Libs Story ---")
print(story)
