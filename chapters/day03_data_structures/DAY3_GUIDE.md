# Day 3: Data Structures - Lists, Dictionaries & Comprehensions

**Duration**: 3 hours  
**Goal**: Master Python's core data structures and powerful comprehension syntax

---

## 📋 Learning Objectives

By the end of Day 3, you will:
- ✅ Master Python lists and list methods
- ✅ Work with dictionaries (like JS objects)
- ✅ Understand tuples and sets
- ✅ Write list comprehensions
- ✅ Use dictionary and set comprehensions
- ✅ Nest and manipulate complex data structures

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: Lists | 30 min | Reading |
| Exercise: List Operations | 30 min | Coding |
| Theory: Dictionaries & Tuples | 30 min | Reading |
| Exercise: Dictionary Practice | 30 min | Coding |
| Theory: Comprehensions | 30 min | Reading |
| Mini-Project: Contact Manager | 30 min | Project |

---

## 🎯 Hour 1: Lists (60 min)

### Lists (Arrays in JavaScript) (30 min)

#### JavaScript vs Python Arrays/Lists

**JavaScript**:
```javascript
const arr = [1, 2, 3, 4, 5];
arr.push(6);           // Add to end
arr.pop();             // Remove from end
arr.unshift(0);        // Add to start
arr.shift();           // Remove from start
arr.length;            // Get length
```

**Python**:
```python
arr = [1, 2, 3, 4, 5]
arr.append(6)          # Add to end
arr.pop()              # Remove from end
arr.insert(0, 0)       # Add to start
arr.pop(0)             # Remove from start
len(arr)               # Get length
```

### List Operations

```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]  # Mixed types allowed!
empty = []
from_range = list(range(1, 6))  # [1, 2, 3, 4, 5]

# Accessing elements
first = numbers[0]         # 1
last = numbers[-1]         # 5 (negative index!)
second_last = numbers[-2]  # 4

# Slicing (powerful!)
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])    # [1, 2, 3] (start:end, end excluded)
print(numbers[:3])     # [0, 1, 2] (first 3)
print(numbers[3:])     # [3, 4, 5] (from index 3)
print(numbers[-2:])    # [4, 5] (last 2)
print(numbers[::2])    # [0, 2, 4] (every 2nd)
print(numbers[::-1])   # [5, 4, 3, 2, 1, 0] (reverse!)

# List methods
fruits = ["apple", "banana", "cherry"]
fruits.append("date")              # Add to end
fruits.insert(1, "blueberry")      # Insert at index
fruits.remove("banana")            # Remove by value
fruits.pop()                       # Remove and return last
fruits.pop(0)                      # Remove and return at index
fruits.clear()                     # Remove all

# Useful operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                     # Sort in place
sorted_nums = sorted(numbers)      # Return sorted copy
numbers.reverse()                  # Reverse in place
count = numbers.count(1)           # Count occurrences
index = numbers.index(4)           # Find first index

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2           # [1, 2, 3, 4, 5, 6]
repeated = list1 * 3               # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Checking membership
if 2 in numbers:
    print("Found!")
```

### Practice Exercises (30 min)

Create `day03_lists.py`:

```python
# Exercise 1: Lists

# TODO 1: Create a list of your top 5 programming languages
languages = []

# TODO 2: Add "Go" to the end using append()

# TODO 3: Insert "Rust" at index 2 using insert()

# TODO 4: Remove the first language using pop(0)

# TODO 5: Find the index of "Python" (if it exists)

# TODO 6: Sort the list alphabetically

# TODO 7: Reverse the list

# TODO 8: Create a new list with the last 3 languages using slicing

# TODO 9: Check if "JavaScript" is in the list

# TODO 10: Create a list of numbers 1-10 and get only even numbers using slicing
numbers = list(range(1, 11))
evens = []  # Use slicing: numbers[1::2] or similar
```

---

## 🎯 Hour 2: Dictionaries & Tuples (60 min)

### Dictionaries (Objects in JavaScript) (30 min)

**JavaScript**:
```javascript
const user = {
    name: "John",
    age: 30,
    email: "john@email.com"
};
console.log(user.name);
user.city = "NYC";
```

**Python**:
```python
user = {
    "name": "John",
    "age": 30,
    "email": "john@email.com"
}
print(user["name"])
user["city"] = "NYC"
```

### Dictionary Operations

```python
# Creating dictionaries
person = {"name": "John", "age": 30}
empty = {}
from_pairs = dict(name="John", age=30)

# Accessing values
name = person["name"]              # Raises KeyError if not found
age = person.get("age")            # Returns None if not found
age = person.get("age", 0)         # Returns 0 if not found (default)

# Adding/updating
person["email"] = "j@e.com"        # Add new key
person["age"] = 31                 # Update existing

# Removing
del person["email"]                # Delete key
age = person.pop("age")            # Remove and return
person.clear()                     # Remove all

# Dictionary methods
person = {"name": "John", "age": 30, "city": "NYC"}
keys = person.keys()               # dict_keys(['name', 'age', 'city'])
values = person.values()           # dict_values(['John', 30, 'NYC'])
items = person.items()             # dict_items([('name', 'John'), ...])

# Iterating
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Checking membership
if "name" in person:
    print("Name exists")

# Merging dictionaries (Python 3.9+)
defaults = {"theme": "dark", "lang": "en"}
settings = {"lang": "es"}
merged = defaults | settings       # {'theme': 'dark', 'lang': 'es'}
```

### Tuples (Immutable Lists)

```python
# Tuples - like lists but immutable
point = (10, 20)
rgb = (255, 128, 0)

# Accessing
x = point[0]
y = point[1]

# Unpacking
x, y = point
r, g, b = rgb

# Multiple return values use tuples
def get_dimensions():
    return 1920, 1080  # Actually returns tuple

width, height = get_dimensions()

# Named tuples (more readable)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)
```

### Sets (Unique Values)

```python
# Sets - unordered collection of unique values
numbers = {1, 2, 3, 4, 5}
unique = {1, 2, 2, 3, 3, 3}  # {1, 2, 3}

# Set operations
numbers.add(6)
numbers.remove(1)
numbers.discard(10)  # Won't error if not found

# Set math
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # Union: {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersection: {3, 4}
print(a - b)  # Difference: {1, 2}
```

### Practice Exercises (30 min)

Create `day03_dictionaries.py`:

```python
# Exercise 2: Dictionaries

# TODO 1: Create a dictionary representing a book
book = {
    # Add: title, author, year, pages, rating
}

# TODO 2: Add a key "isbn" with any value

# TODO 3: Update the rating to a new value

# TODO 4: Get the author using .get() method

# TODO 5: Check if "publisher" key exists

# TODO 6: Print all keys

# TODO 7: Print all values

# TODO 8: Print all key-value pairs using .items()

# TODO 9: Create a dictionary of students and their grades
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
# Add 3 more students

# TODO 10: Calculate average grade
total = sum(students.values())
average = total / len(students)
print(f"Average grade: {average:.2f}")
```

---

## 🎯 Hour 3: Comprehensions & Mini-Project (60 min)

### List Comprehensions (30 min)

**JavaScript**:
```javascript
// Map
const doubled = numbers.map(n => n * 2);

// Filter
const evens = numbers.filter(n => n % 2 === 0);

// Map + Filter
const evenSquares = numbers
    .filter(n => n % 2 === 0)
    .map(n => n ** 2);
```

**Python**:
```python
# List comprehension (single line!)
numbers = [1, 2, 3, 4, 5]

doubled = [n * 2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]

# More examples
# Squares of 1-10
squares = [n ** 2 for n in range(1, 11)]

# Upper case all words
words = ["hello", "world"]
upper = [word.upper() for word in words]

# Nested loops
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]

# Conditional expressions
result = [n if n > 0 else 0 for n in [-2, -1, 0, 1, 2]]
# [0, 0, 0, 1, 2]
```

### Dictionary & Set Comprehensions

```python
# Dictionary comprehension
squares = {n: n**2 for n in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From two lists
keys = ['name', 'age', 'city']
values = ['John', 30, 'NYC']
person = {k: v for k, v in zip(keys, values)}

# Set comprehension
unique_lengths = {len(word) for word in ['hello', 'world', 'hi']}
# {2, 5}
```

### Mini-Project: Contact Manager (30 min)

Create `day03_contact_manager.py`:

```python
# Mini-Project: Contact Manager

contacts = []

def add_contact(name, phone, email):
    """Add a new contact"""
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print(f"✓ Added {name}")

def list_contacts():
    """List all contacts"""
    if not contacts:
        print("No contacts yet")
        return
    
    print("\n=== All Contacts ===")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

def search_contact(name):
    """Search for a contact by name"""
    # TODO: Implement search using list comprehension
    results = [c for c in contacts if name.lower() in c['name'].lower()]
    
    if results:
        print(f"\nFound {len(results)} contact(s):")
        for contact in results:
            print(f"  {contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print(f"No contacts found with name: {name}")

def delete_contact(name):
    """Delete a contact by name"""
    # TODO: Implement delete
    global contacts
    contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    print(f"✓ Deleted {name}")

# Main program loop
while True:
    print("\n=== Contact Manager ===")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    
    choice = input("\nEnter choice (1-5): ")
    
    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contact(name, phone, email)
    
    elif choice == '2':
        list_contacts()
    
    elif choice == '3':
        name = input("Search name: ")
        search_contact(name)
    
    elif choice == '4':
        name = input("Delete name: ")
        delete_contact(name)
    
    elif choice == '5':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")

# BONUS: Add a function to export contacts to a file
# BONUS: Add a function to import contacts from a file
```

---

## 🔍 Key Takeaways

### Python Data Structures

| Structure | JavaScript Equivalent | Mutable | Ordered | Unique |
|-----------|----------------------|---------|---------|--------|
| list | Array | Yes | Yes | No |
| dict | Object | Yes | Yes (3.7+) | Keys only |
| tuple | N/A | No | Yes | No |
| set | Set | Yes | No | Yes |

### Important Concepts

1. **Negative indexing** - `arr[-1]` gets last element
2. **Slicing** - `arr[start:end:step]` is very powerful
3. **List comprehensions** - Replace map/filter with single line
4. **Dictionary .get()** - Safer than `[]` access
5. **Unpacking** - `x, y = point` is elegant

---

## 📚 Resources

- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [List Comprehensions](https://realpython.com/list-comprehension-python/)

---

## ✅ Day 3 Checklist

- [ ] Perform list operations (append, insert, slice)
- [ ] Work with dictionaries (add, update, iterate)
- [ ] Use list comprehensions instead of loops
- [ ] Write dictionary comprehensions
- [ ] Understand tuples and when to use them
- [ ] Complete the contact manager project

---

## 🎯 Homework

1. Complete all list exercises
2. Complete all dictionary exercises
3. Enhance the contact manager with file persistence
4. **Challenge**: Create a TODO list manager using lists and dictionaries

---

**Tomorrow**: Day 4 - Object-Oriented Python (Classes & Inheritance)

**You're making great progress! 🎉**
