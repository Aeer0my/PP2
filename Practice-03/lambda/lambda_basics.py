# lambda_basics.py
# Demonstrates basic lambda (anonymous) function syntax and usage


# 1. Simple lambda vs regular function — same result
def double_regular(x):
    return x * 2

double_lambda = lambda x: x * 2  # equivalent one-liner

print(double_regular(5))   # Output: 10
print(double_lambda(5))    # Output: 10


# 2. Lambda with two arguments
multiply = lambda a, b: a * b
print(multiply(3, 7))     # Output: 21


# 3. Lambda with a conditional expression (ternary)
classify = lambda n: "even" if n % 2 == 0 else "odd"
print(classify(4))    # Output: even
print(classify(7))    # Output: odd


# 4. Immediately Invoked Lambda — call it right where it's defined
result = (lambda x, y: x ** y)(2, 10)
print(f"2 to the power of 10 = {result}")  # Output: 1024
