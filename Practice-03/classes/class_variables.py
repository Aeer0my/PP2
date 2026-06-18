# class_variables.py
# Demonstrates the difference between class variables and instance variables


# 1. Class variable vs instance variable
class Employee:
    """Represents an employee at a company."""

    company = "TechCorp"    # class variable — same for every Employee
    employee_count = 0      # class variable — tracks total number of employees

    def __init__(self, name, salary):
        self.name = name          # instance variable — unique per object
        self.salary = salary      # instance variable — unique per object
        Employee.employee_count += 1  # update class variable on each creation

    def describe(self):
        print(f"{self.name} at {self.company} | Salary: ${self.salary:,}")


emp1 = Employee("Alice", 90000)
emp2 = Employee("Bob", 75000)
emp3 = Employee("Charlie", 85000)

emp1.describe()
emp2.describe()
print(f"Total employees: {Employee.employee_count}")  # 3


# 2. Class variable shared until overridden on an instance
class Config:
    """Shared app configuration."""
    debug = False
    version = "1.0"


cfg_a = Config()
cfg_b = Config()

# Both share the same class variable
print(cfg_a.debug, cfg_b.debug)    # False False

# Overriding on an instance creates an instance variable (shadow)
cfg_a.debug = True
print(cfg_a.debug)   # True  — now an instance variable
print(cfg_b.debug)   # False — still reads the class variable
print(Config.debug)  # False — class variable unchanged


# 3. Mutable class variable — be careful, shared state can cause bugs
class Team:
    members = []   # shared list — all Team instances share this!

    def add_member(self, name):
        self.members.append(name)


team_a = Team()
team_b = Team()
team_a.add_member("Alice")
team_b.add_member("Bob")

# Both teams see both members — this is a classic Python pitfall!
print("Team A members:", team_a.members)  # ['Alice', 'Bob']
print("Team B members:", team_b.members)  # ['Alice', 'Bob']


# FIX: use instance variable in __init__ instead
class TeamFixed:
    def __init__(self):
        self.members = []   # each instance gets its own list

    def add_member(self, name):
        self.members.append(name)


ta = TeamFixed()
tb = TeamFixed()
ta.add_member("Alice")
tb.add_member("Bob")

print("Fixed Team A:", ta.members)   # ['Alice']
print("Fixed Team B:", tb.members)   # ['Bob']
