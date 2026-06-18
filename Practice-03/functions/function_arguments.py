# function_arguments.py
# Demonstrates different types of function arguments in Python


# 1. Positional arguments — order matters
def describe_pet(animal_type, pet_name):
    """Display info about a pet using positional arguments."""
    print(f"I have a {animal_type} named {pet_name}.")


describe_pet("dog", "Rex")   # positional: dog -> animal_type, Rex -> pet_name
describe_pet("cat", "Whiskers")


# 2. Default argument values
def make_coffee(size="medium", sugar=1, milk=True):
    """Order a coffee with optional customizations."""
    milk_status = "with milk" if milk else "without milk"
    print(f"Coffee: {size}, {sugar} sugar(s), {milk_status}")


make_coffee()                          # uses all defaults
make_coffee("large", 2)               # overrides size and sugar
make_coffee("small", 0, False)        # overrides everything


# 3. Keyword arguments — order doesn't matter
def register_user(username, email, age):
    """Register a user with keyword arguments."""
    print(f"Registered: {username}, Email: {email}, Age: {age}")


# Using keyword arguments allows any order
register_user(email="bob@example.com", age=25, username="bob99")


# 4. Mixing positional and keyword arguments
def create_profile(name, city, job="Unknown"):
    """Create a user profile mixing positional and keyword args."""
    print(f"Name: {name} | City: {city} | Job: {job}")


create_profile("Anna", "Almaty")                  # job uses default
create_profile("Mark", "Berlin", job="Engineer")  # job overridden
