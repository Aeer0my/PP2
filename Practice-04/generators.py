# generators.py
# Python Iterators and Generators exercises


# Exercise 1: Generator that yields squares of numbers up to N
def squares_up_to(n):
    """Generate squares of numbers from 1 to N."""
    for i in range(1, n + 1):
        yield i ** 2

print("Exercise 1 — Squares up to N=5:")
for sq in squares_up_to(5):
    print(sq, end=" ")
print()
# Output: 1 4 9 16 25


# Exercise 2: Generator for even numbers between 0 and n (comma separated)
def even_numbers(n):
    """Generate even numbers from 0 to n."""
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input("\nExercise 2 — Enter n for even numbers: "))
result = ",".join(str(x) for x in even_numbers(n))
print(result)
# Example input: 10 → Output: 0,2,4,6,8,10


# Exercise 3: Generator for numbers divisible by both 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    """Generate numbers divisible by both 3 and 4 in range [0, n]."""
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("\nExercise 3 — Divisible by 3 and 4 up to 50:")
for num in divisible_by_3_and_4(50):
    print(num, end=" ")
print()
# Output: 0 12 24 36 48


# Exercise 4: Generator 'squares' that yields squares from a to b
def squares(a, b):
    """Yield the square of all numbers from a to b (inclusive)."""
    for i in range(a, b + 1):
        yield i ** 2

print("\nExercise 4 — Squares from 3 to 7:")
for val in squares(3, 7):
    print(val)
# Output: 9 16 25 36 49


# Exercise 5: Generator that counts down from n to 0
def countdown(n):
    """Generate numbers from n down to 0."""
    while n >= 0:
        yield n
        n -= 1

print("\nExercise 5 — Countdown from 5:")
for num in countdown(5):
    print(num, end=" ")
print()
# Output: 5 4 3 2 1 0
