# builtin_functions/map_filter_reduce.py
# Demonstrates map(), filter(), reduce(), and common aggregates

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

# --- len(), sum(), min(), max() ---
print("=== Aggregates ===")
print(f"len(numbers)  = {len(numbers)}")
print(f"sum(numbers)  = {sum(numbers)}")
print(f"min(numbers)  = {min(numbers)}")
print(f"max(numbers)  = {max(numbers)}")
print(f"min(words)    = {min(words)}")   # alphabetical
print(f"max(words, key=len) = {max(words, key=len)}")  # longest word

# --- map() ---
print("\n=== map() ===")
# map(function, iterable) — applies function to every element
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squares: {squared}")

upper_words = list(map(str.upper, words))
print(f"Uppercased: {upper_words}")

# map with regular function
def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 1)

temps_c = [0, 20, 37, 100]
temps_f = list(map(celsius_to_fahrenheit, temps_c))
print(f"Celsius {temps_c} -> Fahrenheit {temps_f}")

# --- filter() ---
print("\n=== filter() ===")
# filter(function, iterable) — keeps elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

long_words = list(filter(lambda w: len(w) > 5, words))
print(f"Words longer than 5 chars: {long_words}")

# --- reduce() ---
print("\n=== reduce() ===")
# reduce(function, iterable) — applies function cumulatively
product = reduce(lambda a, b: a * b, numbers)
print(f"Product of all numbers: {product}")

total = reduce(lambda a, b: a + b, numbers)
print(f"Sum via reduce: {total}")

longest = reduce(lambda a, b: a if len(a) >= len(b) else b, words)
print(f"Longest word via reduce: '{longest}'")

# --- sorted() ---
print("\n=== sorted() ===")
unsorted = [5, 1, 9, 3, 7, 2]
print(f"sorted() ascending:  {sorted(unsorted)}")
print(f"sorted() descending: {sorted(unsorted, reverse=True)}")
print(f"words by length:     {sorted(words, key=len)}")

# --- Type conversions ---
print("\n=== Type conversions ===")
print(f"int('42')     = {int('42')}")
print(f"float('3.14') = {float('3.14')}")
print(f"str(100)      = {str(100)!r}")
print(f"bool(0)       = {bool(0)}")
print(f"bool('hi')    = {bool('hi')}")
print(f"list((1,2,3)) = {list((1, 2, 3))}")
print(f"tuple([1,2])  = {tuple([1, 2])}")
print(f"set([1,1,2])  = {set([1, 1, 2])}")

# --- Type checking ---
print("\n=== type() and isinstance() ===")
values = [42, 3.14, "hello", True, [1, 2], {"a": 1}]
for v in values:
    print(f"  {str(v):<15} type={type(v).__name__:<8} "
          f"isinstance(int)={isinstance(v, int)}")
