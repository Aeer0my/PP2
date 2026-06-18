# basic_functions.py
# Demonstrates basic function definition and calling in Python


# 1. Simple function with no arguments
def greet():
    """Print a simple greeting message."""
    print("Hello, World!")


greet()  # Output: Hello, World!


# 2. Function with a parameter
def greet_user(name):
    """Greet a specific user by name."""
    print(f"Hello, {name}!")


greet_user("Alice")  # Output: Hello, Alice!


# 3. Function that performs a calculation
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    area = width * height
    return area


result = calculate_area(5, 3)
print(f"Area of rectangle: {result}")  # Output: Area of rectangle: 15


# 4. Function with a list as argument
def print_items(items):
    """Print each item from a list on a new line."""
    for item in items:
        print(f"  - {item}")


fruits = ["apple", "banana", "cherry"]
print("Fruits:")
print_items(fruits)
