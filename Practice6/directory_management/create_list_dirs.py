# directory_management/create_list_dirs.py
# Demonstrates creating, listing, and searching directories

import os
import shutil
from pathlib import Path

base = Path("demo_dirs")

# --- Create nested directories ---
print("=== os.makedirs() — create nested dirs ===")
nested = base / "level1" / "level2" / "level3"
os.makedirs(nested, exist_ok=True)   # exist_ok=True prevents error if exists
print(f"Created: {nested}")

# Add some dummy files
for name in ["data.txt", "notes.csv", "image.png", "report.csv"]:
    (base / "level1" / name).write_text(f"content of {name}")
(base / "level1" / "level2" / "deep.txt").write_text("deep file")

# --- os.getcwd() and os.chdir() ---
print(f"\n=== Current directory ===")
print(f"os.getcwd(): {os.getcwd()}")

# --- os.listdir() ---
print(f"\n=== os.listdir('{base / 'level1'}') ===")
for entry in os.listdir(base / "level1"):
    print(f"  {entry}")

# --- os.walk() — recursive listing ---
print(f"\n=== os.walk() — all files and dirs recursively ===")
for root, dirs, files in os.walk(base):
    depth = root.replace(str(base), "").count(os.sep)
    indent = "  " * depth
    print(f"{indent}{Path(root).name}/")
    for file in files:
        print(f"{indent}  {file}")

# --- Find files by extension ---
print("\n=== Find all .csv files ===")
csv_files = list(base.rglob("*.csv"))
for p in csv_files:
    print(f"  {p}")

print("\n=== Find all .txt files ===")
txt_files = list(base.rglob("*.txt"))
for p in txt_files:
    print(f"  {p}")

# --- os.mkdir() vs os.makedirs() ---
print("\n=== os.mkdir() — single level only ===")
single = base / "single"
os.mkdir(single)
print(f"Created single dir: {single}")

# --- os.rmdir() — remove EMPTY dir only ---
os.rmdir(single)
print(f"Removed empty dir: {single}")

# Cleanup everything
shutil.rmtree(base)
print(f"\nRemoved entire tree: {base}")
