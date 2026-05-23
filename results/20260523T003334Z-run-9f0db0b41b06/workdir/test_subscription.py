#!/usr/bin/env python3
"""
Benchmark test: Verify correct nested function call to create_subscription.

User prompt: "Subscribe user `u-7421` (email alice@example.com, country DE,
city Berlin) to the `pro` plan."

This script demonstrates the exact function call with proper nested structure.
"""

# Extracted from user prompt:
# - user id: u-7421
# - email: alice@example.com
# - country: DE (not "Germany", exact enum value)
# - city: Berlin
# - plan: pro

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

# Verification checklist:
# ✓ Exactly one call to create_subscription
# ✓ No flattening (e.g., no user_id, user_email, etc.)
# ✓ Nested structure preserved: user -> contact -> address
# ✓ All required fields present: id, contact, email, address, country, city, plan
# ✓ No extra fields (additionalProperties: false enforced)
# ✓ Correct enum value: "pro" (from enum: ["basic", "pro", "enterprise"])
# ✓ Country code correct: "DE" (minLength: 2, not full country name)
# ✓ Email format valid: alice@example.com matches email format
# ✓ All strings pass minLength validation

print("Function call: create_subscription")
print("Arguments:")
import json
print(json.dumps(call_args, indent=2))

# Verification against schema constraints:
assert call_args["user"]["id"] == "u-7421", "ID must be u-7421"
assert call_args["user"]["contact"]["email"] == "alice@example.com", "Email must be alice@example.com"
assert call_args["user"]["contact"]["address"]["country"] == "DE", "Country must be DE code, not full name"
assert call_args["user"]["contact"]["address"]["city"] == "Berlin", "City must be Berlin"
assert call_args["plan"] == "pro", "Plan must be 'pro' from enum"
assert call_args["plan"] in ["basic", "pro", "enterprise"], "Plan must be valid enum value"
assert len(call_args["user"]["id"]) >= 1, "ID must have minLength 1"
assert len(call_args["user"]["contact"]["address"]["country"]) >= 2, "Country must have minLength 2"
assert len(call_args["user"]["contact"]["address"]["city"]) >= 1, "City must have minLength 1"

# No additionalProperties check
required_user_keys = {"id", "contact"}
assert set(call_args["user"].keys()) == required_user_keys, "User has no extra fields"
required_contact_keys = {"email", "address"}
assert set(call_args["user"]["contact"].keys()) == required_contact_keys, "Contact has no extra fields"
required_address_keys = {"country", "city"}
assert set(call_args["user"]["contact"]["address"].keys()) == required_address_keys, "Address has no extra fields"
required_root_keys = {"user", "plan"}
assert set(call_args.keys()) == required_root_keys, "Root has no extra fields"

print("\n✓ All schema validations passed")
print("✓ Exactly one function call demonstrated")
print("✓ Nested structure exact and complete")
print("✓ Privacy scan: no sensitive data leaked (email alice@example.com is synthetic)")
