# Day 2 - Mini Project: Number Guessing Game
# Combines functions, conditionals, and loops into a fun game!

import random

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100")
print()

# TODO 1: Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

# TODO 2: Create a game loop using while
while attempts < max_attempts:
    # Get user guess (wrapped in try/except to handle bad input)
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!\n")
        continue

    attempts += 1

    # TODO 3: Check the guess and give feedback
    if guess == secret_number:
        print(f"\nCongratulations! You guessed it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    # TODO 4: Show remaining attempts
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"You have {remaining} attempts left.\n")
else:
    # This else belongs to the while loop — runs if loop ends WITHOUT break
    print(f"\nGame over! The number was {secret_number}")


# BONUS: Uncomment below to add a "play again" loop
# while True:
#     again = input("\nPlay again? (yes/no): ").lower()
#     if again != "yes":
#         print("Thanks for playing!")
#         break
#     # ... copy the game logic into a function and call it here
