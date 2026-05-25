import math
import os

# Read the CSV file
with open('values.csv', 'r') as f:
    lines = f.readlines()

# Skip header, process data rows
valid_sum = 0.0

for line in lines[1:]:  # Skip header row
    line = line.rstrip('\n')
    if not line:
        continue

    # Split on first comma only to separate name from amount
    parts = line.split(',', 1)
    if len(parts) < 2:
        continue

    amount_str = parts[1].strip()

    # Empty value is invalid
    if not amount_str:
        continue

    # Remove underscores only (no comma removal, no locale conversion)
    amount_str_cleaned = amount_str.replace('_', '')

    try:
        value = float(amount_str_cleaned)
        # Reject NaN explicitly
        if math.isnan(value):
            continue
        # Valid value, add to sum
        valid_sum += value
    except ValueError:
        # Invalid value (e.g., contains commas, alpha strings), skip
        continue

# Format to 2 decimal places
result = f"{valid_sum:.2f}"

# Create out directory if it doesn't exist
os.makedirs('out', exist_ok=True)

# Write to file with no trailing newline
with open('out/sum.txt', 'w') as f:
    f.write(result)

print(f"Sum: {result}")
