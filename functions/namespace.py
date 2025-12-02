# 1. First function: Used for counting items
def item_counter(item_list):
    # 'count' variable exists only in the local namespace of item_counter
    count = 0
    for item in item_list:
        count += 1
    
    # Printing the local 'count'
    print(f"Inside item_counter: The list has a 'count' of {count} items.")

# 2. Second function: Used for logging events
def event_logger(message):
    # 'count' variable exists only in the local namespace of event_logger
    # Note: It is completely separate from the 'count' in the first function
    count = 1  # Using 'count' here to track the event ID or log line number
    
    # Printing the local 'count'
    print(f"Inside event_logger: Event ID '{count}' logged message: '{message}'")

# --- Function Calls ---
# Call the first function
data = ["Apple", "Banana", "Cherry", "Date"]
item_counter(data)

# Call the second function
event_logger("System startup successful.")