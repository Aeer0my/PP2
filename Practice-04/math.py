# math.py
# Python Math library exercises

import math


# Exercise 1: Convert degrees to radians
# Formula: radians = degrees * (pi / 180)
degree = float(input("Exercise 1 — Input degree: "))
radian = degree * (math.pi / 180)
print(f"Output radian: {radian:.6f}")
# Example: 15 degrees → 0.261799


# Exercise 2: Calculate the area of a trapezoid
# Formula: area = ((base1 + base2) / 2) * height
print("\nExercise 2 — Area of a trapezoid:")
height = float(input("  Height: "))
base1  = float(input("  Base, first value: "))
base2  = float(input("  Base, second value: "))
area_trapezoid = ((base1 + base2) / 2) * height
print(f"  Area of trapezoid: {area_trapezoid}")
# Example: height=5, base1=5, base2=6 → 27.5


# Exercise 3: Calculate the area of a regular polygon
# Formula: area = (n * s^2) / (4 * tan(pi / n))
print("\nExercise 3 — Area of a regular polygon:")
n = int(input("  Input number of sides: "))
s = float(input("  Input the length of a side: "))
area_polygon = (n * s ** 2) / (4 * math.tan(math.pi / n))
print(f"  The area of the polygon is: {area_polygon:.0f}")
# Example: n=4, s=25 → 625


# Exercise 4: Calculate the area of a parallelogram
# Formula: area = base * height
print("\nExercise 4 — Area of a parallelogram:")
base   = float(input("  Length of base: "))
height = float(input("  Height of parallelogram: "))
area_parallelogram = base * height
print(f"  Expected Output: {area_parallelogram}")
# Example: base=5, height=6 → 30.0
