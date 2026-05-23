#!/usr/bin/env python3
"""
Benchmark test: Call submit_form with form_id="signup-2026" and three fields.
Fields are: email, full_name, and age (all values as strings per schema).
"""

# The exact call that meets all acceptance criteria:
result = submit_form(
    form_id="signup-2026",
    fields=[
        {"name": "email", "value": "alice@example.com"},
        {"name": "full_name", "value": "Alice Example"},
        {"name": "age", "value": "30"}
    ]
)

print(result)
