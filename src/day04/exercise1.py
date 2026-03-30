# Day 4 - Exercise 1: Classes

print("=== Exercise 1: Classes ===\n")

# ============================================================
# TODO 1: Create a BankAccount class
# ============================================================

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to account. Only allow positive amounts."""
        pass  # TODO: implement

    def withdraw(self, amount):
        """Remove money (only if sufficient funds). Return True/False."""
        pass  # TODO: implement

    def get_balance(self):
        """Return current balance"""
        pass  # TODO: implement

    def __str__(self):
        """Return: 'Account 12345 (John Doe): $1000.00'"""
        pass  # TODO: implement


# Test TODO 1 (uncomment when ready)
# account = BankAccount("12345", "John Doe", 1000)
# account.deposit(500)
# print(account.get_balance())   # Expected: 1500
# account.withdraw(200)
# print(account.get_balance())   # Expected: 1300
# account.withdraw(5000)         # Should fail — not enough funds
# print(account)                 # Account 12345 (John Doe): $1300.00


# ============================================================
# TODO 2: Create a Rectangle class
# ============================================================

class Rectangle:
    def __init__(self, width, height):
        pass  # TODO: Store width and height

    def area(self):
        """Return width * height"""
        pass

    def perimeter(self):
        """Return 2 * (width + height)"""
        pass

    def is_square(self):
        """Return True if width == height"""
        pass

    def __str__(self):
        """Return: 'Rectangle(5x10)'"""
        pass


# Test TODO 2 (uncomment when ready)
# rect = Rectangle(5, 10)
# print(f"Area:      {rect.area()}")        # Expected: 50
# print(f"Perimeter: {rect.perimeter()}")   # Expected: 30
# print(f"Is square: {rect.is_square()}")   # Expected: False
# square = Rectangle(5, 5)
# print(f"Is square: {square.is_square()}")  # Expected: True
# print(rect)                                # Rectangle(5x10)


# ============================================================
# TODO 3: Create a Student class with class variable
# ============================================================

class Student:
    total_students = 0  # Class variable — tracks all students

    def __init__(self, name, grade):
        pass  # TODO: Store name, grade, and increment total_students

    @classmethod
    def get_total_students(cls):
        """Return total number of students created"""
        pass

    def is_passing(self):
        """Return True if grade >= 60"""
        pass

    def __str__(self):
        """Return: 'Student: Alice (Grade: 85)'"""
        pass


# Test TODO 3 (uncomment when ready)
# s1 = Student("Alice", 85)
# s2 = Student("Bob", 55)
# s3 = Student("Charlie", 72)
# print(f"Total students: {Student.get_total_students()}")  # Expected: 3
# print(f"{s1} - Passing: {s1.is_passing()}")  # True
# print(f"{s2} - Passing: {s2.is_passing()}")  # False


# ============================================================
# CHALLENGE: Create a TodoItem class
# ============================================================

# TODO: Create a TodoItem class with:
# - Properties: title, completed (default False)
# - Method: toggle() — flips completed
# - Method: __str__() — shows "[x] title" or "[ ] title"
# - Class variable: total_todos


# Test CHALLENGE (uncomment when ready)
# t1 = TodoItem("Learn Python")
# t2 = TodoItem("Build Django app")
# print(t1)         # [ ] Learn Python
# t1.toggle()
# print(t1)         # [x] Learn Python
# print(f"Total todos: {TodoItem.total_todos}")  # 2
