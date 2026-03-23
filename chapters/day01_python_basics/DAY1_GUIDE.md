# Day 1: Python Fundamentals I - Variables, Data Types & Basic Operations

**Duration**: 3 hours  
**Goal**: Understand Python syntax, variables, and basic data types coming from JavaScript

---

## 📋 Learning Objectives

By the end of Day 1, you will:
- ✅ Understand Python syntax differences from JavaScript
- ✅ Work with variables and Python's type system
- ✅ Master basic data types (strings, numbers, booleans)
- ✅ Perform basic operations and type conversions
- ✅ Use Python's interactive shell (REPL)
- ✅ Write and run your first Python scripts

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Setup & Environment | 20 min | Hands-on |
| Theory: Variables & Types | 30 min | Reading |
| Exercise 1: Basic Operations | 40 min | Coding |
| Theory: Strings & Formatting | 30 min | Reading |
| Exercise 2: String Manipulation | 40 min | Coding |
| Mini-Project: Calculator | 20 min | Project |

---

## 🎯 Hour 1: Setup & Variables (60 min)

### Setup (20 min)

#### Install Python
```bash
# Check if Python is installed
python --version

# Download from: https://www.python.org/downloads/
# Make sure to check "Add Python to PATH"
```

#### Create Virtual Environment
```bash
cd c:\workspace\learning\python_learning
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### Verify Installation
```bash
python --version
pip --version
```

### Variables & Basic Types (40 min)

#### JavaScript vs Python Variables

**JavaScript**:
```javascript
const name = "John";  // Immutable
let age = 30;         // Mutable
var old = true;       // Old way (mutable)
```

**Python**:
```python
name = "John"  # All variables are mutable (like 'let')
age = 30
# Convention: UPPERCASE for constants
MAX_SIZE = 100
```

#### Python Data Types

```python
# Numbers
integer = 42
float_num = 3.14
complex_num = 2 + 3j

# Strings
single = 'Hello'
double = "World"
multi_line = """This is
a multi-line
string"""

# Boolean (capitalized!)
is_active = True
is_deleted = False

# None (like null in JS)
empty = None

# Check type
print(type(integer))  # <class 'int'>
print(type(name))     # <class 'str'>
```

#### Type Conversion

```python
# String to number
age = int("30")
price = float("19.99")

# Number to string
count_str = str(42)

# Boolean conversion
bool(1)      # True
bool(0)      # False
bool("")     # False
bool("hi")   # True
```

---

## 🎯 Hour 2: Strings & Formatting (60 min)

### String Operations (30 min)

```python
# String concatenation
first = "Hello"
last = "World"
full = first + " " + last  # "Hello World"

# String repetition (unique to Python!)
stars = "*" * 10  # "**********"

# String indexing
text = "Python"
print(text[0])      # 'P' (first character)
print(text[-1])     # 'n' (last character)
print(text[1:4])    # 'yth' (slice)

# String methods
message = "hello world"
print(message.upper())        # "HELLO WORLD"
print(message.capitalize())   # "Hello world"
print(message.title())        # "Hello World"
print(message.replace("hello", "hi"))  # "hi world"
print(message.split())        # ['hello', 'world']
print("hello" in message)     # True
```

### String Formatting (30 min)

```python
name = "John"
age = 30

# 1. f-strings (Python 3.6+, RECOMMENDED)
message = f"My name is {name} and I'm {age} years old"

# With expressions
print(f"Next year I'll be {age + 1}")
print(f"Name in caps: {name.upper()}")

# 2. format() method
message = "My name is {} and I'm {} years old".format(name, age)
message = "My name is {0} and I'm {1} years old".format(name, age)

# 3. Old style (not recommended)
message = "My name is %s and I'm %d years old" % (name, age)

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")     # Price: $19.99
print(f"Count: {42:05d}")          # Count: 00042
```

---

## 🎯 Hour 3: Practice & Mini-Project (60 min)

### Exercise 1: Basic Operations (20 min)

Create `day01_exercise1.py`:

```python
# Exercise 1: Variables and Types

# TODO 1: Create variables for your name, age, and favorite programming language
# your code here

# TODO 2: Print a greeting using f-strings
# Example: "Hi, I'm John, 30 years old, and I love JavaScript"

# TODO 3: Calculate and print your age in days (age * 365)

# TODO 4: Create a variable with your full name (first + last)
first_name = "John"
last_name = "Doe"
# Combine them

# TODO 5: Print your name in uppercase and lowercase

# TODO 6: Check if your name contains the letter 'a' (use 'in' operator)
```

### Exercise 2: String Manipulation (20 min)

Create `day01_exercise2.py`:

```python
# Exercise 2: String Operations

email = "john.doe@example.com"

# TODO 1: Extract the username (before @)
# Hint: use split('@')

# TODO 2: Extract the domain (after @)

# TODO 3: Check if the email contains '.com'

# TODO 4: Replace '.com' with '.org'

# TODO 5: Print the email in uppercase

# Challenge: Extract just the domain name without .com
# "john.doe@example.com" -> "example"
```

### Mini-Project: Simple Calculator (20 min)

Create `day01_calculator.py`:

```python
# Mini-Project: Simple Calculator

print("=== Simple Calculator ===")
print("This calculator performs basic operations")
print()

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# TODO: Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# TODO: Print results using f-strings
print(f"\nResults:")
print(f"{num1} + {num2} = {addition}")
# Add more print statements

# BONUS: Add power and modulo operations
# power = num1 ** num2
# modulo = num1 % num2
```

---

## 🔍 Key Takeaways

### Python vs JavaScript Differences

| Feature | JavaScript | Python |
|---------|-----------|--------|
| Variables | `const`, `let`, `var` | No keywords (all like `let`) |
| Strings | `'` or `"` (same) | `'` or `"` or `"""` (multi-line) |
| String interpolation | `` `${var}` `` | `f"{var}"` |
| Boolean | `true`, `false` | `True`, `False` |
| Null | `null`, `undefined` | `None` |
| Comments | `//` or `/* */` | `#` or `"""..."""` |
| Console | `console.log()` | `print()` |

### Important Python Concepts

1. **Indentation Matters** - Python uses indentation instead of `{}`
2. **No Semicolons** - Line breaks are significant
3. **snake_case** - Use `snake_case` not `camelCase`
4. **Type Flexibility** - Variables can change types
5. **String Slicing** - Powerful string manipulation with `[start:end]`

---

## 📚 Resources

### Documentation
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)

### Practice
- [Python Exercises - W3Schools](https://www.w3schools.com/python/python_exercises.asp)
- [Codewars Python](https://www.codewars.com/?language=python)
- [HackerRank Python](https://www.hackerrank.com/domains/python)

---

## ✅ Day 1 Checklist

Before moving to Day 2, make sure you can:
- [ ] Create and run Python scripts
- [ ] Use variables and understand Python types
- [ ] Work with strings (concatenation, slicing, methods)
- [ ] Use f-strings for string formatting
- [ ] Convert between different data types
- [ ] Use the Python REPL for quick testing

---

## 🎯 Homework

1. Complete all exercises (exercise1.py and exercise2.py)
2. Complete the mini-project (calculator.py)
3. Experiment with the Python REPL:
   ```bash
   python
   >>> name = "Python"
   >>> print(name.upper())
   >>> exit()
   ```
4. Read ahead: Day 2 covers functions and control flow

---

## 💡 Pro Tips

1. **Use the REPL** - Great for testing small snippets
2. **Type as You Learn** - Don't just copy-paste
3. **Compare to JS** - Connect new concepts to what you know
4. **Print Everything** - Use `print()` liberally while learning
5. **Read Error Messages** - Python errors are very helpful

---

**Tomorrow**: Day 2 - Functions, Control Flow, and Loops

**Great job on Day 1! Keep coding! 🚀**
