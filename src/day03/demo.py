# Day 3 - Data Structures Demo
# Run this file to see lists, dictionaries, tuples, sets & comprehensions in action!

print("=== Welcome to Day 3: Data Structures! ===\n")

# ============================================================
# 1. LISTS - Creating & Accessing
# ============================================================
print("1. Lists (Python's Arrays):")

numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
from_range = list(range(1, 6))

print(f"   numbers:    {numbers}")
print(f"   mixed:      {mixed}")
print(f"   from_range: {from_range}")
print()

# ============================================================
# 2. INDEXING (Negative indexing is a Python superpower!)
# ============================================================
print("2. Indexing:")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(f"   fruits:       {fruits}")
print(f"   First:        {fruits[0]}")
print(f"   Last:         {fruits[-1]}")       # No need for arr[arr.length - 1]!
print(f"   Second last:  {fruits[-2]}")
print()

# ============================================================
# 3. SLICING (No JS equivalent!)
# ============================================================
print("3. Slicing [start:end:step]:")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"   numbers:        {numbers}")
print(f"   [2:5]  →        {numbers[2:5]}")     # Index 2 to 4
print(f"   [:4]   →        {numbers[:4]}")       # First 4
print(f"   [6:]   →        {numbers[6:]}")       # From index 6
print(f"   [-3:]  →        {numbers[-3:]}")      # Last 3
print(f"   [::2]  →        {numbers[::2]}")      # Every 2nd
print(f"   [1::2] →        {numbers[1::2]}")     # Every 2nd starting at 1
print(f"   [::-1] →        {numbers[::-1]}")     # Reversed!
print()

# ============================================================
# 4. LIST METHODS
# ============================================================
print("4. List Methods:")
fruits = ["apple", "banana", "cherry"]
print(f"   Start:   {fruits}")

fruits.append("date")
print(f"   append:  {fruits}")

fruits.insert(1, "blueberry")
print(f"   insert:  {fruits}")

fruits.remove("banana")
print(f"   remove:  {fruits}")

popped = fruits.pop()
print(f"   pop():   {fruits} (popped: '{popped}')")

popped = fruits.pop(0)
print(f"   pop(0):  {fruits} (popped: '{popped}')")
print()

# ============================================================
# 5. SORTING & SEARCHING
# ============================================================
print("5. Sorting & Searching:")
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"   Original:        {nums}")

sorted_copy = sorted(nums)
print(f"   sorted() copy:   {sorted_copy}")
print(f"   Original still:  {nums}")

nums.sort()
print(f"   .sort() in-place:{nums}")

nums.reverse()
print(f"   .reverse():      {nums}")

print(f"   count(1):        {nums.count(1)}")
print(f"   index(5):        {nums.index(5)}")
print(f"   5 in nums:       {5 in nums}")
print()

# ============================================================
# 6. LIST OPERATIONS
# ============================================================
print("6. List Operations:")
a = [1, 2, 3]
b = [4, 5, 6]
print(f"   {a} + {b} = {a + b}")
print(f"   {a} * 3   = {a * 3}")
print(f"   len({a})  = {len(a)}")
print()

# ============================================================
# 7. DICTIONARIES (Like JS Objects)
# ============================================================
print("=" * 50)
print("7. Dictionaries:")

person = {
    "name": "Vivek",
    "age": 30,
    "city": "NYC"
}
print(f"   person:           {person}")
print(f"   person['name']:   {person['name']}")
print(f"   .get('age'):      {person.get('age')}")
print(f"   .get('phone'):    {person.get('phone')}")         # Returns None
print(f"   .get('phone', 'N/A'): {person.get('phone', 'N/A')}")  # Default value
print()

# ============================================================
# 8. DICTIONARY OPERATIONS
# ============================================================
print("8. Dictionary Operations:")
person["email"] = "vivek@email.com"    # Add new key
print(f"   After add:  {person}")

person["age"] = 31                      # Update value
print(f"   After update:{person}")

del person["email"]                     # Delete key
print(f"   After del:   {person}")

print(f"   .keys():   {list(person.keys())}")
print(f"   .values(): {list(person.values())}")
print(f"   .items():  {list(person.items())}")
print()

# ============================================================
# 9. ITERATING DICTIONARIES
# ============================================================
print("9. Iterating Dictionaries:")
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

print("   Looping with .items():")
for name, score in scores.items():
    print(f"     {name}: {score}")

print(f"   'Alice' in scores: {'Alice' in scores}")
print()

# ============================================================
# 10. TUPLES (Immutable Lists)
# ============================================================
print("=" * 50)
print("10. Tuples (Immutable - can't change after creation):")

point = (10, 20)
rgb = (255, 128, 0)
print(f"   point:    {point}")
print(f"   rgb:      {rgb}")

# Unpacking
x, y = point
r, g, b = rgb
print(f"   Unpacked: x={x}, y={y}")
print(f"   Unpacked: r={r}, g={g}, b={b}")

# Multiple return values use tuples
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([5, 2, 8, 1, 9])
print(f"   min_max:  low={low}, high={high}")
print()

# ============================================================
# 11. SETS (Unique Values)
# ============================================================
print("11. Sets (Unique, Unordered):")

unique = {1, 2, 2, 3, 3, 3}
print(f"   {{1, 2, 2, 3, 3, 3}} → {unique}")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"   a = {a}")
print(f"   b = {b}")
print(f"   a | b (union):        {a | b}")
print(f"   a & b (intersection): {a & b}")
print(f"   a - b (difference):   {a - b}")

# Removing duplicates from a list
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(f"   Deduplicate: {names} → {unique_names}")
print()

# ============================================================
# 12. LIST COMPREHENSIONS (Python Superpower!)
# ============================================================
print("=" * 50)
print("12. List Comprehensions:")
print("   JavaScript:  numbers.map(n => n * 2)")
print("   Python:      [n * 2 for n in numbers]")
print()

numbers = [1, 2, 3, 4, 5]

# Map equivalent
doubled = [n * 2 for n in numbers]
print(f"   Doubled:       {doubled}")

# Filter equivalent
evens = [n for n in numbers if n % 2 == 0]
print(f"   Evens:         {evens}")

# Map + Filter
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(f"   Even squares:  {even_squares}")

# Squares of 1-10
squares = [n ** 2 for n in range(1, 11)]
print(f"   Squares 1-10:  {squares}")

# Uppercase words
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(f"   Uppercased:    {upper}")

# With condition expression
nums = [-2, -1, 0, 1, 2]
clipped = [n if n > 0 else 0 for n in nums]
print(f"   Clipped:       {nums} → {clipped}")
print()

# ============================================================
# 13. DICTIONARY & SET COMPREHENSIONS
# ============================================================
print("13. Dictionary & Set Comprehensions:")

# Dict comprehension
squares_dict = {n: n ** 2 for n in range(1, 6)}
print(f"   Squares dict:  {squares_dict}")

# From two lists using zip
keys = ["name", "age", "city"]
values = ["Vivek", 30, "NYC"]
person = {k: v for k, v in zip(keys, values)}
print(f"   From zip:      {person}")

# Set comprehension
word_lengths = {len(w) for w in ["hello", "world", "hi", "hey"]}
print(f"   Word lengths:  {word_lengths}")
print()

# ============================================================
# 14. WHEN TO USE WHAT?
# ============================================================
print("=" * 50)
print("14. When to Use What?")
print("   list  → Ordered, changeable, allows duplicates")
print("   dict  → Key-value pairs, fast lookups by key")
print("   tuple → Ordered, immutable (fixed data)")
print("   set   → Unique values, fast membership checks")
print()

print("=== Day 3 Demo Complete! ===")
