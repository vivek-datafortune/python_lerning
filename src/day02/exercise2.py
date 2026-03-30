# Day 2 - Exercise 2: Conditionals & Loops

print("=== Exercise 2: Conditionals & Loops ===\n")

# TODO 1: Write a function that returns a letter grade based on score
# 90-100: "A", 80-89: "B", 70-79: "C", 60-69: "D", below 60: "F"
def get_grade(score): 
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else: 
        return "F" 


# Test TODO 1
print(f"95 → {get_grade(95)}")   # Expected: A
print(f"85 → {get_grade(85)}")   # Expected: B
print(f"72 → {get_grade(72)}")   # Expected: C
print(f"65 → {get_grade(65)}")   # Expected: D
print(f"45 → {get_grade(45)}")   # Expected: F


# TODO 2: Write a function that checks if a number is positive, negative, or zero
# Return the string: "positive", "negative", or "zero"

def check_number(number):
    if number == 0:
        return "zero"
    elif number > 0:
        return "positive"
    else:
        return "negative"



# Test TODO 2
print(f" 5 → {check_number(5)}")    # Expected: positive
print(f"-3 → {check_number(-3)}")   # Expected: negative
print(f" 0 → {check_number(0)}")    # Expected: zero


# TODO 3: Write a function that checks if a year is a leap year
# Rules:
#   Divisible by 4 → leap year
#   BUT if divisible by 100 → NOT a leap year
#   UNLESS also divisible by 400 → leap year

def is_leap_year(year):
    if year % 4 == 0 :
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False

def is_leap_year_short(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



# Test TODO 3
print(f"2024 → {is_leap_year(2024)}")  # Expected: True
print(f"1900 → {is_leap_year(1900)}")  # Expected: False
print(f"2000 → {is_leap_year(2000)}")  # Expected: True
print(f"2023 → {is_leap_year(2023)}")  # Expected: False


# TODO 4: Write a function that uses a for loop to print a multiplication table
# multiply_table(5) should print:
#   5 x 1 = 5
#   5 x 2 = 10
#   ... up to 10

def multiply_table(table):
    for i in range(1, 11):
        print(f"{table} x {i} = {table * (i)}")

# Test TODO 4
multiply_table(5)


# TODO 5: Write a function that takes a list of numbers and returns only the even ones

def get_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

# Test TODO 5
print(f"Evens from [1,2,3,4,5,6]: {get_evens([1, 2, 3, 4, 5, 6])}")  # Expected: [2, 4, 6]
print(f"Evens from [7,8,9,10]:    {get_evens([7, 8, 9, 10])}")        # Expected: [8, 10]
