#!/usr/bin/env python3
"""
Validate that the constructed arguments match the schema exactly.
"""

import json
from jsonschema import validate, ValidationError

# Load schema from tools.json
with open("tools.json") as f:
    tools_def = json.load(f)

schema = tools_def["tools"][0]["parameters"]

# The arguments we constructed from the user prompt
call_args = {
    "user": {
        "id": "u-7421",
        "contact": {
            "email": "alice@example.com",
            "address": {
                "country": "DE",
                "city": "Berlin"
            }
        }
    },
    "plan": "pro"
}

# Validate
try:
    validate(instance=call_args, schema=schema)
    print("✓ PASS: Arguments are schema-valid")
    print(f"\nConstructed call:")
    print(json.dumps(call_args, indent=2))
except ValidationError as e:
    print(f"✗ FAIL: {e.message}")
    exit(1)
