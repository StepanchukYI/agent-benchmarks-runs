#!/usr/bin/env python3
import json
import os

# Read the seed file
with open('seed/items.json', 'r') as f:
    items = json.load(f)

# Filter items according to the rules:
# 1. amount must be a JSON number (int or float; not string, not null)
# 2. currency must be present and equal to "USD"
# 3. Negative amounts are valid
filtered_ids = []
total_sum = 0.0

for item in items:
    # Check if amount is a number (not string, not null)
    amount = item.get('amount')
    if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount is None:
        continue

    # Check if currency is present and equals "USD"
    currency = item.get('currency')
    if currency != "USD":
        continue

    # This item is valid
    filtered_ids.append(item['id'])
    total_sum += amount

# Sort the filtered ids in ascending order
filtered_ids.sort()

# Create the output directory if it doesn't exist
os.makedirs('out', exist_ok=True)

# Write filtered_ids.json - minified, no trailing newline
with open('out/filtered_ids.json', 'w') as f:
    f.write(json.dumps(filtered_ids, separators=(',', ':')))

# Write sum.txt - formatted to 2 decimal places, no trailing newline
with open('out/sum.txt', 'w') as f:
    f.write(f"{total_sum:.2f}")

print("Processing complete")
print(f"Filtered IDs: {filtered_ids}")
print(f"Sum: {total_sum:.2f}")
