#!/usr/bin/env python3
"""Sum valid amount values from CSV with strict validation rules."""

import os

def is_valid(value_str):
    """
    Check if a value is valid for summing.

    Rules:
    - Remove underscores only (no comma removal, no locale conversion)
    - float() must accept the result
    - Exclude NaN explicitly (even though float('NaN') succeeds)
    - Empty values are invalid
    """
    # Empty or whitespace-only values are invalid
    if not value_str or not value_str.strip():
        return False

    # Remove underscores only
    cleaned = value_str.replace('_', '')

    # Try to convert to float
    try:
        result = float(cleaned)
        # Exclude NaN explicitly
        if result != result:  # NaN != NaN is True
            return False
        return True
    except (ValueError, TypeError):
        return False

# Read CSV and sum valid amounts
total = 0.0

with open('values.csv', 'r') as f:
    lines = f.readlines()

# Skip header (line 0) and process data rows
for line_num, line in enumerate(lines[1:], start=2):
    line = line.rstrip('\n\r')
    if not line:
        continue

    # Split only on the first comma to handle amounts that contain commas
    parts = line.split(',', 1)
    if len(parts) != 2:
        continue

    name, amount_str = parts

    if is_valid(amount_str):
        cleaned = amount_str.replace('_', '')
        value = float(cleaned)
        total += value

# Create output directory if needed
os.makedirs('out', exist_ok=True)

# Write result with exactly 2 decimal places and NO trailing newline
result_str = f'{total:.2f}'
with open('out/sum.txt', 'w', newline='') as f:
    f.write(result_str)
