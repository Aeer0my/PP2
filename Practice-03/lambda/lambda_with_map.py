# lambda_with_map.py
# Demonstrates using lambda with map() to transform sequences


# map(function, iterable) applies a function to every element
# and returns a map object (convert to list to view results)


# 1. Convert all temperatures from Celsius to Fahrenheit
celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print("Celsius:   ", celsius_temps)
print("Fahrenheit:", fahrenheit_temps)
# Output: [32.0, 68.0, 98.6, 212.0]


# 2. Square every number in a list
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("\nNumbers:", numbers)
print("Squares:", squares)
# Output: [1, 4, 9, 16, 25]


# 3. Capitalize every word in a list
words = ["hello", "world", "python", "lambda"]
capitalized = list(map(lambda w: w.capitalize(), words))
print("\nOriginal:", words)
print("Capitalized:", capitalized)
# Output: ['Hello', 'World', 'Python', 'Lambda']


# 4. map() with two lists simultaneously — add corresponding elements
list_a = [1, 2, 3, 4]
list_b = [10, 20, 30, 40]
sums = list(map(lambda a, b: a + b, list_a, list_b))
print("\nList A:", list_a)
print("List B:", list_b)
print("Element-wise sums:", sums)
# Output: [11, 22, 33, 44]
