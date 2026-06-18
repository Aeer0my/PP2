# super_function.py
# Demonstrates how super() works to call parent class methods


# 1. super() in __init__ to extend parent initialization
class Vehicle:
    """Base class for all vehicles."""

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        print(f"Vehicle created: {brand}")

    def describe(self):
        print(f"{self.brand} — max speed: {self.speed} km/h")


class ElectricCar(Vehicle):
    """Extends Vehicle with an electric battery."""

    def __init__(self, brand, speed, battery_kwh):
        super().__init__(brand, speed)      # run parent __init__ first
        self.battery_kwh = battery_kwh      # then add child-specific attribute
        print(f"Battery: {battery_kwh} kWh")

    def describe(self):
        super().describe()                  # call parent's describe()
        print(f"  Battery: {self.battery_kwh} kWh (electric)")


tesla = ElectricCar("Tesla", 250, 100)
tesla.describe()


# 2. super() in a multi-level inheritance chain
class Shape:
    def __init__(self, color):
        self.color = color

    def info(self):
        print(f"Color: {self.color}")


class Polygon(Shape):
    def __init__(self, color, sides):
        super().__init__(color)
        self.sides = sides

    def info(self):
        super().info()
        print(f"Sides: {self.sides}")


class RegularPolygon(Polygon):
    def __init__(self, color, sides, side_length):
        super().__init__(color, sides)
        self.side_length = side_length

    def info(self):
        super().info()    # calls Polygon.info which calls Shape.info
        print(f"Side length: {self.side_length} cm")
        print(f"Perimeter: {self.sides * self.side_length} cm")


hexagon = RegularPolygon("blue", 6, 5)
print("\nHexagon info:")
hexagon.info()


# 3. super() to extend a method without replacing it completely
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")


class TimestampLogger(Logger):
    def log(self, message):
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        super().log(f"[{timestamp}] {message}")   # reuse parent logic


tl = TimestampLogger()
tl.log("Server started")   # Output: [LOG] [HH:MM:SS] Server started
