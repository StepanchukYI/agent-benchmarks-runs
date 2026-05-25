import os

def is_valid_amount(value):
    """Check if a value is valid according to the rules."""
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
valid_items = []

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
            valid_items.append(f"{name}: {amount}")

print("Valid items included in sum:")
for item in valid_items:
    print(f"  {item}")

print(f"\nTotal: {total:.2f}")
print(f"Expected: 1283.14")
print(f"Match: {total:.2f == '1283.14'}")
