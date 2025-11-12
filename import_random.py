import random

def play_game():
    """Generates a secret number and runs the guessing game."""
    # Generate a secret number between 1 and 10
    secret_number = random.randint(1, 10)
    
    print("\nI'm thinking of a number between 1 and 10. Can you guess it?")
    
    # Initialize the guess counter
    guess_count = 0
    
    # Start the loop so the user can guess multiple times
    while True:
        try:
            # Get user input and convert to an integer
            guess_str = input("Enter your guess: ").strip()
            
            # Check for empty input
            if not guess_str:
                print("Please enter a number.")
                continue
                
            guess = int(guess_str)
            guess_count += 1 # increments the guess by 1
            
            # Calculate the difference between the secret and the guess
            # This allows us to use match/case effectively for conditional checks
            difference = guess - secret_number
            
            # --- Match Case Logic ---
            # The 'case' statements check the calculated difference:
            match difference:
                # Case 1: Difference is 0 (Guess is correct)
                case 0:
                    print(f"🎉 Congratulations, you guessed it! The number was {secret_number}.")
                    print(f"It took you **{guess_count}** guesses to win.")
                    break # Exit the game loop
                
                # Case 2: Difference is positive (Guess is too high)
                case _ if difference > 0:
                    print("⬇️ Oops, your guess is a bit **high**. Try again!")
                    
                # Case 3: Difference is negative (Guess is too low)
                case _: 
                    # This final case catches any remaining possibility, which must be difference < 0
                    print("⬆️ Nope, your guess is a bit **low**. Give it another shot!")
                    
        except ValueError:
            print("That's not a valid number. Please enter an integer.")

# --- Main Game Loop ---
while True:
    play_game()
    
    # Offer to play again
    play_again = input("Play again? (yes/no): ").strip().lower()
    
    if play_again != 'yes':
        print("\nThanks for playing! Goodbye.")
        break