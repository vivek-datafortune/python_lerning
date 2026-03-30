# Day 2 - Python Functions, Conditionals & Loops Demo
# Run this file to see all the concepts in action!

print("=== Welcome to Day 2: Functions, Control Flow & Loops! ===\n")

# ============================================================
# 1. FUNCTIONS - Reusable blocks of code
# ============================================================
print("1. Functions (def keyword):")

# Basic function - no return value
def say_hello():
    print("   Hello from a function!")

say_hello()  # Call the function

# Function with a parameter
def greet(name):
    print(f"   Hello, {name}!")

greet("Vivek")
greet("Python")
print()

# ============================================================
# 2. FUNCTIONS WITH RETURN VALUES
# ============================================================
print("2. Functions with return values:")

def add(a, b):
    return a + b

result = add(5, 3)
print(f"   add(5, 3) = {result}")
print(f"   add(10, 20) = {add(10, 20)}")
print()

# ============================================================
# 3. DEFAULT PARAMETERS
# ============================================================
print("3. Default parameters:")

def greet_with_default(name="Guest"):
    return f"Hello, {name}!"

print(f"   greet_with_default()        = {greet_with_default()}")
print(f"   greet_with_default('Vivek') = {greet_with_default('Vivek')}")
print()

# ============================================================
# 4. MULTIPLE RETURN VALUES (Python superpower!)
# ============================================================
print("4. Multiple return values:")

def get_name_and_age():
    return "Vivek", 30  # Returns a tuple

name, age = get_name_and_age()  # Unpack into variables
print(f"   Name: {name}, Age: {age}")
print()

# ============================================================
# 5. *args - VARIABLE NUMBER OF ARGUMENTS
# ============================================================
print("5. Variable arguments (*args):")

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"   sum_all(1, 2, 3)    = {sum_all(1, 2, 3)}")
print(f"   sum_all(10, 20, 30) = {sum_all(10, 20, 30)}")
print()

# ============================================================
# 6. IF / ELIF / ELSE - Making decisions
# ============================================================
print("=" * 50)
print("6. If / Elif / Else:")

age = 20

if age >= 18:
    print(f"   age={age}: You are an adult")
else:
    print(f"   age={age}: You are a minor")

# elif = "else if" in JavaScript
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"   score={score}: Grade is {grade}")
print()

# ============================================================
# 7. COMPARISON OPERATORS
# ============================================================
print("7. Comparison Operators:")
print(f"   5 == 5  : {5 == 5}")     # Equal
print(f"   5 != 3  : {5 != 3}")     # Not equal
print(f"   5 > 3   : {5 > 3}")      # Greater than
print(f"   5 < 3   : {5 < 3}")      # Less than
print(f"   5 >= 5  : {5 >= 5}")     # Greater or equal
print(f"   5 <= 3  : {5 <= 3}")     # Less or equal
print()

# ============================================================
# 8. LOGICAL OPERATORS (words, not symbols!)
# ============================================================
print("8. Logical Operators:")
print("   JavaScript uses:  &&  ||  !")
print("   Python uses:      and  or  not")
print()
print(f"   True and False  = {True and False}")   # Both must be True
print(f"   True or False   = {True or False}")    # At least one True
print(f"   not True        = {not True}")         # Flip the value
print()

age = 25
has_license = True
if age >= 18 and has_license:
    print(f"   age={age}, has_license={has_license}: Can drive!")
print()

# ============================================================
# 9. TERNARY OPERATOR (one-line if/else)
# ============================================================
print("9. Ternary Operator:")
print("   JavaScript:  const x = condition ? 'yes' : 'no'")
print("   Python:      x = 'yes' if condition else 'no'")
print()

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"   age={age}: status = {status}")

number = 7
parity = "Even" if number % 2 == 0 else "Odd"
print(f"   number={number}: {parity}")
print()

# ============================================================
# 10. FOR LOOPS with range()
# ============================================================
print("=" * 50)
print("10. For Loops with range():")

print("   range(5) →", end=" ")
for i in range(5):                  # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

print("   range(1, 6) →", end=" ")
for i in range(1, 6):              # 1, 2, 3, 4, 5
    print(i, end=" ")
print()

print("   range(0, 10, 2) →", end=" ")
for i in range(0, 10, 2):         # 0, 2, 4, 6, 8
    print(i, end=" ")
print()
print()

# ============================================================
# 11. FOR LOOPS over lists
# ============================================================
print("11. Looping over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"   I like {fruit}")
print()

# enumerate() gives you the index too
print("   With enumerate():")
for index, fruit in enumerate(fruits, start=1):
    print(f"   {index}. {fruit}")
print()

# ============================================================
# 12. WHILE LOOPS
# ============================================================
print("12. While Loops:")
count = 1
while count <= 5:
    print(f"   Count: {count}")
    count += 1       # Don't forget this or infinite loop!
print()

# ============================================================
# 13. BREAK and CONTINUE
# ============================================================
print("13. Break and Continue:")

print("   break (stop at 5):", end=" ")
for i in range(10):
    if i == 5:
        break          # Exit the loop entirely
    print(i, end=" ")
print()

print("   continue (skip 3):", end=" ")
for i in range(6):
    if i == 3:
        continue       # Skip this iteration, go to next
    print(i, end=" ")
print()
print()

# ============================================================
# 14. COMBINING FUNCTIONS + CONDITIONALS + LOOPS
# ============================================================
print("14. Putting it all together:")

def fizzbuzz(n):
    """Print FizzBuzz from 1 to n."""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

print("   FizzBuzz 1-20:")
print("   ", end="")
fizzbuzz(20)
print()
print()

print("=== Demo complete! Now try the exercises ===")
print("  python exercise1.py")
print("  python exercise2.py")
print("  python day02_guessing_game.py")
