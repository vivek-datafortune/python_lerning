# Day 1 - Exercise 1: Variables and Types

print("=== Exercise 1: Variables and Types ===\n")

# TODO 1: Create variables for your name, age, and favorite programming language
first_name = "Vivek"
last_name = "Kumar"
age = 30
favorite_language = "Python"


# TODO 2: Print a greeting using f-strings
# Example: "Hi, I'm John, 30 years old, and I love JavaScript"
print(f"Hi, I'm {first_name}, {age} years old, and I love {favorite_language}")


# TODO 3: Calculate and print your age in days (age * 365)
age_in_days = age * 365
print(f"I am approximately {age_in_days} days old.")

# TODO 4: Combine first and last name into full name
full_name = first_name + " " + last_name
print(f"My full name is: {full_name}")


# TODO 5: Print your full name in uppercase and lowercase
print(f"Full name in uppercase: {full_name.upper()}")
print(f"Full name in lowercase: {full_name.lower()}")

# TODO 6: Check if your name contains the letter 'a' (use 'in' operator)
contains_a = 'a' in full_name.lower()
print(f"Does my name contain the letter 'a'? {contains_a}")
