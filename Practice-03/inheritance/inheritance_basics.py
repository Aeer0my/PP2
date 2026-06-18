# inheritance_basics.py
# Demonstrates basic parent-child class relationships


# 1. Parent (base) class
class Animal:
    """Base class representing any animal."""

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        """Make the animal produce its sound."""
        print(f"{self.name} says: {self.sound}!")

    def eat(self):
        """Animals eat food."""
        print(f"{self.name} is eating.")


# 2. Child class inherits from Animal
class Dog(Animal):
    """Dog inherits all Animal behavior and adds its own."""

    def __init__(self, name, breed):
        # Call parent __init__ to set name and sound
        super().__init__(name, sound="Woof")
        self.breed = breed   # Dog-specific attribute

    def fetch(self):
        """Dogs can fetch objects."""
        print(f"{self.name} fetches the ball!")


class Cat(Animal):
    """Cat inherits from Animal with its own sound."""

    def __init__(self, name, indoor):
        super().__init__(name, sound="Meow")
        self.indoor = indoor

    def purr(self):
        """Cats can purr."""
        location = "indoor" if self.indoor else "outdoor"
        print(f"{self.name} purrs contentedly ({location} cat).")


# 3. Using inherited and new methods
dog = Dog("Rex", "Labrador")
cat = Cat("Luna", indoor=True)

dog.speak()    # inherited from Animal — Rex says: Woof!
dog.eat()      # inherited from Animal — Rex is eating.
dog.fetch()    # Dog-specific — Rex fetches the ball!

cat.speak()    # inherited from Animal — Luna says: Meow!
cat.purr()     # Cat-specific


# 4. isinstance() and issubclass() checks
print(isinstance(dog, Dog))       # True
print(isinstance(dog, Animal))    # True — Dog IS an Animal
print(isinstance(cat, Dog))       # False

print(issubclass(Dog, Animal))    # True
print(issubclass(Cat, Animal))    # True
print(issubclass(Dog, Cat))       # False
