import re
import yaml

# Load privacy patterns
with open('docs/privacy-patterns.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Read the solution file
with open('solution.py', 'r') as f:
    content = f.read()

# Check against patterns
hits = []
for pattern in config['patterns']:
    regex = pattern['regex']
    pattern_id = pattern['id']
    try:
        matches = list(re.finditer(regex, content, re.MULTILINE | re.DOTALL))
        if matches:
            hits.append((pattern_id, len(matches), matches))
    except Exception as e:
        print(f"Error checking pattern {pattern_id}: {e}")

# Report results
if hits:
    print(f"FAILED: Found {len(hits)} pattern(s) with hits:")
    for pattern_id, count, matches in hits:
        print(f"  - {pattern_id}: {count} match(es)")
        for match in matches[:3]:  # Show first 3 matches
            print(f"    {match.group()}")
else:
    print("PASSED: Zero hits - privacy scan successful!")

exit(len(hits))
