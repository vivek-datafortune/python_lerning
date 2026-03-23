# Day 1 - Python Basics Demo
# Run this file to see basic Python concepts in action

print("=== Welcome to Day 1: Python Basics! ===\n")

# 1. VARIABLES (no const/let/var needed!)
print("1. Variables:")
name = "Python Learner"
age = 25
is_learning = True
print(f"   Name: {name}, Age: {age}, Learning: {is_learning}")
print()

# 2. DATA TYPES
print("2. Data Types:")
print(f"   String:  {type('hello').__name__}")
print(f"   Integer: {type(42).__name__}")
print(f"   Float:   {type(3.14).__name__}")
print(f"   Boolean: {type(True).__name__}")
print(f"   None:    {type(None).__name__}")
print()

# 3. STRING OPERATIONS
print("3. String Operations:")
text = "Python"
print(f"   Original:    {text}")
print(f"   Uppercase:   {text.upper()}")
print(f"   First char:  {text[0]}")
print(f"   Last char:   {text[-1]}")
print(f"   Slice [0:3]: {text[0:3]}")
print(f"   Repetition:  {'*' * 5}")
print()

# 4. F-STRINGS (Modern string formatting)
print("4. F-Strings:")
language = "Python"
version = 3.13
print(f"   I'm learning {language} version {version}")
print(f"   Math inside:  10 + 5 = {10 + 5}")
print(f"   Method inside: {'hello'.upper()}")
print()

# 5. TYPE CONVERSION
print("5. Type Conversion:")
num_string = "42"
actual_num = int(num_string)
print(f"   str '42'  -> int: {actual_num} ({type(actual_num).__name__})")
print(f"   int 100   -> str: '{str(100)}' ({type(str(100)).__name__})")
print()

# 6. BOOLEANS (capitalized in Python!)
print("6. Booleans:")
print(f"   True  (not 'true'): {True}")
print(f"   False (not 'false'): {False}")
print(f"   None  (not 'null'):  {None}")
print()

# 7. BASIC MATH OPERATIONS
print("7. Math Operations:")
a, b = 10, 3
print(f"   {a} + {b}  = {a + b}")
print(f"   {a} - {b}  = {a - b}")
print(f"   {a} * {b}  = {a * b}")
print(f"   {a} / {b}  = {a / b:.2f}")
print(f"   {a} ** {b} = {a ** b}  (power)")
print(f"   {a} % {b}  = {a % b}   (modulo)")
print()

print("=== Demo complete! Now try the exercises ===")
print("  python exercise1.py")
print("  python exercise2.py")
print("  python calculator.py")
