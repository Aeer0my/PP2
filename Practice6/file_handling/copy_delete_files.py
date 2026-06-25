# file_handling/copy_delete_files.py
# Demonstrates copying, backing up, and safely deleting files

import shutil
from pathlib import Path

# Setup
src = Path("original.txt")
src.write_text("This is the original file.\nIt contains important data.\n", encoding="utf-8")

# --- Copy a file ---
print("=== shutil.copy() ===")
backup = Path("backup.txt")
shutil.copy(src, backup)
print(f"Copied '{src}' -> '{backup}'")
print(f"Backup contents:\n{backup.read_text(encoding='utf-8')}")

# --- Copy with metadata preserved ---
print("=== shutil.copy2() (preserves metadata) ===")
backup2 = Path("backup_meta.txt")
shutil.copy2(src, backup2)
print(f"Copied with metadata: '{backup2}'")

# --- Safe delete (check existence first) ---
print("\n=== Safe delete ===")
for f in [backup, backup2]:
    if f.exists():
        f.unlink()
        print(f"Deleted: {f}")
    else:
        print(f"Not found (skipped): {f}")

# --- Try to delete a non-existent file without crashing ---
ghost = Path("ghost.txt")
try:
    ghost.unlink()
except FileNotFoundError:
    print(f"FileNotFoundError caught: '{ghost}' does not exist.")

# Python 3.8+: missing_ok=True avoids the exception entirely
ghost.unlink(missing_ok=True)
print("unlink(missing_ok=True) — no error even if file is absent.")

# Cleanup original
src.unlink(missing_ok=True)
print("\nAll done.")
