# Day 2 - Exercise 1: Functions

print("=== Exercise 1: Functions ===\n")

# TODO 1: Write a function called "add" that takes two numbers and returns their sum
def add(a, b):
    return a + b


# Test TODO 1
print(f"add(5, 3) = {add(5, 3)}")          # Expected: 8
print(f"add(-2, 7) = {add(-2, 7)}")        # Expected: 5


# TODO 2: Write a function that converts Celsius to Fahrenheit
# Formula: (celsius * 9/5) + 32
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32



# Test TODO 2
print(f"0°C  = {celsius_to_fahrenheit(0)}°F")    # Expected: 32.0
print(f"100°C = {celsius_to_fahrenheit(100)}°F")  # Expected: 212.0


# TODO 3: Write a function "greet" with a default parameter
# greet("Vivek") should return "Hello, Vivek!"
# greet()        should return "Hello, Guest!"
def greet(name="Guest"):
    return f"Hello, {name}!"


# Test TODO 3
print(greet())          # Expected: Hello, Guest!
print(greet("Vivek"))   # Expected: Hello, Vivek!


# TODO 4: Write a function that returns multiple values
# Given first name, last name, and age:
# Return full_name, age, and is_adult (True if age >= 18)
def create_person(first, last, age):
    full_name = first + " " + last
    is_adult = age >= 18
    return full_name, age, is_adult


# Test TODO 4
name, age, is_adult = create_person("Vivek", "Kumar", 30)
print(f"Name: {name}, Age: {age}, Adult: {is_adult}")  # Vivek Kumar, 30, True


# TODO 5: Write a function that accepts any number of arguments and returns their sum
# sum_numbers(1, 2, 3, 4) should return 10
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Test TODO 5
print(f"sum_numbers(1, 2, 3, 4) = {sum_numbers(1, 2, 3, 4)}")  # Expected: 10
print(f"sum_numbers(10, 20) = {sum_numbers(10, 20)}")            # Expected: 30
