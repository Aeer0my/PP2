# args_kwargs.py
# Demonstrates *args and **kwargs for flexible function signatures


# 1. *args — accepts any number of positional arguments
def calculate_sum(*args):
    """Sum any number of provided numbers."""
    total = sum(args)
    print(f"Sum of {args} = {total}")
    return total


calculate_sum(1, 2, 3)           # Output: Sum of (1, 2, 3) = 6
calculate_sum(10, 20, 30, 40)    # Output: Sum of (10, 20, 30, 40) = 100


# 2. **kwargs — accepts any number of keyword arguments
def display_info(**kwargs):
    """Display any key-value pairs passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print("User Info:")
display_info(name="Alice", age=28, city="Almaty", job="Developer")


# 3. Combining regular args, *args, and **kwargs
def full_order(item, *toppings, **options):
    """
    Build a food order with a required item, optional toppings,
    and optional extra settings.
    """
    print(f"\nOrder: {item}")
    if toppings:
        print(f"  Toppings: {', '.join(toppings)}")
    if options:
        for key, value in options.items():
            print(f"  {key}: {value}")


full_order("Pizza", "cheese", "olives", size="large", delivery=True)
full_order("Burger")  # no toppings or extras


# 4. Unpacking a list/dict into a function using * and **
def greet(first, last, greeting="Hello"):
    """Greet a person using their full name."""
    print(f"{greeting}, {first} {last}!")


person_data = {"first": "John", "last": "Doe"}
greet(**person_data)                      # unpack dict as keyword args

name_parts = ["Jane", "Smith"]
greet(*name_parts, greeting="Hi")        # unpack list as positional args
