# lambda_with_filter.py
# Demonstrates using lambda with filter() to select elements


# filter(function, iterable) keeps only elements where function returns True


# 1. Filter out only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("All numbers:", numbers)
print("Even only: ", evens)
# Output: [2, 4, 6, 8, 10]


# 2. Filter words longer than 4 characters
words = ["cat", "elephant", "dog", "tiger", "ox", "hippopotamus"]
long_words = list(filter(lambda w: len(w) > 4, words))
print("\nAll words: ", words)
print("Long words:", long_words)
# Output: ['elephant', 'tiger', 'hippopotamus']


# 3. Filter out negative numbers (keep only positives)
values = [-10, 5, -3, 8, 0, -1, 7, 2]
positives = list(filter(lambda x: x > 0, values))
print("\nAll values:", values)
print("Positives: ", positives)
# Output: [5, 8, 7, 2]


# 4. Filter students who passed (grade >= 60)
grades = [45, 72, 58, 90, 61, 33, 88, 55]
passing = list(filter(lambda g: g >= 60, grades))
print("\nAll grades:    ", grades)
print("Passing grades:", passing)
# Output: [72, 90, 61, 88]
