# Day 4 - Exercise 2: Inheritance & Magic Methods

print("=== Exercise 2: Inheritance & Magic Methods ===\n")

# ============================================================
# PART A: Inheritance
# ============================================================
print("--- Part A: Inheritance ---\n")


# Base class (already done for you)
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        return f"{self.brand} {self.model} is starting..."

    def stop(self):
        return f"{self.brand} {self.model} is stopping..."

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


# TODO 1: Create Car class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        pass  # TODO: Call super().__init__() and store num_doors

    def honk(self):
        """Return: 'Toyota Camry goes Beep Beep!'"""
        pass


# TODO 2: Create Motorcycle class that inherits from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar=False):
        pass  # TODO: implement

    def wheelie(self):
        """Return: 'Harley Sportster is doing a wheelie!'"""
        pass


# TODO 3: Create ElectricCar that inherits from Car
class ElectricCar(Car):
    def __init__(self, brand, model, year, num_doors, battery_kwh):
        pass  # TODO: implement

    def charge(self):
        """Return: 'Tesla Model 3 is charging (75 kWh battery)'"""
        pass

    def start(self):
        """Override — electric cars don't rumble!
        Return: 'Tesla Model 3 silently starts...'"""
        pass


# Test Part A (uncomment when ready)
# car = Car("Toyota", "Camry", 2024, 4)
# print(car.start())
# print(car.honk())
# print(car)
#
# moto = Motorcycle("Harley", "Sportster", 2023)
# print(moto.start())
# print(moto.wheelie())
#
# tesla = ElectricCar("Tesla", "Model 3", 2025, 4, 75)
# print(tesla.start())     # Should use overridden version
# print(tesla.charge())
# print(tesla.honk())      # Inherited from Car
#
# print(f"\nisinstance(tesla, Car):     {isinstance(tesla, Car)}")
# print(f"isinstance(tesla, Vehicle): {isinstance(tesla, Vehicle)}")


# ============================================================
# PART B: Magic Methods
# ============================================================
print("\n--- Part B: Magic Methods ---\n")


# TODO 4: Create a Money class with magic methods
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        """Return: '$150.00' or '150.00 EUR'"""
        pass  # TODO: implement

    def __repr__(self):
        """Return: Money(150.00, 'USD')"""
        pass  # TODO: implement

    def __add__(self, other):
        """Add two Money objects (same currency only)"""
        pass  # TODO: implement — return new Money object

    def __sub__(self, other):
        """Subtract two Money objects (same currency only)"""
        pass  # TODO: implement

    def __eq__(self, other):
        """Check if two Money objects are equal"""
        pass  # TODO: implement

    def __lt__(self, other):
        """Compare by amount (same currency only)"""
        pass  # TODO: implement


# Test TODO 4 (uncomment when ready)
# m1 = Money(100)
# m2 = Money(50)
# m3 = Money(100)
# print(m1)             # $100.00
# print(repr(m1))       # Money(100, 'USD')
# print(m1 + m2)        # $150.00
# print(m1 - m2)        # $50.00
# print(m1 == m3)       # True
# print(m1 < m2)        # False


# ============================================================
# PART C: Properties
# ============================================================
print("\n--- Part C: Properties ---\n")


# TODO 5: Create a Circle class with properties
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter for radius"""
        pass  # TODO: return self._radius

    @radius.setter
    def radius(self, value):
        """Setter — only allow positive values"""
        pass  # TODO: validate and set

    @property
    def area(self):
        """Computed property: pi * r^2"""
        pass  # TODO: implement (use 3.14159)

    @property
    def circumference(self):
        """Computed property: 2 * pi * r"""
        pass  # TODO: implement

    def __str__(self):
        """Return: 'Circle(r=5)'"""
        pass


# Test TODO 5 (uncomment when ready)
# c = Circle(5)
# print(c)                           # Circle(r=5)
# print(f"Area:          {c.area:.2f}")           # 78.54
# print(f"Circumference: {c.circumference:.2f}")  # 31.42
# c.radius = 10
# print(f"New area:      {c.area:.2f}")           # 314.16
# c.radius = -5                      # Should raise ValueError


# ============================================================
# CHALLENGE: Create a Playlist class
# ============================================================

# TODO: Create a Song class (title, artist, duration_seconds)
# TODO: Create a Playlist class that:
#   - Has a name and list of songs
#   - __len__ returns number of songs
#   - __add__ combines two playlists into a new one
#   - Has a property 'total_duration' that returns total seconds
#   - Has a method 'longest_song' that returns the longest song

# Test CHALLENGE (uncomment when ready)
# s1 = Song("Bohemian Rhapsody", "Queen", 354)
# s2 = Song("Stairway to Heaven", "Led Zeppelin", 482)
# s3 = Song("Hotel California", "Eagles", 390)
#
# rock = Playlist("Rock Classics")
# rock.add_song(s1)
# rock.add_song(s2)
# print(f"Songs: {len(rock)}")              # 2
# print(f"Duration: {rock.total_duration}s") # 836
# print(f"Longest: {rock.longest_song()}")
