# file_handling/write_files.py
# Demonstrates writing and appending to files

from pathlib import Path

output = Path("output.txt")

# --- Write mode 'w' (creates or overwrites) ---
print("=== Writing with mode 'w' ===")
with open(output, "w", encoding="utf-8") as f:
    f.write("First line written with write()\n")
    f.writelines([
        "Second line via writelines()\n",
        "Third line via writelines()\n",
    ])
print(output.read_text(encoding="utf-8"))

# --- Append mode 'a' ---
print("=== Appending with mode 'a' ===")
with open(output, "a", encoding="utf-8") as f:
    f.write("Fourth line — appended\n")
    f.write("Fifth line — appended\n")
print(output.read_text(encoding="utf-8"))

# --- Exclusive creation mode 'x' (fails if file exists) ---
print("=== Exclusive creation with mode 'x' ===")
new_file = Path("new_only.txt")
if new_file.exists():
    new_file.unlink()
try:
    with open(new_file, "x", encoding="utf-8") as f:
        f.write("Created exclusively — file must not exist beforehand\n")
    print("File created successfully.")
    # Try again — should raise FileExistsError
    with open(new_file, "x", encoding="utf-8") as f:
        f.write("This should not run\n")
except FileExistsError:
    print("FileExistsError caught: file already exists, 'x' mode refused.")

# --- pathlib shortcut ---
print("\n=== pathlib write_text / read_text ===")
p = Path("pathlib_demo.txt")
p.write_text("Written directly via pathlib!\nNo open() needed.\n", encoding="utf-8")
print(p.read_text(encoding="utf-8"))

# Cleanup
for f in [output, new_file, p]:
    if f.exists():
        f.unlink()
print("Temp files removed.")
