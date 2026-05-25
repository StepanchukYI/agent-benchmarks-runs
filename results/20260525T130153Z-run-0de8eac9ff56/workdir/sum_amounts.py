#!/usr/bin/env python3
import sys
import math

def is_valid_amount(value_str):
    """
    Check if a value is valid according to the rules:
    - Python's float() accepts it after removing underscores ONLY
    - NaN is explicitly excluded
    - Empty strings are invalid
    """
    if not value_str or value_str.strip() == '':
        return False

    # Remove underscores only
    processed = value_str.replace('_', '')

    try:
        num = float(processed)
        # NaN is explicitly not valid
        if math.isnan(num):
            return False
        return True
    except ValueError:
        return False

def main():
    total = 0.0

    with open('values.csv', 'r') as f:
        lines = f.readlines()

    # Skip header (first line)
    for line in lines[1:]:
        line = line.rstrip('\n')
        if not line:  # Skip empty lines
            continue

        parts = line.split(',', 1)  # Split on first comma only
        if len(parts) < 2:
            continue

        name, amount_str = parts
        amount_str = amount_str.strip()

        if is_valid_amount(amount_str):
            processed = amount_str.replace('_', '')
            total += float(processed)

    # Format to 2 decimal places
    result = f"{total:.2f}"

    # Write to out/sum.txt with NO trailing newline
    with open('out/sum.txt', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
