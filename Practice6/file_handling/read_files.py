# file_handling/read_files.py
# Demonstrates reading files using different methods

from pathlib import Path

# Create a sample file to read
sample_path = Path("sample.txt")
sample_path.write_text(
    "Line 1: Python file handling\n"
    "Line 2: Reading files is easy\n"
    "Line 3: Using context managers\n"
    "Line 4: Pathlib is cross-platform\n"
    "Line 5: End of file\n",
    encoding="utf-8",
)

print("=== read() — entire file as one string ===")
with open(sample_path, "r", encoding="utf-8") as f:
    content = f.read()
print(content)

print("=== readline() — one line at a time ===")
with open(sample_path, "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        print(repr(line))
        line = f.readline()

print("\n=== readlines() — list of all lines ===")
with open(sample_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")
for i, line in enumerate(lines, 1):
    print(f"  [{i}] {line.strip()}")

print("\n=== Iterating line by line (memory-efficient) ===")
with open(sample_path, "r", encoding="utf-8") as f:
    for line in f:
        print(f"  >> {line.strip()}")

# Cleanup
sample_path.unlink()
print("\nSample file removed.")
