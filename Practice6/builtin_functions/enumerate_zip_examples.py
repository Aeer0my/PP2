# builtin_functions/enumerate_zip_examples.py
# Demonstrates enumerate(), zip(), and related built-ins

# --- enumerate() ---
print("=== enumerate() ===")
# enumerate(iterable, start=0) — yields (index, value) pairs
fruits = ["apple", "banana", "cherry", "date"]

for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

print("\nStarting from index 1:")
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}. {fruit}")

# Practical: find index of item matching condition
scores = [45, 82, 91, 60, 75]
above_80 = [(i, s) for i, s in enumerate(scores) if s > 80]
print(f"\nScores above 80 (index, value): {above_80}")

# --- zip() ---
print("\n=== zip() ===")
# zip(iter1, iter2, ...) — pairs elements from multiple iterables
names = ["Alice", "Bob", "Charlie"]
ages  = [25, 30, 22]
cities = ["Almaty", "Astana", "Shymkent"]

for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}, {city}")

# zip stops at the shortest iterable
long_list  = [1, 2, 3, 4, 5]
short_list = ["a", "b", "c"]
print(f"\nzip stops early: {list(zip(long_list, short_list))}")

# Unzip with * operator
pairs = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print(f"Unzipped: nums={nums}, letters={letters}")

# --- enumerate + zip together ---
print("\n=== enumerate + zip ===")
products = ["Milk", "Bread", "Eggs"]
prices   = [350, 180, 520]

for i, (product, price) in enumerate(zip(products, prices), start=1):
    print(f"  {i}. {product:<10} {price:>6} тг")

total = sum(prices)
print(f"  {'TOTAL':<10} {total:>6} тг")

# --- zip to build a dict ---
print("\n=== zip to build a dict ===")
keys   = ["name", "age", "city"]
values = ["Diana", 28, "Almaty"]
person = dict(zip(keys, values))
print(f"  {person}")

# --- any() and all() ---
print("\n=== any() and all() ===")
nums = [2, 4, 6, 8, 10]
print(f"all even? {all(n % 2 == 0 for n in nums)}")   # True
print(f"any > 9?  {any(n > 9 for n in nums)}")         # True
print(f"all > 5?  {all(n > 5 for n in nums)}")         # False

# --- range(), abs(), round(), pow() ---
print("\n=== Other useful built-ins ===")
print(f"range(1, 6):     {list(range(1, 6))}")
print(f"abs(-42):        {abs(-42)}")
print(f"round(3.14159, 2): {round(3.14159, 2)}")
print(f"pow(2, 10):      {pow(2, 10)}")
print(f"divmod(17, 5):   {divmod(17, 5)}")   # (quotient, remainder)
