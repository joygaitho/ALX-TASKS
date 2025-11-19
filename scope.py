# 1. Global Scope (G)
# This variable is available everywhere.
location = "Mars (Global Scope)"

def outer_function():
    # 2. Enclosing Scope (E)
    # This variable is "enclosing" for any function defined *inside* outer_function.
    location = "Jupiter (Enclosing Scope)"
    
    def inner_function():
        # 3. Local Scope (L)
        # This function has no 'location' defined locally, so it must search outwards.
        
        # --- Lookup Process (LEGB Rule) ---
        
        # Accessing the Enclosing Variable:
        # Python looks in Local (L) -> Not found.
        # Python looks in Enclosing (E) -> Found 'Jupiter (Enclosing Scope)'.
        print(f"Inside inner_function (Enclosing Scope): {location}")
        
        # Accessing the Global Variable:
        # We must use the 'global' keyword to explicitly skip Enclosing (E)
        # and retrieve the variable from the Global (G) scope.
        global location
        print(f"Inside inner_function (Global Scope): {location}")

    # Call the inner function to execute the lookup logic
    inner_function()
    
    # Printing from the Outer/Enclosing Scope to show its value is preserved
    print(f"Inside outer_function (Enclosing Scope): {location}")

# Call the outer function to start the demonstration
outer_function()

# 4. Printing from the Global Scope (G)
# This confirms the global variable was not changed by the enclosing definition.
print(f"Outside all functions (Global Scope): {location}")