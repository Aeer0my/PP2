# method_overriding.py
# Demonstrates overriding parent methods in child classes


# 1. Basic method overriding
class Shape:
    """Base class for geometric shapes."""

    def area(self):
        """Default area — subclasses should override this."""
        return 0

    def describe(self):
        print(f"Shape with area = {self.area():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):   # OVERRIDES Shape.area()
        import math
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):   # OVERRIDES Shape.area()
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):   # OVERRIDES Shape.area()
        return 0.5 * self.base * self.height


# All shapes use the same describe() method, but each area() is unique
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for shape in shapes:
    shape.describe()
# Output:
# Shape with area = 78.54
# Shape with area = 24.00
# Shape with area = 12.00


# 2. Overriding __str__ for readable object representation
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):   # OVERRIDES the default object string
        return f"Product('{self.name}', ${self.price:.2f})"


class DiscountedProduct(Product):
    def __init__(self, name, price, discount_pct):
        super().__init__(name, price)
        self.discount_pct = discount_pct

    def __str__(self):   # OVERRIDES Product.__str__
        discounted = self.price * (1 - self.discount_pct / 100)
        return (f"Product('{self.name}', ${self.price:.2f} "
                f"-> ${discounted:.2f} [{self.discount_pct}% off])")


p = Product("Laptop", 1200)
dp = DiscountedProduct("Laptop", 1200, 15)

print(p)    # Output: Product('Laptop', $1200.00)
print(dp)   # Output: Product('Laptop', $1200.00 -> $1020.00 [15% off])
