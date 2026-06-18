# init_method.py
# Demonstrates the __init__() constructor and instance initialization


# 1. Basic __init__ with required parameters
class Person:
    """Represents a person with a name and age."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
p1.introduce()   # Output: Hi, I'm Alice and I'm 30 years old.
p2.introduce()   # Output: Hi, I'm Bob and I'm 25 years old.


# 2. __init__ with default parameter values
class Car:
    """Represents a car with optional color."""

    def __init__(self, brand, model, color="White"):
        self.brand = brand
        self.model = model
        self.color = color

    def describe(self):
        print(f"{self.color} {self.brand} {self.model}")


car1 = Car("Toyota", "Camry")           # uses default color
car2 = Car("BMW", "X5", "Black")        # overrides default
car1.describe()   # Output: White Toyota Camry
car2.describe()   # Output: Black BMW X5


# 3. __init__ with computed attributes
class Rectangle:
    """Represents a rectangle and auto-computes area and perimeter."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height              # computed at creation
        self.perimeter = 2 * (width + height)  # computed at creation

    def describe(self):
        print(f"Rectangle {self.width}x{self.height}: "
              f"Area={self.area}, Perimeter={self.perimeter}")


rect = Rectangle(5, 3)
rect.describe()   # Output: Rectangle 5x3: Area=15, Perimeter=16


# 4. __init__ with a list attribute (mutable default handled correctly)
class ShoppingCart:
    """Represents a shopping cart that starts empty."""

    def __init__(self, owner):
        self.owner = owner
        self.items = []   # each cart gets its own independent list

    def add_item(self, item):
        self.items.append(item)

    def show_cart(self):
        print(f"{self.owner}'s cart: {self.items}")


cart1 = ShoppingCart("Alice")
cart2 = ShoppingCart("Bob")
cart1.add_item("Apple")
cart1.add_item("Bread")
cart2.add_item("Milk")

cart1.show_cart()   # Output: Alice's cart: ['Apple', 'Bread']
cart2.show_cart()   # Output: Bob's cart: ['Milk']
