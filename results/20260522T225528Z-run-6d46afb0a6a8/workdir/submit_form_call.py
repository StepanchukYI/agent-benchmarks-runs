#!/usr/bin/env python3
"""
Test demonstrating the correct invocation of submit_form fixture.
This script shows how the submit_form function should be called with the
user's input: form signup-2026 with email, full_name, and age fields.
"""

# This would be the fixture call in a test environment
result = submit_form(
    form_id="signup-2026",
    fields=[
        {"name": "email", "value": "alice@example.com"},
        {"name": "full_name", "value": "Alice Example"},
        {"name": "age", "value": "30"}
    ]
)
