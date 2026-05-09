# Python Classes & Object-Oriented Programming
### A Complete Structured Course

---

## Table of Contents

**Part I – Python Classes: Core Concepts**
1. Introduction to Classes
2. Instance Attributes
3. Class Attributes
4. Methods in Classes
5. Class Methods
6. Static Methods
7. Special (Magic/Dunder) Methods
8. Properties and Encapsulation
9. Object Introspection
10. Composition (Has-A Relationship)
11. Mini Class Project – Bank Account

**Part II – Object-Oriented Programming Concepts**
1. Introduction to OOP
2. Inheritance
3. Polymorphism
4. Abstraction
5. Advanced OOP Concepts
6. Mini Projects Using OOP

---

# PART I – Python Classes: Core Concepts

---

## 1. Introduction to Classes

### What is a Class?

A **class** is a blueprint or template used to create objects. It defines the structure (attributes) and behavior (methods) that all objects of that type will share. Think of a class like an architectural plan: the plan itself isn't a house, but you can use it to build many houses.

```python
class Dog:
    pass  # An empty class — valid Python
```

### Difference Between Class and Object

| Concept | Description | Example |
|--------|-------------|---------|
| **Class** | The blueprint/template | `Dog` |
| **Object** | A specific instance created from the class | `my_dog = Dog()` |

A class is defined once. Objects (instances) are created from it as many times as needed, each potentially holding different data.

### Creating a Simple Class

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def describe(self):
        return f"A {self.color} {self.brand}"
```

### Instantiating Objects

```python
car1 = Car("Toyota", "red")
car2 = Car("Honda", "blue")

print(car1.describe())  # A red Toyota
print(car2.describe())  # A blue Honda
```

Each call to `Car(...)` creates a **new, independent object** in memory.

---

## 2. Instance Attributes

### Definition and Use

**Instance attributes** are variables that belong to a specific object (instance). Every object has its own copy of these attributes, independent of other objects.

### Setting Attributes in `__init__`

The `__init__` method is the **constructor** — it runs automatically when an object is created. Use it to initialize instance attributes:

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name      # instance attribute
        self.age = age        # instance attribute
        self.grade = grade    # instance attribute
```

### Accessing and Modifying Instance Attributes

```python
s1 = Student("Alice", 20, "A")
s2 = Student("Bob", 22, "B")

# Accessing
print(s1.name)    # Alice
print(s2.age)     # 22

# Modifying
s1.grade = "A+"
print(s1.grade)   # A+
print(s2.grade)   # B  (unchanged — independent)
```

> **Key point:** Modifying `s1.grade` has no effect on `s2.grade`. They are separate objects.

---

## 3. Class Attributes

### Difference from Instance Attributes

**Class attributes** are defined at the class level (outside `__init__`) and are **shared by all instances**.

```python
class Employee:
    company = "TechCorp"       # class attribute (shared)
    employee_count = 0         # class attribute (shared)

    def __init__(self, name, salary):
        self.name = name       # instance attribute
        self.salary = salary   # instance attribute
        Employee.employee_count += 1
```

### Shared Data Across Objects

```python
e1 = Employee("Grace", 80000)
e2 = Employee("James", 90000)

print(e1.company)            # TechCorp
print(e2.company)            # TechCorp
print(Employee.employee_count)  # 2
```

### Use Cases and Examples

- Tracking a count of how many objects have been created
- Storing constants shared by all instances (e.g., tax rate, company name)
- Default values that rarely change

```python
class BankAccount:
    interest_rate = 0.035  # 3.5% for all accounts

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate
```

---

## 4. Methods in Classes

### Instance Methods

**Instance methods** are the most common type. They operate on the data of a specific instance and always take `self` as the first parameter.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def scale(self, factor):
        self.width *= factor
        self.height *= factor
```

### Method Parameters (`self`)

`self` refers to the **current object** calling the method. Python passes it automatically — you never supply it yourself when calling a method.

```python
rect = Rectangle(4, 6)
print(rect.area())       # 24
print(rect.perimeter())  # 20

rect.scale(2)
print(rect.area())       # 96
```

### Calling Methods on Objects

```python
r1 = Rectangle(3, 5)
r2 = Rectangle(7, 2)

# Each call operates on that specific object's data
print(r1.area())   # 15
print(r2.area())   # 14
```

---

## 5. Class Methods

### `@classmethod` Decorator

A **class method** is bound to the class, not the instance. It receives `cls` (the class itself) as its first argument instead of `self`.

```python
class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor using birth year"""
        import datetime
        age = datetime.date.today().year - birth_year
        return cls(name, age)
```

### Using `cls` Parameter

`cls` refers to the class itself, not an instance. This allows class methods to:
- Access and modify class attributes
- Serve as **alternative constructors** (factory methods)

```python
p1 = Person("Amara", 28)
p2 = Person.from_birth_year("Tunde", 1995)

print(Person.get_population())  # 2
print(p2.age)                   # calculated from birth year
```

### Use Cases for Class Methods

- Factory/alternative constructors (create objects in different ways)
- Modifying or reading class-level state
- Named constructors that improve readability

---

## 6. Static Methods

### `@staticmethod` Decorator

A **static method** belongs to the class namespace but doesn't receive `self` or `cls`. It's essentially a regular function grouped inside a class for logical organization.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
```

### Utility Functions Inside a Class

```python
print(MathUtils.add(3, 7))                   # 10
print(MathUtils.is_even(4))                  # True
print(MathUtils.celsius_to_fahrenheit(100))  # 212.0
```

### Difference from Instance and Class Methods

| Feature | Instance Method | Class Method | Static Method |
|--------|----------------|--------------|---------------|
| First param | `self` | `cls` | None |
| Accesses instance? | ✅ Yes | ❌ No | ❌ No |
| Accesses class? | ✅ (via `self.__class__`) | ✅ Yes | ❌ No |
| Use case | Work with object data | Factory / class state | Utility functions |

---

## 7. Special (Magic/Dunder) Methods

### What Are Magic Methods?

Magic methods (also called **dunder methods**, short for "double underscore") let you customize how Python's built-in operations work with your objects. They're defined with `__double_underscores__`.

### Key Magic Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Human-readable string — used by print()"""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Developer/debug representation"""
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        """Enables v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """Enables v1 == v2"""
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """Enables len(v)"""
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

    def __mul__(self, scalar):
        """Enables v * 3"""
        return Vector(self.x * scalar, self.y * scalar)
```

### Examples

```python
v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(v1)           # Vector(2, 3)     → uses __str__
print(repr(v1))     # Vector(x=2, y=3) → uses __repr__
print(v1 + v2)      # Vector(3, 7)     → uses __add__
print(v1 == v2)     # False            → uses __eq__
print(v1 * 2)       # Vector(4, 6)     → uses __mul__
```

### Common Magic Methods Reference

| Method | Triggered by | Purpose |
|--------|-------------|---------|
| `__init__` | `MyClass()` | Constructor |
| `__str__` | `print(obj)`, `str(obj)` | Readable string |
| `__repr__` | `repr(obj)`, REPL display | Debug string |
| `__len__` | `len(obj)` | Return length |
| `__add__` | `obj + other` | Addition |
| `__sub__` | `obj - other` | Subtraction |
| `__mul__` | `obj * other` | Multiplication |
| `__eq__` | `obj == other` | Equality check |
| `__lt__` | `obj < other` | Less than |
| `__contains__` | `x in obj` | Membership test |
| `__getitem__` | `obj[key]` | Index/key access |
| `__iter__` | `for x in obj` | Iteration |

---

## 8. Properties and Encapsulation

### Private vs Public Attributes

Python uses naming conventions to signal access intent:

| Convention | Meaning | Example |
|-----------|---------|---------|
| `name` | Public — freely accessible | `self.name` |
| `_name` | Protected — "internal use" (convention only) | `self._name` |
| `__name` | Private — name-mangled by Python | `self.__name` |

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._account_type = "savings"  # protected
        self.__balance = balance    # private (name-mangled)
```

### Getters and Setters with `@property`

The `@property` decorator lets you define **computed attributes** and attach **validation logic**:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed property — no setter needed"""
        return (self._celsius * 9/5) + 32
```

```python
t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0

t.celsius = 100
print(t.fahrenheit)   # 212.0

t.celsius = -300      # ❌ Raises ValueError
```

### Encapsulation Best Practices

- Hide internal implementation details
- Expose only what external code needs
- Use `@property` for controlled attribute access
- Validate data in setters to maintain object integrity

---

## 9. Object Introspection

Python lets you examine objects at runtime using built-in functions:

```python
class Animal:
    species = "Unknown"

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

dog = Animal("Rex")
```

### Key Introspection Tools

```python
# Check type
print(type(dog))                    # <class '__main__.Animal'>

# Check inheritance
print(isinstance(dog, Animal))      # True
print(isinstance(dog, str))         # False

# Check if attribute/method exists
print(hasattr(dog, "name"))         # True
print(hasattr(dog, "fly"))          # False

# Get attribute value dynamically
print(getattr(dog, "name"))         # Rex
print(getattr(dog, "color", "brown"))  # brown (default)

# Set attribute dynamically
setattr(dog, "color", "black")
print(dog.color)                    # black

# Inspect all attributes and methods
print(dir(dog))                     # list of all attributes/methods

# View instance's attribute dictionary
print(dog.__dict__)                 # {'name': 'Rex', 'color': 'black'}
```

---

## 10. Composition (Has-A Relationship)

### What is Composition?

Composition means building complex objects by **combining simpler objects**. One class contains an instance of another class as an attribute. This models a "has-a" relationship.

> A `Car` **has-a** `Engine`. A `House` **has-a** `Room`.

### Creating Classes Within Classes

```python
class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start(self):
        return f"Engine started ({self.horsepower}hp, {self.fuel_type})"


class Wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, brand, engine, wheel_size):
        self.brand = brand
        self.engine = engine                   # composed object
        self.wheels = [Wheel(wheel_size)] * 4  # list of composed objects

    def drive(self):
        engine_status = self.engine.start()
        return f"{self.brand} is driving. {engine_status}"
```

```python
v8 = Engine(450, "petrol")
mustang = Car("Ford Mustang", v8, 18)

print(mustang.drive())
# Ford Mustang is driving. Engine started (450hp, petrol)
print(mustang.engine.fuel_type)  # petrol
```

### Composition vs Inheritance

| Aspect | Composition | Inheritance |
|--------|-------------|-------------|
| Relationship | Has-A | Is-A |
| Flexibility | High — swap components | Lower — tightly coupled |
| Coupling | Loose | Tight |
| Reusability | Good | Good but fragile |
| Preferred when | Complex behavior from parts | True type hierarchy |

---

## 11. Full Example: Mini Class Project — Bank Account

This project brings together instance attributes, class attributes, instance/class/static methods, properties, magic methods, and encapsulation.

```python
class BankAccount:
    """A complete Bank Account class demonstrating all class concepts."""

    bank_name = "PyBank"        # class attribute
    interest_rate = 0.04        # class attribute
    _total_accounts = 0         # class attribute (protected)

    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance   # private
        self._transactions = []
        BankAccount._total_accounts += 1
        self.account_id = BankAccount._total_accounts

    # --- Properties (Encapsulation) ---
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

    # --- Instance Methods ---
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self._transactions.append(f"Deposit: +${amount:.2f}")
        return self

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self._transactions.append(f"Withdrawal: -${amount:.2f}")
        return self

    def get_statement(self):
        lines = [f"Account Statement for {self.owner}",
                 f"Account ID: #{self.account_id}",
                 "-" * 35]
        lines.extend(self._transactions)
        lines.append("-" * 35)
        lines.append(f"Current Balance: ${self.__balance:.2f}")
        return "\n".join(lines)

    # --- Class Method ---
    @classmethod
    def get_total_accounts(cls):
        return f"{cls.bank_name} has {cls._total_accounts} account(s) open."

    @classmethod
    def apply_interest_to(cls, account):
        interest = account.balance * cls.interest_rate
        account.deposit(interest)
        return interest

    # --- Static Method ---
    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    # --- Magic Methods ---
    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance=${self.__balance:.2f})"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.__balance})"

    def __add__(self, other):
        """Merge two accounts (returns combined balance)"""
        return self.__balance + other.balance

    def __eq__(self, other):
        return self.owner == other.owner and self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance
```

```python
# --- Demo ---
acc1 = BankAccount("Amara", 1000)
acc2 = BankAccount("Tunde", 500)

acc1.deposit(500).deposit(200)   # method chaining
acc1.withdraw(100)

interest = BankAccount.apply_interest_to(acc1)
print(f"Interest applied: ${interest:.2f}")

print(acc1.get_statement())
print(BankAccount.get_total_accounts())

print(acc1 > acc2)               # True
print(acc1 + acc2)               # combined balance
print(BankAccount.validate_amount(-50))  # False
```

---

---

# PART II – Object-Oriented Programming Concepts

---

## 1. Introduction to OOP

### What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code around **objects** — bundles of data (attributes) and behavior (methods) — rather than just functions and logic.

### Benefits of OOP

- **Modularity** — Code is organized into self-contained classes
- **Reusability** — Classes and methods can be reused across projects
- **Maintainability** — Easier to find, fix, and extend specific parts
- **Scalability** — New features can be added with minimal changes to existing code
- **Modeling** — Natural way to model real-world entities and relationships

### Core Principles (The Four Pillars)

| Principle | Description | Key Mechanism |
|-----------|-------------|---------------|
| **Encapsulation** | Bundle data + methods; hide internals | Private attrs, properties |
| **Abstraction** | Expose only what's necessary | Abstract classes, interfaces |
| **Inheritance** | Derive new classes from existing ones | `class Child(Parent)` |
| **Polymorphism** | Same interface, different behavior | Method overriding, duck typing |

---

## 2. Inheritance

### Single Inheritance

A child class **inherits** all attributes and methods from a parent class and can extend or override them.

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def breathe(self):
        return f"{self.name} breathes air."

    def speak(self):
        return f"{self.name} makes a sound."

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)    # call parent __init__
        self.breed = breed

    def speak(self):                   # override parent method
        return f"{self.name} says: Woof!"

    def fetch(self):
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"
```

```python
dog = Dog("Rex", 3, "Labrador")
cat = Cat("Whiskers", 5)

print(dog.breathe())   # inherited from Animal
print(dog.speak())     # overridden in Dog
print(dog.fetch())     # unique to Dog
print(cat.speak())     # overridden in Cat
print(str(dog))        # uses Animal.__str__ → Dog(name=Rex, age=3)
```

### Multiple Inheritance

A class can inherit from more than one parent:

```python
class Flyable:
    def fly(self):
        return f"{self.name} is flying!"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return f"{self.name} says: Quack!"

donald = Duck("Donald", 2)
print(donald.fly())    # from Flyable
print(donald.swim())   # from Swimmable
print(donald.speak())  # overridden in Duck
```

### Using `super()`

`super()` calls the **parent class's version** of a method. Essential for extending (not replacing) parent behavior:

```python
class GuideDog(Dog):
    def __init__(self, name, age, breed, owner_name):
        super().__init__(name, age, breed)   # call Dog.__init__
        self.owner_name = owner_name

    def speak(self):
        parent_speak = super().speak()       # call Dog.speak
        return f"{parent_speak} (Guide dog for {self.owner_name})"
```

### Method Resolution Order (MRO)

Python uses the **C3 Linearization** algorithm to determine which parent's method to call in multiple inheritance:

```python
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Animal'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'object'>)
```

---

## 3. Polymorphism

### Method Overriding (Runtime Polymorphism)

Different classes can implement the same method name with different behavior. The correct method is chosen at **runtime** based on the object's actual type.

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def describe(self):
        return f"I am a {self.__class__.__name__} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
```

```python
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print(shape.describe())   # same interface, different area() behavior
```

### Duck Typing

Python's approach to polymorphism: **if it walks like a duck and quacks like a duck, it's a duck**. Python doesn't require formal inheritance — it only cares whether the object has the needed method.

```python
class Robot:
    def speak(self):
        return "Beep boop!"

class Parrot:
    def speak(self):
        return "Polly wants a cracker!"

class Human:
    def speak(self):
        return "Hello, world!"

def make_it_speak(entity):
    """Works with ANY object that has a speak() method"""
    print(entity.speak())

for entity in [Robot(), Parrot(), Human()]:
    make_it_speak(entity)
```

---

## 4. Abstraction

### Abstract Base Classes

The `abc` module lets you define **abstract classes** — classes that cannot be instantiated and that enforce method implementation in all subclasses.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class — cannot be instantiated directly"""

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def fuel_type(self):
        """Must be implemented by all subclasses"""
        pass

    @abstractmethod
    def max_speed(self):
        """Must be implemented by all subclasses"""
        pass

    def describe(self):
        """Concrete method — shared by all subclasses"""
        return (f"{self.year} {self.brand} | "
                f"Fuel: {self.fuel_type()} | "
                f"Max Speed: {self.max_speed()} km/h")


class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"

    def max_speed(self):
        return 250


class Motorcycle(Vehicle):
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return 200
```

```python
# v = Vehicle("X", 2020)  # ❌ TypeError: Can't instantiate abstract class

tesla = ElectricCar("Tesla", 2023)
moto = Motorcycle("Ducati", 2022)

print(tesla.describe())
print(moto.describe())
```

### Benefits of Abstraction

- Enforces a consistent interface across related classes
- Prevents instantiation of incomplete classes
- Documents what subclasses are required to implement
- Enables safe polymorphism

---

## 5. Advanced OOP Concepts

### Class Decorators

You can use Python decorators to modify or augment classes:

```python
def add_greeting(cls):
    """A class decorator that adds a greet method"""
    def greet(self):
        return f"Hello, I am {self.name}!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ada")
print(p.greet())  # Hello, I am Ada!
```

### Design Patterns

**Singleton Pattern** — ensures only one instance of a class exists:

```python
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance

    def connect(self):
        self.connected = True
        return "Connected to database."

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True — same object
```

**Factory Pattern** — creates objects without specifying the exact class:

```python
class Animal:
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "Woof!"

class Cat(Animal):
    def speak(self): return "Meow!"

class AnimalFactory:
    @staticmethod
    def create(animal_type):
        animals = {"dog": Dog, "cat": Cat}
        cls = animals.get(animal_type.lower())
        if cls:
            return cls()
        raise ValueError(f"Unknown animal: {animal_type}")

pet = AnimalFactory.create("dog")
print(pet.speak())  # Woof!
```

### Best Practices for Professional OOP

- **Favor composition over inheritance** when relationships are "has-a"
- **Keep classes small and focused** (Single Responsibility Principle)
- **Program to interfaces**, not implementations
- **Don't repeat yourself (DRY)** — extract common logic into base classes
- **Use `__slots__`** for memory optimization in large numbers of objects
- **Write docstrings** for all classes and methods
- **Avoid deep inheritance chains** — prefer flat hierarchies

---

## 6. Mini Projects Using OOP

### Project 1: Banking System

Combines: Inheritance, Encapsulation, Polymorphism, Class methods

```python
from abc import ABC, abstractmethod
from datetime import datetime

class Account(ABC):
    _total_accounts = 0

    def __init__(self, owner, balance=0):
        Account._total_accounts += 1
        self.account_number = f"ACC{Account._total_accounts:04d}"
        self.owner = owner
        self._balance = balance
        self._history = []

    @property
    def balance(self): return self._balance

    def deposit(self, amount):
        self._balance += amount
        self._log(f"Deposit +${amount:.2f}")

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._log(f"Withdrawal -${amount:.2f}")

    def _log(self, msg):
        self._history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | {msg}")

    @abstractmethod
    def account_type(self): pass

    def __str__(self):
        return f"[{self.account_type()}] {self.owner} | Bal: ${self._balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.04):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def account_type(self): return "Savings"

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        return interest


class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def account_type(self): return "Checking"

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self._balance -= amount
        self._log(f"Withdrawal -${amount:.2f}")
```

---

### Project 2: Student Management System

Combines: Composition, Encapsulation, Class methods

```python
class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.credits} credits)"


class Grade:
    SCALE = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

    def __init__(self, course, letter_grade):
        self.course = course
        self.letter = letter_grade.upper()
        self.points = self.SCALE.get(self.letter, 0.0)


class Student:
    _student_count = 0

    def __init__(self, name, major):
        Student._student_count += 1
        self.student_id = f"STU{Student._student_count:04d}"
        self.name = name
        self.major = major
        self._grades = []

    def add_grade(self, course, letter):
        self._grades.append(Grade(course, letter))

    def calculate_gpa(self):
        if not self._grades:
            return 0.0
        total_points = sum(g.points * g.course.credits for g in self._grades)
        total_credits = sum(g.course.credits for g in self._grades)
        return total_points / total_credits

    def transcript(self):
        lines = [f"Transcript — {self.name} ({self.student_id})",
                 f"Major: {self.major}", "-" * 40]
        for g in self._grades:
            lines.append(f"  {g.course.name:<20} {g.letter}  ({g.points:.1f})")
        lines.append("-" * 40)
        lines.append(f"  GPA: {self.calculate_gpa():.2f}")
        return "\n".join(lines)
```

---

### Project 3: Library System

Combines: Inheritance, Polymorphism, Composition, Abstraction

```python
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_available = True
        self.borrower = None

    @abstractmethod
    def item_type(self): pass

    def checkout(self, member_name):
        if not self.is_available:
            raise ValueError(f"{self.title} is already checked out.")
        self.is_available = False
        self.borrower = member_name

    def return_item(self):
        self.is_available = True
        self.borrower = None

    def __str__(self):
        status = "Available" if self.is_available else f"Checked out by {self.borrower}"
        return f"[{self.item_type()}] {self.title} | {status}"


class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def item_type(self): return "Book"


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration_min):
        super().__init__(title, item_id)
        self.director = director
        self.duration_min = duration_min

    def item_type(self): return "DVD"


class Library:
    def __init__(self, name):
        self.name = name
        self._catalog = {}

    def add_item(self, item):
        self._catalog[item.item_id] = item

    def search(self, title):
        return [item for item in self._catalog.values()
                if title.lower() in item.title.lower()]

    def checkout(self, item_id, member_name):
        item = self._catalog.get(item_id)
        if item:
            item.checkout(member_name)

    def return_item(self, item_id):
        item = self._catalog.get(item_id)
        if item:
            item.return_item()

    def available_items(self):
        return [item for item in self._catalog.values() if item.is_available]
```

---

### Project 4: RPG Game with Class Hierarchies

Combines: All OOP pillars — Inheritance, Polymorphism, Abstraction, Encapsulation, Composition

```python
from abc import ABC, abstractmethod
import random

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name} (dmg: {self.damage})"


class Character(ABC):
    def __init__(self, name, health, attack_power):
        self.name = name
        self._max_health = health
        self._health = health
        self._attack_power = attack_power
        self.level = 1
        self.weapon = None

    @property
    def health(self): return self._health

    @property
    def is_alive(self): return self._health > 0

    def equip(self, weapon):
        self.weapon = weapon

    def attack(self, target):
        damage = self._attack_power
        if self.weapon:
            damage += self.weapon.damage
        damage += random.randint(0, 5)   # randomness
        target.take_damage(damage)
        return damage

    def take_damage(self, amount):
        self._health = max(0, self._health - amount)

    def heal(self, amount):
        self._health = min(self._max_health, self._health + amount)

    @abstractmethod
    def special_ability(self, target): pass

    @abstractmethod
    def character_class(self): pass

    def __str__(self):
        return (f"[{self.character_class()}] {self.name} "
                f"| HP: {self._health}/{self._max_health} "
                f"| ATK: {self._attack_power}"
                f"| Weapon: {self.weapon or 'None'}")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def character_class(self): return "Warrior"

    def special_ability(self, target):
        """Shield Bash — deals double damage"""
        damage = self._attack_power * 2
        target.take_damage(damage)
        return f"{self.name} uses Shield Bash! -{damage} HP"


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=25)
        self._mana = 100

    def character_class(self): return "Mage"

    def special_ability(self, target):
        """Fireball — high damage, costs mana"""
        if self._mana < 30:
            return f"{self.name} is out of mana!"
        damage = 50
        target.take_damage(damage)
        self._mana -= 30
        return f"{self.name} casts Fireball! -{damage} HP (Mana: {self._mana})"


class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)

    def character_class(self): return "Rogue"

    def special_ability(self, target):
        """Backstab — guaranteed critical"""
        damage = self._attack_power * 3
        target.take_damage(damage)
        return f"{self.name} backstabs! CRITICAL! -{damage} HP"
```

---

*End of Course Content*
