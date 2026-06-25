# directory_management/move_files.py
# Demonstrates moving and copying files between directories

import shutil
from pathlib import Path

# Setup source structure
src_dir = Path("source")
dst_dir = Path("destination")
backup_dir = Path("backup")

for d in [src_dir, dst_dir, backup_dir]:
    d.mkdir(exist_ok=True)

# Create sample files
files = ["alpha.txt", "beta.txt", "gamma.csv"]
for name in files:
    (src_dir / name).write_text(f"Data inside {name}\n")

print("=== Initial source contents ===")
for f in src_dir.iterdir():
    print(f"  {f.name}")

# --- Move a single file ---
print("\n=== shutil.move() — move one file ===")
shutil.move(str(src_dir / "alpha.txt"), str(dst_dir / "alpha.txt"))
print(f"Moved alpha.txt -> {dst_dir}")

# --- Copy a single file ---
print("\n=== shutil.copy() — copy one file ===")
shutil.copy(src_dir / "beta.txt", dst_dir / "beta_copy.txt")
print(f"Copied beta.txt -> destination/beta_copy.txt")

# --- Copy entire directory tree ---
print("\n=== shutil.copytree() — copy whole dir ===")
if backup_dir.exists():
    shutil.rmtree(backup_dir)
shutil.copytree(src_dir, backup_dir)
print(f"Copied entire '{src_dir}' -> '{backup_dir}'")
for f in backup_dir.iterdir():
    print(f"  {f.name}")

# --- Move entire directory ---
print("\n=== shutil.move() — move whole dir ===")
moved_dir = Path("moved_source")
if moved_dir.exists():
    shutil.rmtree(moved_dir)
shutil.move(str(src_dir), str(moved_dir))
print(f"Moved '{src_dir}' -> '{moved_dir}'")
for f in moved_dir.iterdir():
    print(f"  {f.name}")

# Final listing
print("\n=== Destination contents ===")
for f in dst_dir.iterdir():
    print(f"  {f.name}")

# Cleanup
for d in [dst_dir, backup_dir, moved_dir]:
    shutil.rmtree(d, ignore_errors=True)
print("\nCleanup done.")
