# receipt_parser.py
# Practical exercise: Parse receipt data from raw.txt using RegEx
import re
import json


def parse_receipt(filepath):
    """Parse a receipt text file and extract structured data."""

    with open(filepath, encoding="utf-8") as f:
        text = f.read()

    result = {}

    # --- 1. Extract date and time ---
    # Pattern matches: 18.04.2019 11:13:58
    dt_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)
    if dt_match:
        result["date"] = dt_match.group(1)
        result["time"] = dt_match.group(2)

    # --- 2. Extract store / company info ---
    bin_match = re.search(r"БИН\s+(\d+)", text)
    if bin_match:
        result["BIN"] = bin_match.group(1)

    check_match = re.search(r"Чек №(\d+)", text)
    if check_match:
        result["check_number"] = check_match.group(1)

    # --- 3. Find payment method ---
    if re.search(r"Банковская карта", text):
        result["payment_method"] = "Банковская карта"
    elif re.search(r"Наличные", text):
        result["payment_method"] = "Наличные"
    else:
        result["payment_method"] = "Неизвестно"

    # --- 4. Extract total amount ---
    # ИТОГО: followed by the amount on the next line (may have spaces: 18 009,00)
    total_match = re.search(r"ИТОГО:\s*\n([\d\s]+,\d{2})", text)
    if total_match:
        total_str = total_match.group(1).replace(" ", "").replace(",", ".")
        result["total"] = float(total_str)

    # --- 5. Extract item prices from "qty x unit_price" lines ---
    # Each product has a line like: 2,000 x 154,00
    # The number after x is the unit price; total for item = qty * unit
    # We extract the item total from the line immediately after qty x price
    item_prices = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # Match quantity x price pattern
        if re.match(r"[\d\s]+,\d{3}\s+x\s+[\d\s]+,\d{2}", line.strip()):
            # The NEXT non-empty line is the item total
            for j in range(i + 1, min(i + 3, len(lines))):
                candidate = lines[j].strip()
                if re.match(r"^[\d\s]+,\d{2}$", candidate):
                    val = float(candidate.replace(" ", "").replace(",", "."))
                    item_prices.append(val)
                    break
    result["all_prices"] = item_prices

    # --- 6. Extract product names ---
    products = []
    for i, line in enumerate(lines):
        if re.match(r"^\d+\.$", line.strip()):
            for j in range(i + 1, min(i + 3, len(lines))):
                name = lines[j].strip()
                if name:
                    products.append(name)
                    break
    result["products"] = products

    return result


def display_receipt(data):
    """Print parsed receipt data in a readable format."""
    print("=" * 60)
    print("           PARSED RECEIPT")
    print("=" * 60)
    print(f"Date:           {data.get('date', 'N/A')}")
    print(f"Time:           {data.get('time', 'N/A')}")
    print(f"Check №:        {data.get('check_number', 'N/A')}")
    print(f"BIN:            {data.get('BIN', 'N/A')}")
    print(f"Payment:        {data.get('payment_method', 'N/A')}")
    print(f"Total:          {data.get('total', 0):,.2f} тг")
    print("-" * 60)
    print("Products:")
    prices = data.get("all_prices", [])
    for i, product in enumerate(data.get("products", [])):
        price = prices[i] if i < len(prices) else 0
        print(f"  {i+1:>2}. {product[:45]:<45} {price:>10,.2f} тг")
    print("-" * 60)
    calculated_total = sum(data.get("all_prices", []))
    print(f"Calculated sum: {calculated_total:,.2f} тг")
    print(f"Receipt total:  {data.get('total', 0):,.2f} тг")
    print("=" * 60)


if __name__ == "__main__":
    data = parse_receipt("raw.txt")
    display_receipt(data)

    with open("parsed_receipt.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("\nSaved structured data to parsed_receipt.json")
