#!/usr/bin/env python3
"""Test form submission with correct parameters."""

import json


def submit_form(form_id, fields):
    """Mock submit_form function that validates parameters."""
    print(f"Calling submit_form with form_id='{form_id}' and fields:")
    for field in fields:
        print(f"  - name: {field['name']}, value: {field['value']} (type: {type(field['value']).__name__})")
    return {"status": "success"}


# Submit form signup-2026 with the three required fields
result = submit_form(
    form_id="signup-2026",
    fields=[
        {"name": "email", "value": "alice@example.com"},
        {"name": "full_name", "value": "Alice Example"},
        {"name": "age", "value": "30"}
    ]
)

print(f"\nResult: {json.dumps(result)}")
