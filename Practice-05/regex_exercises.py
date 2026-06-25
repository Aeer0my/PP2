# regex_exercises.py
# Python Regular Expressions — 10 exercises
import re


# Exercise 1: Match a string that has 'a' followed by zero or more 'b's
# Pattern: ab* means 'a' then 0 or more 'b'
pattern1 = r"ab*"
tests1 = ["a", "ab", "abbb", "ac", "b"]
print("Exercise 1 — 'a' followed by zero or more 'b':")
for s in tests1:
    match = re.match(pattern1, s)
    print(f"  '{s}' -> {'Match: ' + match.group() if match else 'No match'}")


# Exercise 2: Match a string that has 'a' followed by 2 to 3 'b's
# Pattern: ab{2,3} means 'a' then exactly 2 or 3 'b'
pattern2 = r"ab{2,3}"
tests2 = ["ab", "abb", "abbb", "abbbb"]
print("\nExercise 2 — 'a' followed by 2 to 3 'b':")
for s in tests2:
    match = re.match(pattern2, s)
    print(f"  '{s}' -> {'Match: ' + match.group() if match else 'No match'}")


# Exercise 3: Find sequences of lowercase letters joined with an underscore
# Pattern: [a-z]+ matches one or more lowercase letters, _ joins them
pattern3 = r"[a-z]+_[a-z]+"
tests3 = ["hello_world", "foo_bar_baz", "Hello_World", "snake_case_string"]
print("\nExercise 3 — Lowercase letters joined with underscore:")
for s in tests3:
    matches = re.findall(pattern3, s)
    print(f"  '{s}' -> {matches}")


# Exercise 4: Find sequences of one uppercase letter followed by lowercase letters
# Pattern: [A-Z][a-z]+ means capital + one or more lowercase
pattern4 = r"[A-Z][a-z]+"
tests4 = ["Hello World", "CamelCase", "Python RegEx", "ABC"]
print("\nExercise 4 — One uppercase followed by lowercase letters:")
for s in tests4:
    matches = re.findall(pattern4, s)
    print(f"  '{s}' -> {matches}")


# Exercise 5: Match a string that has 'a' followed by anything, ending in 'b'
# Pattern: a.*b means 'a', then any chars (.* = greedy), then 'b'
pattern5 = r"a.*b"
tests5 = ["aXYZb", "ab", "ab123b", "hello", "a_anything_here_b"]
print("\nExercise 5 — 'a' followed by anything ending in 'b':")
for s in tests5:
    match = re.search(pattern5, s)
    print(f"  '{s}' -> {'Match: ' + match.group() if match else 'No match'}")


# Exercise 6: Replace all spaces, commas, or dots with a colon
# Pattern: [ ,.] is a character class matching space, comma, or dot
pattern6 = r"[ ,.]"
tests6 = ["one two,three.four", "hello world", "a,b.c d"]
print("\nExercise 6 — Replace space, comma, dot with colon:")
for s in tests6:
    result = re.sub(pattern6, ":", s)
    print(f"  '{s}' -> '{result}'")


# Exercise 7: Convert snake_case string to camelCase
# Strategy: find _x patterns and capitalize the letter after underscore
def snake_to_camel(snake_str):
    # Replace _x with uppercase X, then capitalize first letter
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), snake_str)

tests7 = ["hello_world", "my_variable_name", "convert_this_string"]
print("\nExercise 7 — snake_case to camelCase:")
for s in tests7:
    print(f"  '{s}' -> '{snake_to_camel(s)}'")


# Exercise 8: Split a string at uppercase letters
# Pattern: (?=[A-Z]) is a lookahead — splits before each uppercase letter
pattern8 = r"(?=[A-Z])"
tests8 = ["CamelCaseString", "HelloWorld", "PythonRegEx"]
print("\nExercise 8 — Split at uppercase letters:")
for s in tests8:
    parts = re.split(pattern8, s)
    parts = [p for p in parts if p]   # remove empty strings
    print(f"  '{s}' -> {parts}")


# Exercise 9: Insert spaces between words starting with capital letters
# Pattern: (?<=[a-z])(?=[A-Z]) — between lowercase and uppercase
pattern9 = r"(?<=[a-z])(?=[A-Z])"
tests9 = ["CamelCaseString", "HelloWorld", "InsertSpacesHere"]
print("\nExercise 9 — Insert spaces before capitals:")
for s in tests9:
    result = re.sub(pattern9, " ", s)
    print(f"  '{s}' -> '{result}'")


# Exercise 10: Convert camelCase to snake_case
# Strategy: find uppercase letters and replace with _lowercase
def camel_to_snake(camel_str):
    # Insert _ before each uppercase letter, then lowercase everything
    result = re.sub(r"([A-Z])", r"_\1", camel_str)
    return result.lstrip("_").lower()

tests10 = ["camelCaseString", "myVariableName", "convertThisString"]
print("\nExercise 10 — camelCase to snake_case:")
for s in tests10:
    print(f"  '{s}' -> '{camel_to_snake(s)}'")
