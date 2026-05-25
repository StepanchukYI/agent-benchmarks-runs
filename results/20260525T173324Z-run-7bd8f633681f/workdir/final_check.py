import os

def is_valid_amount(value):
    if not value:
        return False
    value_processed = value.replace('_', '')
    if value_processed.upper() == 'NAN':
        return False
    try:
        float(value_processed)
        return True
    except ValueError:
        return False

def parse_amount(value):
    value_processed = value.replace('_', '')
    return float(value_processed)

total = 0.0

with open('values.csv', 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',', 1)
        if len(parts) < 2:
            continue
        name = parts[0].strip()
        amount_str = parts[1].strip()
        if is_valid_amount(amount_str):
            amount = parse_amount(amount_str)
            total += amount
            print(f"  ✓ {name}: {amount_str} -> {amount}")
        else:
            print(f"  ✗ {name}: {amount_str} (invalid)")

print(f"\nCalculated sum: {total:.2f}")
print(f"Expected sum:   1283.14")
print(f"Result: {'PASS' if total == 1283.14 else 'FAIL'}")

# Verify output file
with open('out/sum.txt', 'r') as f:
    content = f.read()
    print(f"\nOutput file content: '{content}'")
    print(f"File size: {len(content)} bytes")
    print(f"Correct content: {'PASS' if content == '1283.14' else 'FAIL'}")
