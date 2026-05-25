import os

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

with open('values.csv', 'r') as f:
    lines = f.readlines()
    
    # Skip header row
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        
        # Split on first comma only to preserve commas in the amount value
        parts = line.split(',', 1)
        
        if len(parts) < 2:
            continue
        
        amount_str = parts[1].strip()
        
        if is_valid_amount(amount_str):
            amount = parse_amount(amount_str)
            total += amount

# Format to 2 decimal places
result = f"{total:.2f}"

# Write to output file with no trailing newline
os.makedirs('out', exist_ok=True)

with open('out/sum.txt', 'w') as f:
    f.write(result)

print(f"Sum: {result}")
