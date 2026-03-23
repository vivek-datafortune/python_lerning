# Day 2: Python Fundamentals II - Functions, Control Flow & Loops

**Duration**: 3 hours  
**Goal**: Master Python functions, conditionals, and iteration patterns

---

## 📋 Learning Objectives

By the end of Day 2, you will:
- ✅ Write and call Python functions with parameters
- ✅ Use default parameters and return values
- ✅ Master if/elif/else conditionals
- ✅ Implement for and while loops
- ✅ Understand range() and enumerate()
- ✅ Handle basic error cases

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: Functions | 30 min | Reading |
| Exercise: Function Practice | 30 min | Coding |
| Theory: Control Flow | 30 min | Reading |
| Exercise: Conditionals | 30 min | Coding |
| Theory: Loops | 30 min | Reading |
| Mini-Project: Number Guessing Game | 30 min | Project |

---

## 🎯 Hour 1: Functions (60 min)

### Basic Function Syntax (30 min)

#### JavaScript vs Python Functions

**JavaScript**:
```javascript
// Function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

// Arrow function
const add = (a, b) => a + b;

// Default parameters
function greet(name = "Guest") {
    return `Hello, ${name}!`;
}
```

**Python**:
```python
# Function definition
def greet(name):
    return f"Hello, {name}!"

# Lambda (less common than JS arrows)
add = lambda a, b: a + b

# Default parameters
def greet(name="Guest"):
    return f"Hello, {name}!"
```

### Function Features

```python
# Multiple return values (unique to Python!)
def get_user_info():
    return "John", 30, "john@email.com"

name, age, email = get_user_info()
print(name)  # John

# Docstrings (function documentation)
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.
    
    Args:
        width (float): Rectangle width
        height (float): Rectangle height
    
    Returns:
        float: Area of the rectangle
    """
    return width * height

# Type hints (optional, but recommended)
def add(a: int, b: int) -> int:
    return a + b

# Keyword arguments
def create_user(name, age, email):
    print(f"{name}, {age}, {email}")

create_user(name="John", email="j@e.com", age=30)  # Order doesn't matter!

# *args and **kwargs
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="NYC")
```

### Practice Exercises (30 min)

Create `day02_functions.py`:

```python
# Exercise 1: Basic Functions

# TODO 1: Write a function that takes two numbers and returns their sum
def add(a, b):
    pass  # Replace with your code

# TODO 2: Write a function that converts Celsius to Fahrenheit
# Formula: (celsius * 9/5) + 32
def celsius_to_fahrenheit(celsius):
    pass

# TODO 3: Write a function with default parameter
# greet(name="Guest") should default to "Guest" if no name provided
def greet(name="Guest"):
    pass

# TODO 4: Write a function that returns multiple values
# Return: full_name, age, is_adult (True if age >= 18)
def create_person(first, last, age):
    pass

# TODO 5: Write a function that takes variable arguments
# sum_numbers(1, 2, 3, 4) should return 10
def sum_numbers(*numbers):
    pass

# Test your functions
print(add(5, 3))
print(celsius_to_fahrenheit(0))
print(greet())
print(greet("John"))
```

---

## 🎯 Hour 2: Control Flow (60 min)

### If/Elif/Else Statements (30 min)

#### JavaScript vs Python Conditionals

**JavaScript**:
```javascript
if (age >= 18 && hasLicense) {
    console.log("Can drive");
} else if (age >= 16) {
    console.log("Can get permit");
} else {
    console.log("Too young");
}
```

**Python**:
```python
if age >= 18 and has_license:
    print("Can drive")
elif age >= 16:
    print("Can get permit")
else:
    print("Too young")
```

### Comparison Operators

```python
# Comparison (similar to JS)
5 == 5      # True (equal)
5 != 3      # True (not equal)
5 > 3       # True
5 < 3       # False
5 >= 5      # True
5 <= 3      # False

# Python-specific
5 < 10 < 20  # True (chained comparison!)
x in [1, 2, 3]  # Check if x is in list
"hello" in "hello world"  # True

# Logical operators (WORDS, not symbols!)
True and False   # False (not &&)
True or False    # True (not ||)
not True         # False (not !)
```

### Ternary Operator

```python
# JavaScript: const result = age >= 18 ? "Adult" : "Minor";
# Python:
result = "Adult" if age >= 18 else "Minor"

# Example
max_value = a if a > b else b
status = "Pass" if score >= 60 else "Fail"
```

### Practice Exercises (30 min)

Create `day02_conditionals.py`:

```python
# Exercise 2: Control Flow

# TODO 1: Write a function that returns grade based on score
# 90-100: A, 80-89: B, 70-79: C, 60-69: D, below 60: F
def get_grade(score):
    pass

# TODO 2: Write a function that checks if a number is positive, negative, or zero
def check_number(num):
    pass

# TODO 3: Write a function that checks if a year is a leap year
# Leap year: divisible by 4, but not by 100, unless also divisible by 400
def is_leap_year(year):
    pass

# TODO 4: FizzBuzz for a single number
# If divisible by 3: return "Fizz"
# If divisible by 5: return "Buzz"
# If divisible by both: return "FizzBuzz"
# Otherwise: return the number
def fizzbuzz(number):
    pass

# TODO 5: Using ternary operator
# Write a one-liner that returns "Even" or "Odd"
def even_or_odd(number):
    return  # Your ternary expression here

# Test your functions
print(get_grade(85))
print(check_number(-5))
print(is_leap_year(2024))
print(fizzbuzz(15))
print(even_or_odd(7))
```

---

## 🎯 Hour 3: Loops & Mini-Project (60 min)

### Loops (30 min)

#### For Loops

**JavaScript**:
```javascript
// Traditional for
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// For...of
for (const item of array) {
    console.log(item);
}
```

**Python**:
```python
# For loop with range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# For loop over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Range with start and end
for i in range(1, 6):  # 1, 2, 3, 4, 5 (6 is excluded!)
    print(i)

# Range with step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Enumerate (with index)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Starting enumerate from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
```

#### While Loops

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")

# While with continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)  # Only prints odd numbers
```

### Loop Control

```python
# Break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# Continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4

# Else with loops (unique to Python!)
for i in range(5):
    print(i)
else:
    print("Loop completed normally")  # Runs if no break occurred
```

### Mini-Project: Number Guessing Game (30 min)

Create `day02_guessing_game.py`:

```python
import random

# Mini-Project: Number Guessing Game

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100")
print()

# TODO 1: Generate random number
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

# TODO 2: Create game loop
while attempts < max_attempts:
    # Get user guess
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
    attempts += 1
    
    # TODO 3: Check guess and give feedback
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
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
    print(f"😢 Game over! The number was {secret_number}")

# BONUS: Ask if they want to play again
# Use another while loop to restart the game
```

---

## 🔍 Key Takeaways

### Python vs JavaScript

| Feature | JavaScript | Python |
|---------|-----------|--------|
| Function | `function name() {}` | `def name():` |
| If statement | `if (condition) {}` | `if condition:` |
| Logical AND | `&&` | `and` |
| Logical OR | `\|\|` | `or` |
| Logical NOT | `!` | `not` |
| For loop | `for (let i=0; i<5; i++)` | `for i in range(5):` |
| For...of | `for (const x of arr)` | `for x in arr:` |

### Important Concepts

1. **Indentation is critical** - Defines code blocks
2. **No parentheses in if/while** - But colon is required
3. **range() is not inclusive** - `range(5)` = 0-4
4. **enumerate() adds index** - Better than manual counter
5. **Multiple return values** - Unique Python feature

---

## 📚 Resources

- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Loops Tutorial](https://realpython.com/python-for-loop/)

---

## ✅ Day 2 Checklist

- [ ] Write functions with parameters and return values
- [ ] Use default parameters
- [ ] Implement if/elif/else statements
- [ ] Use logical operators (and, or, not)
- [ ] Write for loops with range()
- [ ] Use enumerate() for indexed iteration
- [ ] Implement while loops with break/continue
- [ ] Complete the guessing game project

---

## 🎯 Homework

1. Complete `day02_functions.py` exercises
2. Complete `day02_conditionals.py` exercises
3. Build and enhance the guessing game
4. **Challenge**: Create a simple menu-driven calculator using loops and functions

---

**Tomorrow**: Day 3 - Lists, Dictionaries & Comprehensions

**Keep up the great work! 💪**
