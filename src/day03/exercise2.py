# Day 3 - Exercise 2: Dictionaries, Tuples & Sets

print("=== Exercise 2: Dictionaries, Tuples & Sets ===\n")

# ============================================================
# PART A: Dictionaries
# ============================================================
print("--- Part A: Dictionaries ---\n")

# TODO 1: Create a dictionary representing a book
# Add: title, author, year, pages, rating
book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "pages": 218,
    "rating": 4.2
}


# Test TODO 1
print(f"Book: {book}")


# TODO 2: Add a key "isbn" with any value
book["isbn"] = "978-0743273565"

# Test TODO 2
print(f"After adding isbn: {book}")


# TODO 3: Update the rating to a new value
book["rating"] = 4.5  # Update to new rating

# Test TODO 3
print(f"After updating rating: {book.get('rating')}")


# TODO 4: Get the author using .get() method
author = book.get("author")


# Test TODO 4
print(f"Author: {author}")


# TODO 5: Check if "publisher" key exists
# Use the 'in' operator
has_publisher = "publisher" in book

# Test TODO 5
print(f"Has publisher: {has_publisher}")


# TODO 6: Print all keys
print(f"Keys: {list(book.keys())}")


# TODO 7: Print all values
print(f"Values: {list(book.values())}")


# TODO 8: Loop through all key-value pairs using .items()
print("All entries:")
for key, value in book.items():
    print(f"  {key}: {value}")


# TODO 9: Create a dictionary of students and their grades
# Start with Alice: 85, Bob: 92, Charlie: 78, then add 3 more
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}


# Test TODO 9
print(f"\nStudents: {students}")


# TODO 10: Calculate average grade using sum() and len()
# Hint: sum(students.values()) / len(students)
average = sum(students.values()) / len(students)

# Test TODO 10
print(f"Average grade: {average:.2f}")


# ============================================================
# PART B: Tuples
# ============================================================
print("\n--- Part B: Tuples ---\n")

# TODO 11: Create a tuple for RGB color (255, 128, 0) and unpack it
rgb = (255, 128, 0)
r, g, b = rgb


# Test TODO 11
print(f"r={r}, g={g}, b={b}")


# TODO 12: Write a function that returns min, max, and average of a list
def list_stats(numbers):
    # Return (min_val, max_val, average) as a tuple
    if not numbers:
        return (None, None, None)
    min_val = min(numbers)
    max_val = max(numbers)
    average = sum(numbers) / len(numbers)
    return (min_val, max_val, average)


# Test TODO 12
test_nums = [4, 8, 2, 9, 1, 5]
low, high, avg = list_stats(test_nums)
print(f"Stats of {test_nums}: min={low}, max={high}, avg={avg}")
