# json.py
# Python JSON parsing exercises

import json


# Exercise 1: Parse sample-data.json and display Interface Status table
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20}  {'Speed':<6}  {'MTU':<6}")
print(f"{'-' * 50} {'-' * 20}  {'-' * 6}  {'-' * 6}")

# Read and parse the JSON file
with open("sample-data.json", "r") as f:
    data = json.load(f)

# Iterate over each interface entry
for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn    = attrs["dn"]
    descr = attrs["descr"]         # empty string if no description
    speed = attrs["speed"]
    mtu   = attrs["mtu"]
    print(f"{dn:<50} {descr:<20}  {speed:<6}  {mtu:<6}")


# Exercise 2: json.loads() — parse a JSON string into a Python dict
print("\n--- Exercise 2: json.loads() ---")
json_string = '{"name": "Alice", "age": 30, "city": "Almaty"}'
person = json.loads(json_string)   # string → Python dict
print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")


# Exercise 3: json.dumps() — convert a Python dict to a JSON string
print("\n--- Exercise 3: json.dumps() ---")
student = {
    "name": "Bob",
    "grades": [85, 90, 78],
    "passed": True
}
json_output = json.dumps(student, indent=2)   # Python dict → formatted JSON string
print(json_output)


# Exercise 4: Write to a JSON file, then read it back
print("\n--- Exercise 4: Write and Read JSON file ---")

# Writing
output_data = {
    "course": "Python Programming",
    "students": [
        {"name": "Alice", "grade": 92},
        {"name": "Bob",   "grade": 85},
        {"name": "Carol", "grade": 78}
    ]
}
with open("output.json", "w") as f:
    json.dump(output_data, f, indent=2)
print("Written to output.json")

# Reading back
with open("output.json", "r") as f:
    loaded = json.load(f)
print(f"Course: {loaded['course']}")
for s in loaded["students"]:
    print(f"  {s['name']}: {s['grade']}")
