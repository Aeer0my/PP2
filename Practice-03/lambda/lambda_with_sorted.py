# lambda_with_sorted.py
# Demonstrates using lambda with sorted() for custom sorting


# sorted(iterable, key=function, reverse=False)
# The key function extracts the value used for comparison


# 1. Sort strings by their length
words = ["banana", "fig", "apple", "kiwi", "strawberry", "pear"]
sorted_by_length = sorted(words, key=lambda w: len(w))
print("By length (asc): ", sorted_by_length)
# Output: ['fig', 'kiwi', 'pear', 'apple', 'banana', 'strawberry']


# 2. Sort a list of tuples by the second element (score)
students = [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("Diana", 80)]
sorted_by_score = sorted(students, key=lambda s: s[1], reverse=True)
print("\nStudents by score (desc):")
for name, score in sorted_by_score:
    print(f"  {name}: {score}")
# Output: Charlie 95, Alice 88, Diana 80, Bob 72


# 3. Sort dictionaries by a specific field
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse",  "price": 25},
    {"name": "Monitor","price": 350},
    {"name": "Keyboard","price": 75},
]
sorted_by_price = sorted(products, key=lambda p: p["price"])
print("\nProducts by price (asc):")
for product in sorted_by_price:
    print(f"  {product['name']}: ${product['price']}")


# 4. Sort by multiple criteria — primary: grade desc, secondary: name asc
records = [("Bob", "B"), ("Alice", "A"), ("Charlie", "B"), ("Diana", "A")]
grade_order = {"A": 1, "B": 2, "C": 3}   # lower number = better grade
sorted_records = sorted(records, key=lambda r: (grade_order[r[1]], r[0]))
print("\nSorted by grade then name:")
for name, grade in sorted_records:
    print(f"  {name}: {grade}")
