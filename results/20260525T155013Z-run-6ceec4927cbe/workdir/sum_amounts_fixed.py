import csv

def is_valid_amount(value):
    """Check if a value is valid according to the rules."""
    # Remove underscores only (no comma removal, no locale conversion)
    cleaned = value.replace('_', '')
    
    # Empty string is invalid
    if not cleaned:
        return False
    
    # NaN is explicitly invalid
    if cleaned.upper() == 'NAN':
        return False
    
    # Try to convert to float
    try:
        float(cleaned)
        return True
    except ValueError:
        return False

def parse_amount(value):
    """Parse a valid amount to float."""
    cleaned = value.replace('_', '')
    return float(cleaned)

# Read the CSV and sum valid amounts
total = 0.0
valid_values = []

with open('values.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    
    for row in reader:
        if len(row) < 1:
            continue
        
        name = row[0]
        
        # Handle case where amount value contains commas (extra columns)
        # If there are more than 2 columns, join the rest with commas
        if len(row) > 2:
            amount_str = ','.join(row[1:])
        elif len(row) == 2:
            amount_str = row[1]
        else:
            amount_str = ''
        
        print(f"Processing: {name}, '{amount_str}'")
        
        if is_valid_amount(amount_str):
            parsed = parse_amount(amount_str)
            print(f"  -> VALID: {parsed}")
            total += parsed
            valid_values.append(parsed)
        else:
            print(f"  -> INVALID (skipped)")

print(f"\nValid values: {valid_values}")
print(f"Sum: {total}")
print(f"Formatted: {total:.2f}")

# Write to out/sum.txt without trailing newline
import os
os.makedirs('out', exist_ok=True)
result = f"{total:.2f}"
with open('out/sum.txt', 'w') as f:
    f.write(result)
