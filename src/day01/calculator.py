# Day 1 - Mini Project: Simple Calculator

print("=== Simple Calculator ===\n")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition       = num1 + num2
subtraction    = num1 - num2
multiplication = num1 * num2
division       = num1 / num2 if num2 != 0 else "Cannot divide by zero"

print(f"\nResults:")
print(f"  {num1} + {num2} = {addition}")
print(f"  {num1} - {num2} = {subtraction}")
print(f"  {num1} * {num2} = {multiplication}")
print(f"  {num1} / {num2} = {division}")

# BONUS: Uncomment these lines to add more operations
# power  = num1 ** num2
# modulo = num1 % num2
# print(f"  {num1} ** {num2} = {power}")
# print(f"  {num1} % {num2}  = {modulo}")
