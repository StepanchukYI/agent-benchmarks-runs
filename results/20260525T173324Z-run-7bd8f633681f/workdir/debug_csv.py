import csv

def is_valid_amount(value):
    """Check if a value is valid according to the rules."""
    if not value:  # Empty string
        return False
    
    # Remove underscores only (no comma removal)
    value_processed = value.replace('_', '')
    
    # Explicitly exclude NaN (case-insensitive)
    if value_processed.upper() == 'NAN':
        return False
    
    # Try to convert to float - if it works, it's valid
    try:
        float(value_processed)
        return True
    except ValueError:
        return False

def parse_amount(value):
    """Parse a valid amount to float."""
    # Remove underscores
    value_processed = value.replace('_', '')
    return float(value_processed)

# Read CSV and sum valid amounts
total = 0.0
valid_values = []

with open('values.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    
    for row in reader:
        if len(row) < 2:  # Skip malformed rows
            continue
        
        name = row[0]
        amount_str = row[1]
        
        print(f"Row: {name}, amount_str: '{amount_str}'")
        
        if is_valid_amount(amount_str):
            amount = parse_amount(amount_str)
            total += amount
            valid_values.append((name, amount))
            print(f"  VALID: {amount}")
        else:
            print(f"  INVALID")

print(f"\nValid values: {valid_values}")
print(f"Sum: {total}")
print(f"Sum (2 decimal places): {total:.2f}")
