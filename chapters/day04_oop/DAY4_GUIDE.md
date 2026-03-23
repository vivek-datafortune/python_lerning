# Day 4: Object-Oriented Python - Classes, Inheritance & Magic Methods

**Duration**: 3 hours  
**Goal**: Master Python's OOP concepts - essential for Django models

---

## 📋 Learning Objectives

By the end of Day 4, you will:
- ✅ Create classes with `__init__` constructor
- ✅ Understand `self` (like `this` in JavaScript)
- ✅ Implement inheritance and method overriding
- ✅ Use class variables vs instance variables
- ✅ Master magic methods (`__str__`, `__repr__`, etc.)
- ✅ Apply OOP to real-world problems

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: Classes Basics | 30 min | Reading |
| Exercise: Create Classes | 30 min | Coding |
| Theory: Inheritance & Polymorphism | 30 min | Reading |
| Exercise: Inheritance Practice | 30 min | Coding |
| Theory: Magic Methods & Properties | 30 min | Reading |
| Mini-Project: Library System | 30 min | Project |

---

## 🎯 Hour 1: Classes Basics (60 min)

### Creating Classes (30 min)

#### JavaScript vs Python Classes

**JavaScript**:
```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    greet() {
        return `Hi, I'm ${this.name}`;
    }
    
    static species() {
        return "Homo sapiens";
    }
}

const john = new Person("John", 30);
```

**Python**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hi, I'm {self.name}"
    
    @classmethod
    def species(cls):
        return "Homo sapiens"

john = Person("John", 30)  # No 'new' keyword!
```

### Class Concepts

```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self.tricks = []
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    def add_trick(self, trick):
        self.tricks.append(trick)
    
    # String representation
    def __str__(self):
        return f"Dog named {self.name}, age {self.age}"
    
    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

# Creating instances
buddy = Dog("Buddy", 3)
max = Dog("Max", 5)

print(buddy.bark())  # Buddy says Woof!
print(Dog.species)   # Canis familiaris
buddy.add_trick("roll over")
```

### Class vs Instance Variables

```python
class Counter:
    count = 0  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
        Counter.count += 1  # Modify class variable
    
    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter("First")
c2 = Counter("Second")
print(Counter.get_count())  # 2
```

### Practice Exercises (30 min)

Create `day04_classes.py`:

```python
# Exercise 1: Classes

# TODO 1: Create a BankAccount class
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to account"""
        pass  # TODO: implement
    
    def withdraw(self, amount):
        """Remove money from account (if sufficient funds)"""
        pass  # TODO: implement
    
    def get_balance(self):
        """Return current balance"""
        pass  # TODO: implement
    
    def __str__(self):
        """String representation"""
        pass  # TODO: implement

# Test your class
# account = BankAccount("12345", "John Doe", 1000)
# account.deposit(500)
# account.withdraw(200)
# print(account)

# TODO 2: Create a Rectangle class
class Rectangle:
    def __init__(self, width, height):
        pass  # TODO: Store width and height
    
    def area(self):
        """Calculate and return area"""
        pass
    
    def perimeter(self):
        """Calculate and return perimeter"""
        pass
    
    def is_square(self):
        """Return True if it's a square"""
        pass

# TODO 3: Create a Student class with class variable
class Student:
    total_students = 0  # Class variable
    
    def __init__(self, name, grade):
        pass  # TODO: Store name, grade, and increment total_students
    
    @classmethod
    def get_total_students(cls):
        """Return total number of students"""
        pass
```

---

## 🎯 Hour 2: Inheritance & Polymorphism (60 min)

### Inheritance (30 min)

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"
    
    def __str__(self):
        return f"{self.__class__.__name__} named {self.name}"

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed
    
    # Override parent method
    def speak(self):
        return "Woof!"
    
    # Add new method
    def fetch(self):
        return f"{self.name} is fetching!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
print(dog.fetch())  # Buddy is fetching!

# Check inheritance
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True
```

### Multiple Inheritance

```python
class Walkable:
    def walk(self):
        return "Walking..."

class Swimmable:
    def swim(self):
        return "Swimming..."

class Duck(Walkable, Swimmable):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.walk())   # Walking...
print(duck.swim())   # Swimming...
print(duck.quack())  # Quack!
```

### Practice Exercises (30 min)

Create `day04_inheritance.py`:

```python
# Exercise 2: Inheritance

# TODO 1: Create a base Vehicle class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        return f"{self.brand} {self.model} is starting..."
    
    def stop(self):
        return f"{self.brand} {self.model} is stopping..."

# TODO 2: Create Car class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        pass  # TODO: Call parent __init__ and store num_doors
    
    def honk(self):
        """Car-specific method"""
        pass

# TODO 3: Create Motorcycle class that inherits from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        pass  # TODO: implement
    
    def wheelie(self):
        """Motorcycle-specific method"""
        pass

# TODO 4: Create ElectricCar that inherits from Car
class ElectricCar(Car):
    def __init__(self, brand, model, year, num_doors, battery_capacity):
        pass  # TODO: implement
    
    def charge(self):
        """Electric car specific method"""
        pass

# Test your classes
# car = Car("Toyota", "Camry", 2024, 4)
# print(car.start())
# print(car.honk())
```

---

## 🎯 Hour 3: Magic Methods & Mini-Project (60 min)

### Magic Methods (Dunder Methods) (30 min)

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation (for end users)
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # Developer representation (for debugging)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Length
    def __len__(self):
        return self.pages
    
    # Equality
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # Less than (for sorting)
    def __lt__(self, other):
        return self.pages < other.pages
    
    # Addition
    def __add__(self, other):
        # Combine pages when adding books
        return self.pages + other.pages

book1 = Book("Python 101", "John Doe", 300)
book2 = Book("Django Pro", "Jane Smith", 450)

print(str(book1))      # 'Python 101' by John Doe
print(repr(book1))     # Book('Python 101', 'John Doe', 300)
print(len(book1))      # 300
total = book1 + book2  # 750

# Sorting
books = [book2, book1]
books.sort()  # Sorts by pages using __lt__
```

### Properties (Getters/Setters)

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
temp.celsius = 30       # Uses setter
```

### Mini-Project: Library Management System (30 min)

Create `day04_library_system.py`:

```python
# Mini-Project: Library Management System

class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.borrowed = 0
    
    def available_copies(self):
        return self.copies - self.borrowed
    
    def checkout(self):
        if self.available_copies() > 0:
            self.borrowed += 1
            return True
        return False
    
    def return_book(self):
        if self.borrowed > 0:
            self.borrowed -= 1
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies()} available)"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.checkout():
            self.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"✓ Added: {book.title}")
    
    def register_member(self, member):
        self.members.append(member)
        print(f"✓ Registered: {member.name}")
    
    def list_books(self):
        print(f"\n=== {self.name} - Available Books ===")
        for book in self.books:
            if book.available_copies() > 0:
                print(f"  {book}")
    
    def find_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        return None

# Main program
library = Library("City Library")

# Add books
library.add_book(Book("Python Crash Course", "Eric Matthes", "123", 3))
library.add_book(Book("Django for APIs", "William Vincent", "456", 2))
library.add_book(Book("Clean Code", "Robert Martin", "789", 1))

# Register members
alice = Member("Alice Johnson", "M001")
bob = Member("Bob Smith", "M002")
library.register_member(alice)
library.register_member(bob)

# Borrow books
book = library.find_book("Python")
if book and alice.borrow_book(book):
    print(f"\n✓ {alice.name} borrowed {book.title}")

# List available books
library.list_books()

# Return books
alice.return_book(book)
print(f"\n✓ {alice.name} returned {book.title}")

library.list_books()

# TODO: Add menu system like previous projects
# TODO: Add search functionality
# TODO: Add overdue tracking with dates
```

---

## 🔍 Key Takeaways

### Python OOP vs JavaScript

| Feature | JavaScript | Python |
|---------|-----------|--------|
| Constructor | `constructor()` | `__init__()` |
| This/Self | `this` | `self` |
| Inheritance | `extends` | Class name in parentheses |
| Super | `super.method()` | `super().method()` |
| Static method | `static` | `@classmethod` |
| New instance | `new Class()` | `Class()` (no new) |

### Important Concepts

1. **`self` is explicit** - First parameter of instance methods
2. **`__init__` is constructor** - Called when creating instance
3. **Magic methods** - Special methods with `__name__`
4. **Class vs instance variables** - Shared vs unique data
5. **Properties** - Use `@property` for computed attributes

---

## 📚 Resources

- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [Magic Methods Guide](https://rszalski.github.io/magicmethods/)
- [Real Python OOP](https://realpython.com/python3-object-oriented-programming/)

---

## ✅ Day 4 Checklist

- [ ] Create classes with `__init__`
- [ ] Understand `self` parameter
- [ ] Implement inheritance with `super()`
- [ ] Use magic methods (`__str__`, `__repr__`)
- [ ] Differentiate class vs instance variables
- [ ] Complete the library system project

---

## 🎯 Homework

1. Complete all class exercises
2. Complete inheritance exercises
3. Enhance library system with menu and features
4. **Challenge**: Create a simple RPG game with Player, Enemy, and Item classes

---

**Tomorrow**: Day 5 - Python Modules, Packages & Virtual Environments

**OOP is crucial for Django - you're doing great! 💪**
