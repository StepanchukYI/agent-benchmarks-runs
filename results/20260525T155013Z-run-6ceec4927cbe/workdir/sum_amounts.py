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
with open('values.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    
    for row in reader:
        if len(row) < 2:
            continue
        
        amount_str = row[1]
        
        if is_valid_amount(amount_str):
            total += parse_amount(amount_str)

# Format to 2 decimal places
result = f"{total:.2f}"

# Write to out/sum.txt without trailing newline
import os
os.makedirs('out', exist_ok=True)
with open('out/sum.txt', 'w') as f:
    f.write(result)

print(f"Sum: {result}")
