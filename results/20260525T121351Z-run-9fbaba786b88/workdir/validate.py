import json
import re
import sys

# Load schema and config
with open('schema.json', 'r') as f:
    schema = json.load(f)

with open('config.json', 'r') as f:
    config = json.load(f)

# Validate manually
errors = []

# Check required fields
required = schema.get('required', [])
for field in required:
    if field not in config:
        errors.append(f"Missing required field: {field}")

# Check 'name' field
if 'name' in config:
    if not isinstance(config['name'], str):
        errors.append("'name' must be a string")
    elif len(config['name']) == 0:
        errors.append("'name' must have minLength 1")
    else:
        print(f"✓ 'name' field is valid: '{config['name']}'")

# Check 'version' field
if 'version' in config:
    if not isinstance(config['version'], str):
        errors.append("'version' must be a string")
    else:
        pattern = r'^[0-9]+\.[0-9]+\.[0-9]+$'
        if not re.match(pattern, config['version']):
            errors.append(f"'version' does not match pattern: {config['version']}")
        else:
            print(f"✓ 'version' field matches semver pattern: '{config['version']}'")

if errors:
    print("✗ Validation failed:")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)
else:
    print("\n✓ Validation passed")
    print(f"\nConfig content:")
    print(json.dumps(config, indent=2))
