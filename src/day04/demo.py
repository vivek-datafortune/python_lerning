# Day 4 - Object-Oriented Python Demo
# Run this file to see classes, inheritance & magic methods in action!

print("=== Welcome to Day 4: Object-Oriented Python! ===\n")

# ============================================================
# 1. CREATING A CLASS (JavaScript comparison)
# ============================================================
print("1. Creating a Class:")
print("   JS:     class Person { constructor(name) { this.name = name; } }")
print("   Python: class Person:  def __init__(self, name): self.name = name")
print()


class Person:
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}, {self.age} years old"


# No 'new' keyword needed!
john = Person("Vivek", 30)
jane = Person("Jane", 25)

print(f"   john.greet() → {john.greet()}")
print(f"   jane.greet() → {jane.greet()}")
print(f"   john.name    → {john.name}")
print()

# ============================================================
# 2. CLASS vs INSTANCE VARIABLES
# ============================================================
print("2. Class vs Instance Variables:")


class Dog:
    # Class variable — shared by ALL dogs
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance variables — unique to each dog
        self.name = name
        self.age = age
        self.tricks = []

    def bark(self):
        return f"{self.name} says Woof!"

    def add_trick(self, trick):
        self.tricks.append(trick)


buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

buddy.add_trick("roll over")
buddy.add_trick("shake")
max_dog.add_trick("sit")

print(f"   Dog.species:   {Dog.species}")         # Class variable
print(f"   buddy.species: {buddy.species}")        # Accessible on instance too
print(f"   buddy.name:    {buddy.name}")           # Instance variable
print(f"   buddy.tricks:  {buddy.tricks}")
print(f"   max.tricks:    {max_dog.tricks}")       # Each dog has its own list
print()

# ============================================================
# 3. CLASS VARIABLE COUNTER
# ============================================================
print("3. Class Variable as Counter:")


class Counter:
    count = 0  # Tracks how many instances are created

    def __init__(self, name):
        self.name = name
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


c1 = Counter("First")
c2 = Counter("Second")
c3 = Counter("Third")
print(f"   Created {Counter.get_count()} counters")
print()

# ============================================================
# 4. INHERITANCE — Reusing Code
# ============================================================
print("=" * 50)
print("4. Inheritance:")
print("   JS:     class Dog extends Animal { }")
print("   Python: class Dog(Animal):")
print()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

    def __str__(self):
        return f"{self.__class__.__name__} named {self.name}"


class DogAnimal(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # Call parent constructor
        self.breed = breed

    def speak(self):              # Override parent method
        return "Woof!"

    def fetch(self):              # New method
        return f"{self.name} is fetching!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = DogAnimal("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(f"   dog.speak()  → {dog.speak()}")
print(f"   cat.speak()  → {cat.speak()}")
print(f"   dog.fetch()  → {dog.fetch()}")
print(f"   str(dog)     → {dog}")
print(f"   dog.breed    → {dog.breed}")
print()

# ============================================================
# 5. isinstance & issubclass
# ============================================================
print("5. Type Checking:")
print(f"   isinstance(dog, DogAnimal): {isinstance(dog, DogAnimal)}")
print(f"   isinstance(dog, Animal):    {isinstance(dog, Animal)}")
print(f"   isinstance(cat, DogAnimal): {isinstance(cat, DogAnimal)}")
print(f"   issubclass(DogAnimal, Animal): {issubclass(DogAnimal, Animal)}")
print()

# ============================================================
# 6. POLYMORPHISM — Same interface, different behavior
# ============================================================
print("6. Polymorphism:")
animals = [DogAnimal("Rex", "Poodle"), Cat("Luna"), DogAnimal("Max", "Husky"), Cat("Milo")]

for animal in animals:
    print(f"   {animal} says: {animal.speak()}")
print()

# ============================================================
# 7. MULTIPLE INHERITANCE
# ============================================================
print("7. Multiple Inheritance:")


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
print(f"   duck.walk()  → {duck.walk()}")
print(f"   duck.swim()  → {duck.swim()}")
print(f"   duck.quack() → {duck.quack()}")
print()

# ============================================================
# 8. MAGIC METHODS (Dunder Methods)
# ============================================================
print("=" * 50)
print("8. Magic Methods:")


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # For end users: print(book)
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # For developers: repr(book)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    # len(book) → page count
    def __len__(self):
        return self.pages

    # book1 == book2
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # book1 < book2 (for sorting)
    def __lt__(self, other):
        return self.pages < other.pages

    # book1 + book2 → total pages
    def __add__(self, other):
        return self.pages + other.pages


book1 = Book("Python 101", "John Doe", 300)
book2 = Book("Django Pro", "Jane Smith", 450)

print(f"   str(book1):      {str(book1)}")
print(f"   repr(book1):     {repr(book1)}")
print(f"   len(book1):      {len(book1)}")
print(f"   book1 == book2:  {book1 == book2}")
print(f"   book1 < book2:   {book1 < book2}")
print(f"   book1 + book2:   {book1 + book2} pages")

books = [book2, book1]
books.sort()
print(f"   Sorted:          {[str(b) for b in books]}")
print()

# ============================================================
# 9. PROPERTIES (Getters/Setters the Python way)
# ============================================================
print("9. Properties (@property):")


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


temp = Temperature(25)
print(f"   temp.celsius:    {temp.celsius}")
print(f"   temp.fahrenheit: {temp.fahrenheit}")

temp.celsius = 100
print(f"   After setting to 100°C:")
print(f"   temp.celsius:    {temp.celsius}")
print(f"   temp.fahrenheit: {temp.fahrenheit}")
print()

# ============================================================
# 10. WHY OOP MATTERS FOR DJANGO
# ============================================================
print("=" * 50)
print("10. Why This Matters for Django:")
print("   Django models ARE Python classes:")
print()
print("   class Product(models.Model):")
print("       name = models.CharField(max_length=100)")
print("       price = models.DecimalField(...)")
print()
print("   - __init__  → Django auto-generates it")
print("   - __str__   → What shows in Django admin")
print("   - Inheritance → models.Model gives you DB powers")
print("   - Properties → Computed fields")
print()

print("=== Day 4 Demo Complete! ===")
