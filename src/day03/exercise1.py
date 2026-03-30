# Day 3 - Exercise 1: Lists

print("=== Exercise 1: Lists ===\n")

# TODO 1: Create a list of your top 5 programming languages
languages = ["c", "python", "javascript", "java", "ruby"]


# Test TODO 1
print(f"Languages: {languages}")


# TODO 2: Add "Go" to the end using append()
languages.append("go")


# Test TODO 2
print(f"After append: {languages}")


# TODO 3: Insert "Rust" at index 2 using insert()
languages.insert(2, "rust")

# Test TODO 3
print(f"After insert: {languages}")


# TODO 4: Remove the first language using pop(0)
languages.pop(0)

# Test TODO 4
print(f"After pop(0): {languages}")


# TODO 5: Find the index of "Python" (if it exists)
# Hint: use .index() but be careful — it errors if not found
index = languages.index("python") if "python" in languages else -1

# Test TODO 5
print(f"Index of Python: {index}")


# TODO 6: Sort the list alphabetically
languages.sort()

# Test TODO 6
print(f"Sorted: {languages}")


# TODO 7: Reverse the list
languages.reverse()

# Test TODO 7
print(f"Reversed: {languages}")


# TODO 8: Create a new list with the last 3 languages using slicing
last_three = languages[-3:]  # Replace with a slice


# Test TODO 8
print(f"Last 3: {last_three}")


# TODO 9: Check if "JavaScript" is in the list
# Use the 'in' operator
has_js = "javascript" in languages


# Test TODO 9
print(f"JavaScript in list: {has_js}")


# TODO 10: Create a list of numbers 1-10 and get only even-indexed numbers using slicing
numbers = list(range(1, 11))
evens = numbers[1::2]  # Hint: numbers[1::2]


# Test TODO 10
print(f"Numbers: {numbers}")
print(f"Evens:   {evens}")


# ============================================================
# CHALLENGE: Combine two lists and remove duplicates
# ============================================================
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
# TODO: Create combined_unique containing all unique values from both
combined_unique = list(set(list_a + list_b))


print(f"\nCHALLENGE - Combined unique: {combined_unique}")
