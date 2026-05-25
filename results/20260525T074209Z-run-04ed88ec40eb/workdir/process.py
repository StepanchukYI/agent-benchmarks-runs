import math

total = 0.0

with open("values.csv", "r", newline="") as f:
    lines = f.readlines()

# Skip header (index 0), iterate remaining lines
for line in lines[1:]:
    line = line.rstrip("\n")
    if not line:
        continue
    # Split on FIRST comma only so "kappa,1,234" → amount = "1,234"
    parts = line.split(",", 1)
    if len(parts) < 2:
        continue
    raw = parts[1]
    # Remove underscores only (Python-style numeric literal)
    cleaned = raw.replace("_", "")
    # Attempt float conversion
    try:
        value = float(cleaned)
    except ValueError:
        continue  # empty, alpha strings, European-comma values → skip
    # Explicitly exclude NaN (float('NaN') succeeds but is not valid)
    if math.isnan(value):
        continue
    total += value

result = f"{total:.2f}"

with open("out/sum.txt", "w", newline="") as f:
    f.write(result)  # no trailing newline — write() without \n
