# class_definition.py
# Demonstrates basic class definition and object creation in Python


# 1. Simplest possible class
class Dog:
    """Represents a dog."""
    species = "Canis lupus familiaris"  # class variable shared by all instances

    def __init__(self, name, breed):
        # Instance variables — unique to each object
        self.name = name
        self.breed = breed

    def bark(self):
        """Make the dog bark."""
        print(f"{self.name} says: Woof!")

    def describe(self):
        """Print a description of the dog."""
        print(f"{self.name} is a {self.breed} ({self.species})")


# Creating objects (instances) of the Dog class
dog1 = Dog("Rex", "German Shepherd")
dog2 = Dog("Buddy", "Golden Retriever")

dog1.bark()       # Output: Rex says: Woof!
dog2.bark()       # Output: Buddy says: Woof!
dog1.describe()   # Output: Rex is a German Shepherd (Canis lupus familiaris)


# 2. Accessing class variable through instance and class
print(dog1.species)   # via instance
print(Dog.species)    # via class name — same value


# 3. Modifying object properties
dog1.name = "Max"     # update existing attribute
dog1.age = 3          # add a new attribute dynamically
print(f"\nUpdated name: {dog1.name}, Age: {dog1.age}")


# 4. Deleting an object property
del dog1.age
# print(dog1.age)  # would raise AttributeError now
print("Age attribute deleted from dog1.")
