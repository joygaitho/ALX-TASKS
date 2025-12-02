city = "new york" # global

def change_city(): # local
    global city # modify city global var 
    city = "london"
    print(f"inside function local scope: {city}")
change_city()
print(f"outside function global scope: {city}") #output will be london instead of new york