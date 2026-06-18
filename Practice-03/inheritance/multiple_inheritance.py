# multiple_inheritance.py
# Demonstrates inheriting from more than one parent class


# 1. Basic multiple inheritance
class Flyable:
    """Mixin that adds flying ability."""

    def fly(self):
        print(f"{self.name} is flying!")


class Swimmable:
    """Mixin that adds swimming ability."""

    def swim(self):
        print(f"{self.name} is swimming!")


class Walkable:
    """Mixin that adds walking ability."""

    def walk(self):
        print(f"{self.name} is walking!")


# Duck inherits from all three mixins
class Duck(Flyable, Swimmable, Walkable):
    def __init__(self, name):
        self.name = name

    def quack(self):
        print(f"{self.name} says: Quack!")


donald = Duck("Donald")
donald.fly()     # from Flyable
donald.swim()    # from Swimmable
donald.walk()    # from Walkable
donald.quack()   # Duck's own method


# 2. Method Resolution Order (MRO) — Python resolves conflicts left to right
class A:
    def greet(self):
        print("Hello from A")


class B(A):
    def greet(self):
        print("Hello from B")


class C(A):
    def greet(self):
        print("Hello from C")


class D(B, C):   # inherits from B first, then C
    pass


d = D()
d.greet()           # Output: Hello from B  (B comes before C in MRO)
print(D.__mro__)    # shows the full resolution order


# 3. Combining a base class with a utility mixin
class JSONMixin:
    """Mixin to add JSON serialization to any class."""

    def to_json(self):
        import json
        # Serialize all instance attributes
        return json.dumps(self.__dict__, indent=2)


class User(JSONMixin):
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age


user = User("alice99", "alice@example.com", 28)
print("\nUser as JSON:")
print(user.to_json())


# 4. Diamond inheritance — super() ensures each class is called once
class Base:
    def process(self):
        print("Base.process()")


class Left(Base):
    def process(self):
        print("Left.process()")
        super().process()


class Right(Base):
    def process(self):
        print("Right.process()")
        super().process()


class Child(Left, Right):
    def process(self):
        print("Child.process()")
        super().process()


print("\nDiamond MRO call chain:")
Child().process()
# Output: Child -> Left -> Right -> Base (each called exactly once)
