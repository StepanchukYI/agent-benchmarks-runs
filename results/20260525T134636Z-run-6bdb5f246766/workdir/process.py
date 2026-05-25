import os
import math

# Ensure out directory exists
os.makedirs('out', exist_ok=True)

values = []

with open('values.csv', 'r') as f:
    lines = f.readlines()
    # Skip header row (first line)
    for line in lines[1:]:
        # Split on first comma only to handle values like "1,234"
        parts = line.strip().split(',', 1)
        if len(parts) >= 2:
            value_str = parts[1]

            # Rule: Remove underscores ONLY
            cleaned = value_str.replace('_', '')

            # Rule: Try to convert to float
            try:
                num = float(cleaned)
                # Rule: NaN is NOT valid — exclude it explicitly
                if math.isnan(num):
                    continue
                values.append(num)
            except ValueError:
                # Invalid value — skip
                pass

# Sum the valid values
total = sum(values)

# Format to 2 decimal places (no trailing newline)
result = f"{total:.2f}"

# Write to file without trailing newline
with open('out/sum.txt', 'w') as f:
    f.write(result)

print(f"Valid values: {values}")
print(f"Sum: {result}")
