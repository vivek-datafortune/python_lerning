# Day 5 - Exercise 2: Packages, Virtual Environments & Advanced Imports

print("=== Exercise 2: Packages & Advanced Imports ===\n")

# ============================================================
# PART A: Package Structure
# ============================================================
# A package is a folder with an __init__.py file.
# It lets you group related modules together.
#
# Example structure you should be able to build mentally:
#
#   myapp/
#     __init__.py           ← makes the folder a package
#     models.py
#     utils.py
#     services/
#       __init__.py
#       email_service.py
#       sms_service.py
#
# Imports from outside would look like:
#   from myapp.models import User
#   from myapp.services.email_service import send_email

print("--- Part A: Understanding Packages ---\n")
print("Think about how you'd structure a small web app into modules.")
print("Answer these questions (in the comments below):")
print()

# Q1: What file MUST exist inside a folder to make it a Python package?
# Answer: TODO

# Q2: If you have myapp/utils.py and you're in main.py (at the root),
#     how would you import a function called 'slugify' from utils.py?
# Answer: TODO

# Q3: What does the __init__.py file allow you to do when someone
#     imports the package directly (e.g. 'import myapp')?
# Answer: TODO


# ============================================================
# PART B: Relative vs Absolute Imports
# ============================================================
print("--- Part B: Import Styles Practice ---\n")

# Given this package layout:
#
#   analytics/
#     __init__.py
#     stats.py         (has: def mean(data): ...)
#     charts.py        (has: def bar_chart(data): ...)
#     helpers/
#       __init__.py
#       formatters.py  (has: def format_pct(value): ...)

# TODO 1: Write the absolute import statement to import 'mean' from stats.py
#         (pretend you are in main.py at the project root)
# Your import: TODO

# TODO 2: Write the absolute import to get 'format_pct' from formatters.py
# Your import: TODO

# TODO 3: If you're INSIDE charts.py and want to import 'mean' from stats.py
#         in the same package, write the RELATIVE import.
# Your import: TODO  (hint: use . for current package)


# ============================================================
# PART C: requirements.txt & pip (concept questions)
# ============================================================
print("--- Part C: pip & Virtual Environments ---\n")
print("Map these npm commands to their pip equivalents:\n")

commands = {
    "npm install express":        "TODO: pip equivalent",
    "npm install":                "TODO: pip equivalent",
    "npm uninstall express":      "TODO: pip equivalent",
    "npm list":                   "TODO: pip equivalent",
    "cat package.json":           "TODO: pip equivalent (show installed deps)",
    "npm init (creates pkg.json)":"TODO: pip equivalent (save deps to file)",
}

for npm_cmd, pip_cmd in commands.items():
    print(f"  {npm_cmd}")
    print(f"    → {pip_cmd}")
    print()

# TODO: Fill in the pip equivalents above


# ============================================================
# PART D: Virtual Environment Checklist
# ============================================================
print("--- Part D: Virtual Environment Steps ---\n")
print("Put these steps in the correct order by numbering them 1-6.")
print()

steps = [
    "[ ] pip install -r requirements.txt",
    "[ ] source venv/bin/activate  (or venv\\Scripts\\activate on Windows)",
    "[ ] mkdir my_project && cd my_project",
    "[ ] pip freeze > requirements.txt",
    "[ ] python -m venv venv",
    "[ ] pip install django requests",
]

for step in steps:
    print(f"  {step}")

print()
print("Correct order: TODO (write numbers 1-6 next to each step above)")


# ============================================================
# PART E: Practical — Explore Your Own Environment
# ============================================================
print("--- Part E: Inspect Your Environment ---\n")

import sys
import os

# TODO 4: Print all directories Python searches for modules (sys.path)
# Your code here:


# TODO 5: Print the Python version you are using
# Your code here:


# TODO 6: Print out all .py files in the current directory using os.listdir
# Your code here:


# TODO 7: Using os.path, check if a 'requirements.txt' exists two levels up
#         from the current file's location. Print True or False.
# Hint: use __file__, os.path.dirname, and os.path.exists
# Your code here:
