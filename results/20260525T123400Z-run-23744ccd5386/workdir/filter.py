#!/usr/bin/env python3
import json
import sys

# Read the seed file
with open('seed/items.json', 'r') as f:
    items = json.load(f)

# Filter items according to rules:
# 1. amount must be a JSON number (int or float; not string, not null)
# 2. currency must be present and equal to "USD"
# 3. Negative amounts are valid
filtered_ids = []
total_amount = 0.0

for item in items:
    # Check if amount is a number (not string, not null)
    # In Python, after json.load, numbers are int or float, strings are str, null is None
    if not isinstance(item.get('amount'), (int, float)) or isinstance(item.get('amount'), bool):
        continue

    # Check if currency is present and equals "USD"
    if item.get('currency') != 'USD':
        continue

    # If both conditions are met, include this item
    filtered_ids.append(item['id'])
    total_amount += item['amount']

# Sort ids in ascending order
filtered_ids.sort()

# Write filtered_ids.json (minified, no trailing newline)
with open('out/filtered_ids.json', 'w') as f:
    f.write(json.dumps(filtered_ids, separators=(',', ':')))

# Write sum.txt (formatted to 2 decimal places, no trailing newline)
with open('out/sum.txt', 'w') as f:
    f.write(f'{total_amount:.2f}')

print(f'Filtered IDs: {filtered_ids}')
print(f'Sum: {total_amount:.2f}')
