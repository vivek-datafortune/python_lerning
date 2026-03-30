# Day 5 - Modules, Packages & Standard Library Demo
# Run this file to see imports, modules & standard library in action!

print("=== Welcome to Day 5: Modules, Packages & Standard Library! ===\n")

# ============================================================
# 1. IMPORTING MODULES
# ============================================================
print("1. Import Styles:")
print("   JS:     import { sqrt } from 'math'")
print("   Python: from math import sqrt")
print()

# Style 1 — import entire module
import math
print(f"   math.sqrt(16)  → {math.sqrt(16)}")
print(f"   math.pi        → {math.pi:.5f}")
print(f"   math.ceil(4.2) → {math.ceil(4.2)}")

# Style 2 — import specific items
from math import sqrt, floor
print(f"   sqrt(25)       → {sqrt(25)}")
print(f"   floor(9.9)     → {floor(9.9)}")

# Style 3 — import with alias
import datetime as dt
now = dt.datetime.now()
print(f"   datetime now   → {now.strftime('%Y-%m-%d %H:%M')}")
print()

# ============================================================
# 2. CREATING YOUR OWN MODULE (inline demo)
# ============================================================
print("2. Creating Your Own Module:")
print("   Save functions in a .py file → import them anywhere")
print()

# Simulating what a module would contain:
def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

print(f"   add(10, 5)    → {add(10, 5)}")
print(f"   is_even(4)    → {is_even(4)}")
print(f"   is_even(7)    → {is_even(7)}")
print()

# ============================================================
# 3. if __name__ == "__main__"
# ============================================================
print("3. if __name__ == '__main__':")
print("   When you run a file directly  → __name__ is '__main__'")
print("   When you import it elsewhere  → __name__ is the module name")
print("   This guard prevents setup code from running on import")
print()

# ============================================================
# 4. os MODULE
# ============================================================
print("=" * 50)
print("4. os Module (filesystem operations):")
import os

print(f"   os.getcwd()          → {os.getcwd()}")
print(f"   os.path.exists('.')  → {os.path.exists('.')}")
print(f"   os.path.join examples:")
print(f"     join('src','day05') → {os.path.join('src', 'day05')}")
print(f"     abspath('.')        → {os.path.abspath('.')}")
print()

# ============================================================
# 5. datetime MODULE
# ============================================================
print("5. datetime Module:")
from datetime import datetime, date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)

print(f"   today           → {today}")
print(f"   tomorrow        → {tomorrow}")
print(f"   last_week       → {last_week}")
print(f"   formatted now   → {datetime.now().strftime('%d %b %Y, %H:%M')}")
print()

# ============================================================
# 6. json MODULE
# ============================================================
print("6. json Module:")
import json

data = {"name": "Vivek", "day": 5, "topics": ["modules", "packages", "stdlib"]}
json_string = json.dumps(data, indent=2)
parsed_back = json.loads(json_string)

print(f"   Original dict  → {data}")
print(f"   json.dumps()   → {json.dumps(data)}")
print(f"   Parsed back    → {parsed_back}")
print(f"   Type after load → {type(parsed_back)}")
print()

# ============================================================
# 7. random MODULE
# ============================================================
print("7. random Module:")
import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"   random.randint(1, 100)        → {random.randint(1, 100)}")
print(f"   random.choice([1..10])        → {random.choice(nums)}")
shuffled = nums[:]
random.shuffle(shuffled)
print(f"   random.shuffle([1..10])       → {shuffled}")
print(f"   random.sample([1..10], k=3)   → {random.sample(nums, 3)}")
print()

# ============================================================
# 8. collections MODULE
# ============================================================
print("8. collections Module:")
from collections import Counter, defaultdict

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(f"   Counter(words)         → {count}")
print(f"   Most common (top 2)    → {count.most_common(2)}")

dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("mango")
dd["vegs"].append("carrot")
print(f"   defaultdict result     → {dict(dd)}")
print()

# ============================================================
# 9. pathlib MODULE
# ============================================================
print("9. pathlib Module (modern path handling):")
from pathlib import Path

p = Path(".")
print(f"   Path('.')          → {p.resolve()}")
print(f"   Path exists        → {p.exists()}")
print(f"   Path / 'day05'     → {(p / 'day05').resolve()}")
print()

print("=== End of Day 5 Demo ===")
print("Next: Exercise 1 — Build your own utility modules!")
