# return_values.py
# Demonstrates how functions return values in Python


# 1. Returning a single value
def square(number):
    """Return the square of a number."""
    return number ** 2


print(square(4))   # Output: 16
print(square(9))   # Output: 81


# 2. Returning multiple values (as a tuple)
def min_max(numbers):
    """Return both the minimum and maximum from a list."""
    return min(numbers), max(numbers)


low, high = min_max([3, 1, 7, 2, 9, 4])
print(f"Min: {low}, Max: {high}")  # Output: Min: 1, Max: 9


# 3. Early return — exit function based on condition
def safe_divide(a, b):
    """Divide a by b, return None if b is zero."""
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None   # early exit
    return a / b


print(safe_divide(10, 2))   # Output: 5.0
print(safe_divide(5, 0))    # Output: Error message, then None


# 4. Returning a dictionary with structured data
def get_student_info(name, grade, passed):
    """Return student data as a dictionary."""
    return {
        "name": name,
        "grade": grade,
        "status": "Passed" if passed else "Failed"
    }


student = get_student_info("Dana", 85, True)
print(student)  # Output: {'name': 'Dana', 'grade': 85, 'status': 'Passed'}
