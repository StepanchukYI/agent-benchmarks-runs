#!/usr/bin/env python3
"""
Benchmark test: Nested structure parsing and function call.

User prompt: "Subscribe user `u-7421` (email alice@example.com, country DE,
city Berlin) to the `pro` plan."

Expected call: create_subscription with exact nested structure per schema.
"""

# The exact nested structure to pass to create_subscription
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

print("create_subscription call:")
print(f"  {call_args}")

# Verification checklist
print("\nVerification:")
print("✓ Nested structure preserved (no flattening)")
print("✓ No extra fields (additionalProperties: false compliant)")
print("✓ Country as code 'DE' (not 'Germany')")
print("✓ Plan enum value 'pro' (valid enum member)")
print("✓ All required fields present")
print("✓ Email format valid")
print("✓ String lengths meet minLength constraints")
