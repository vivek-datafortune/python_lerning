# Day 5 - Exercise 1: Building Utility Modules

print("=== Exercise 1: Utility Modules ===\n")

# ============================================================
# PART A: String Utilities
# ============================================================
print("--- Part A: String Utilities ---\n")


# TODO 1: Create a function to capitalize the first letter of each word
def title_case(text):
    """Return text with first letter of each word capitalised.
    Example: 'hello world' → 'Hello World'
    """
    pass  # TODO: implement (hint: look up str.title() or split/join)


# TODO 2: Create a function that counts vowels in a string
def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in text.
    Example: count_vowels('hello') → 2
    """
    pass  # TODO: implement


# TODO 3: Create a function that reverses a string
def reverse_string(text):
    """Return the reversed version of text.
    Example: reverse_string('python') → 'nohtyp'
    """
    pass  # TODO: implement (hint: slicing with [::-1])


# TODO 4: Create a function that checks if a string is a palindrome
def is_palindrome(text):
    """Return True if text reads the same forwards and backwards.
    Example: is_palindrome('racecar') → True
             is_palindrome('hello')   → False
    Tip: ignore case and spaces.
    """
    pass  # TODO: implement


# TODO 5: Create a function that truncates a long string
def truncate(text, max_length, suffix="..."):
    """Return text truncated to max_length, appending suffix if cut.
    Example: truncate('Hello World', 7) → 'Hell...'
    """
    pass  # TODO: implement


# Test Part A (uncomment when ready)
# print(title_case("hello world from python"))    # Hello World From Python
# print(count_vowels("hello world"))              # 3
# print(reverse_string("python"))                # nohtyp
# print(is_palindrome("racecar"))                # True
# print(is_palindrome("hello"))                  # False
# print(truncate("Hello, World!", 8))            # Hello...


# ============================================================
# PART B: Math Utilities
# ============================================================
print("--- Part B: Math Utilities ---\n")


# TODO 6: Create a function that checks if a number is prime
def is_prime(n):
    """Return True if n is a prime number.
    Example: is_prime(7) → True, is_prime(9) → False
    Tip: check divisibility from 2 up to sqrt(n).
    """
    pass  # TODO: implement (hint: import math and use math.sqrt)


# TODO 7: Create a function that returns the factorial of n
def factorial(n):
    """Return n! (factorial of n). n must be >= 0.
    Example: factorial(5) → 120  (5 * 4 * 3 * 2 * 1)
    """
    pass  # TODO: implement (use a loop or recursion)


# TODO 8: Create a function that returns the first n fibonacci numbers
def fibonacci(n):
    """Return a list of the first n fibonacci numbers.
    Example: fibonacci(7) → [0, 1, 1, 2, 3, 5, 8]
    """
    pass  # TODO: implement


# TODO 9: Clamp a number between a min and max value
def clamp(value, min_val, max_val):
    """Return value clamped to [min_val, max_val].
    Example: clamp(15, 0, 10) → 10
             clamp(-5, 0, 10) → 0
             clamp(7,  0, 10) → 7
    """
    pass  # TODO: implement (hint: use min() and max())


# Test Part B (uncomment when ready)
# print(is_prime(7))          # True
# print(is_prime(9))          # False
# print(is_prime(2))          # True
# print(factorial(5))         # 120
# print(factorial(0))         # 1
# print(fibonacci(7))         # [0, 1, 1, 2, 3, 5, 8]
# print(clamp(15, 0, 10))     # 10
# print(clamp(-5, 0, 10))     # 0
# print(clamp(7,  0, 10))     # 7


# ============================================================
# PART C: Using Standard Library Modules
# ============================================================
print("--- Part C: Standard Library ---\n")

import os
import json
import random
from datetime import datetime

# TODO 10: Print today's date formatted as "DD Month YYYY"
# Example output: "27 March 2026"
def formatted_today():
    pass  # TODO: use datetime.now().strftime(...)

# TODO 11: Return a random greeting from a list of greetings
GREETINGS = ["Hello!", "Hi there!", "Hey!", "Howdy!", "Greetings!"]
def random_greeting():
    pass  # TODO: use random.choice(GREETINGS)

# TODO 12: Given a dictionary, return it as a formatted JSON string
def to_json(data):
    """Return a pretty-printed JSON string of data."""
    pass  # TODO: use json.dumps with indent=2

# TODO 13: Return the number of .py files in a given directory path
def count_py_files(directory):
    """Return how many .py files exist directly in directory."""
    pass  # TODO: use os.listdir() and filter by .endswith('.py')


# Test Part C (uncomment when ready)
# print(formatted_today())                             # e.g. "27 March 2026"
# print(random_greeting())                             # e.g. "Hey!"
# print(to_json({"name": "Vivek", "day": 5}))
# print(count_py_files('.'))                           # number of .py files here
