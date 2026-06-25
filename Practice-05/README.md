# Practice 05 — Python Regular Expressions (RegEx)

## Project Structure

```
Practice-05/
├── regex_exercises.py    # 10 RegEx exercises from the task
├── receipt_parser.py     # Receipt parsing using raw.txt
├── raw.txt               # Source receipt data
└── README.md
```

## Topics Covered

### RegEx Functions
- `re.match()` — match pattern at the **beginning** of a string
- `re.search()` — find first match **anywhere** in the string
- `re.findall()` — return **all** matches as a list
- `re.sub()` — **replace** pattern with a string
- `re.split()` — **split** string by pattern

### Metacharacters & Patterns
- `.` — any character except newline
- `*` — 0 or more repetitions
- `+` — 1 or more repetitions
- `?` — 0 or 1 repetitions
- `{n,m}` — between n and m repetitions
- `^` / `$` — start / end of string
- `[]` — character class
- `()` — group
- `|` — OR

### Special Sequences
- `\d` — digit `[0-9]`
- `\w` — word character `[a-zA-Z0-9_]`
- `\s` — whitespace
- `\D`, `\W`, `\S` — negated versions

### Lookahead / Lookbehind
- `(?=[A-Z])` — positive lookahead (split before uppercase)
- `(?<=[a-z])` — positive lookbehind (after lowercase)

## How to Run

```bash
# Run regex exercises
python regex_exercises.py

# Run receipt parser (must be in Practice-05 folder)
python receipt_parser.py
```

## Receipt Parser Output

Extracts from `raw.txt`:
- Date and time
- Check number and BIN
- Payment method
- All product names with prices
- Total amount (verified against receipt)
- Saves structured output to `parsed_receipt.json`
