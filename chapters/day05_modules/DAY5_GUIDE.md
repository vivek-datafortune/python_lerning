# Day 5: Python Modules, Packages & Virtual Environments

**Duration**: 3 hours  
**Goal**: Master Python's module system and dependency management

---

## 📋 Learning Objectives

By the end of Day 5, you will:
- ✅ Import and use Python modules
- ✅ Create your own modules
- ✅ Understand Python packages
- ✅ Master virtual environments (like node_modules)
- ✅ Use pip for package management (like npm)
- ✅ Work with requirements.txt
- ✅ Understand common standard library modules

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: Modules & Imports | 30 min | Reading |
| Exercise: Create Modules | 30 min | Coding |
| Theory: Packages & Virtual Envs | 30 min | Reading |
| Exercise: Package Management | 30 min | Hands-on |
| Theory: Standard Library | 30 min | Reading |
| Mini-Project: File Organizer | 30 min | Project |

---

## 🎯 Hour 1: Modules & Imports (60 min)

### Understanding Modules (30 min)

#### JavaScript vs Python Modules

**JavaScript (ES6)**:
```javascript
// math_utils.js
export function add(a, b) {
    return a + b;
}

// main.js
import { add } from './math_utils.js';
console.log(add(2, 3));
```

**Python**:
```python
# math_utils.py
def add(a, b):
    return a + b

# main.py
from math_utils import add
print(add(2, 3))
```

### Import Styles

```python
# 1. Import entire module
import math
print(math.sqrt(16))  # 4.0

# 2. Import specific items
from math import sqrt, pi
print(sqrt(16))
print(pi)

# 3. Import with alias
import datetime as dt
now = dt.datetime.now()

# 4. Import all (NOT RECOMMENDED)
from math import *

# 5. Import multiple items
from os import path, listdir, getcwd

# 6. Import from subdirectory
from myapp.utils import helper_function
```

### Creating Your Own Modules

Create `calculator.py`:
```python
"""
Calculator module for basic math operations.
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# This runs only when file is executed directly
if __name__ == "__main__":
    print("Calculator module")
    print(f"5 + 3 = {add(5, 3)}")
```

Use it from another file:
```python
# main.py
from calculator import add, multiply

result = add(10, 5)
print(result)
```

### Practice Exercises (30 min)

Create `day05_modules/`:
```
day05_modules/
  ├── string_utils.py
  ├── math_utils.py
  └── main.py
```

`string_utils.py`:
```python
# TODO 1: Create a function to capitalize first letter of each word
def title_case(text):
    pass

# TODO 2: Create a function to count vowels in a string
def count_vowels(text):
    pass

# TODO 3: Create a function to reverse a string
def reverse_string(text):
    pass

if __name__ == "__main__":
    # Test your functions
    print(title_case("hello world"))
    print(count_vowels("hello"))
    print(reverse_string("python"))
```

`math_utils.py`:
```python
# TODO 1: Create a function to check if number is prime
def is_prime(n):
    pass

# TODO 2: Create a function to get factorial
def factorial(n):
    pass

# TODO 3: Create a function to get fibonacci sequence
def fibonacci(n):
    """Return first n fibonacci numbers"""
    pass
```

`main.py`:
```python
# TODO: Import and use functions from both modules
from string_utils import title_case, count_vowels
from math_utils import is_prime, factorial

# Test them
```

---

## 🎯 Hour 2: Packages & Virtual Environments (60 min)

### Python Packages (30 min)

#### Package Structure

```
myproject/
  ├── mypackage/
  │   ├── __init__.py      # Makes it a package
  │   ├── module1.py
  │   ├── module2.py
  │   └── subpackage/
  │       ├── __init__.py
  │       └── module3.py
  └── main.py
```

`mypackage/__init__.py`:
```python
# This file can be empty or contain initialization code
from .module1 import function1
from .module2 import function2

__version__ = "1.0.0"
```

Using the package:
```python
# From main.py
from mypackage import function1
from mypackage.module2 import function2
from mypackage.subpackage import module3
```

### Virtual Environments (30 min)

#### Why Virtual Environments?

**JavaScript**: Each project has `node_modules/` with isolated dependencies
**Python**: Each project needs a virtual environment for isolated packages

#### Creating Virtual Environments

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# You should see (venv) in your prompt

# Deactivate
deactivate
```

#### pip (Python Package Manager)

```bash
# Install package
pip install requests

# Install specific version
pip install django==5.0

# Install multiple packages
pip install django djangorestframework

# Upgrade package
pip install --upgrade django

# Uninstall package
pip uninstall requests

# List installed packages
pip list

# Show package details
pip show django

# Freeze dependencies (like package.json)
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

#### requirements.txt

```txt
# requirements.txt
django>=5.0,<6.0
djangorestframework>=3.14
requests==2.31.0
python-dotenv>=1.0.0

# Development dependencies
# pytest>=7.0
# black>=23.0
```

### Practice Exercise (Hands-on)

Create `day05_venv_practice/`:

```bash
# 1. Create new directory
mkdir day05_venv_practice
cd day05_venv_practice

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate

# 4. Install some packages
pip install requests colorama

# 5. Create requirements.txt
pip freeze > requirements.txt

# 6. Check what you installed
pip list

# 7. Deactivate
deactivate
```

---

## 🎯 Hour 3: Standard Library & Mini-Project (60 min)

### Common Standard Library Modules (30 min)

```python
# 1. os - Operating system interface
import os

current_dir = os.getcwd()
files = os.listdir('.')
os.path.exists('file.txt')
os.path.join('folder', 'file.txt')
os.makedirs('new_folder', exist_ok=True)

# 2. sys - System-specific parameters
import sys

print(sys.version)
print(sys.argv)  # Command line arguments
sys.exit(0)

# 3. datetime - Date and time
from datetime import datetime, date, timedelta

now = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)
formatted = now.strftime("%Y-%m-%d %H:%M:%S")

# 4. json - JSON encoder/decoder
import json

data = {"name": "John", "age": 30}
json_string = json.dumps(data)
parsed = json.loads(json_string)

# 5. random - Random number generation
import random

num = random.randint(1, 100)
choice = random.choice(['a', 'b', 'c'])
random.shuffle(my_list)

# 6. pathlib - Object-oriented filesystem paths
from pathlib import Path

path = Path('folder/file.txt')
if path.exists():
    content = path.read_text()
path.write_text('Hello world')

# 7. collections - Specialized container datatypes
from collections import Counter, defaultdict, namedtuple

count = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})

# 8. itertools - Iterator functions
from itertools import count, cycle, repeat

for i in count(10):  # 10, 11, 12, ...
    if i > 15:
        break

# 9. re - Regular expressions
import re

pattern = r'\d+'  # One or more digits
matches = re.findall(pattern, 'abc123def456')
# ['123', '456']

# 10. urllib - URL handling
from urllib.parse import urlparse

url = urlparse('https://example.com/path?query=value')
print(url.scheme, url.netloc, url.path)
```

### Mini-Project: File Organizer (30 min)

Create `day05_file_organizer/file_organizer.py`:

```python
"""
File Organizer - Organize files by extension
"""
import os
from pathlib import Path
import shutil
from datetime import datetime

class FileOrganizer:
    def __init__(self, target_directory):
        self.target_dir = Path(target_directory)
        self.file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
            'Audio': ['.mp3', '.wav', '.flac'],
            'Archives': ['.zip', '.rar', '.7z', '.tar'],
            'Code': ['.py', '.js', '.html', '.css', '.java']
        }
    
    def organize(self):
        """Organize files in target directory"""
        if not self.target_dir.exists():
            print(f"Directory {self.target_dir} does not exist!")
            return
        
        # Create category folders
        for category in self.file_types.keys():
            category_path = self.target_dir / category
            category_path.mkdir(exist_ok=True)
        
        # Move files
        for file_path in self.target_dir.iterdir():
            if file_path.is_file():
                self.move_file(file_path)
        
        print("✓ Organization complete!")
    
    def move_file(self, file_path):
        """Move file to appropriate category folder"""
        extension = file_path.suffix.lower()
        
        # Find category
        for category, extensions in self.file_types.items():
            if extension in extensions:
                destination = self.target_dir / category / file_path.name
                
                # Handle duplicate names
                if destination.exists():
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    name = file_path.stem
                    destination = self.target_dir / category / f"{name}_{timestamp}{extension}"
                
                shutil.move(str(file_path), str(destination))
                print(f"Moved: {file_path.name} → {category}/")
                return
        
        # If no category found, move to Others
        others_path = self.target_dir / "Others"
        others_path.mkdir(exist_ok=True)
        destination = others_path / file_path.name
        shutil.move(str(file_path), str(destination))
        print(f"Moved: {file_path.name} → Others/")
    
    def list_files(self):
        """List all files in target directory"""
        print(f"\nFiles in {self.target_dir}:")
        for item in self.target_dir.rglob('*'):
            if item.is_file():
                print(f"  {item.relative_to(self.target_dir)}")

# Main program
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("Enter directory to organize: ")
    
    organizer = FileOrganizer(directory)
    
    print(f"Organizing files in: {directory}")
    print("Press Enter to continue or Ctrl+C to cancel...")
    input()
    
    organizer.organize()
    organizer.list_files()

# TODO: Add undo functionality
# TODO: Add configuration file for custom categories
# TODO: Add dry-run mode (preview without moving)
```

Usage:
```bash
python file_organizer.py "C:/Users/username/Downloads"
```

---

## 🔍 Key Takeaways

### Python vs JavaScript Modules

| Feature | JavaScript (Node) | Python |
|---------|------------------|--------|
| Import | `import/require` | `import/from` |
| Export | `export/module.exports` | Just define functions |
| Package manager | `npm/yarn` | `pip` |
| Dependencies file | `package.json` | `requirements.txt` |
| Local packages | `node_modules/` | `venv/` (virtual env) |

### Important Concepts

1. **`__name__ == "__main__"`** - Runs only when executed directly
2. **`__init__.py`** - Makes directory a package
3. **Virtual environments** - Isolate project dependencies
4. **pip freeze** - Like package-lock.json
5. **Standard library** - Rich built-in modules

---

## 📚 Resources

- [Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Standard Library](https://docs.python.org/3/library/)
- [pip Documentation](https://pip.pypa.io/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

---

## ✅ Day 5 Checklist

- [ ] Create and import custom modules
- [ ] Understand `__init__.py` for packages
- [ ] Create and activate virtual environments
- [ ] Use pip to install/uninstall packages
- [ ] Create requirements.txt
- [ ] Use common standard library modules
- [ ] Complete file organizer project

---

## 🎯 Homework

1. Create a package with multiple modules
2. Experiment with standard library modules
3. Enhance file organizer with more features
4. **Challenge**: Create a command-line tool that uses external packages (requests, colorama)

---

**Tomorrow**: Day 6 - Django Setup & First Project

**You're ready for Django! 🚀**
