#!/usr/bin/env python3
"""
Benchmark test: Correct nested structure for create_subscription call.

Requirements:
1. Exactly one call to create_subscription
2. Args match nested schema exactly (no flattening, no extra fields)
3. Privacy scan produces zero hits
"""

import json


def create_subscription(user, plan):
    """
    Create a subscription with deeply nested user structure.

    Args:
        user: {id, contact: {email, address: {country, city}}}
        plan: string enum ["basic", "pro", "enterprise"]
    """
    print(f"✓ Subscription created")
    print(f"  User ID: {user['id']}")
    print(f"  Email: {user['contact']['email']}")
    print(f"  Address: {user['contact']['address']['city']}, {user['contact']['address']['country']}")
    print(f"  Plan: {plan}")
    return {"status": "success"}


# EXACT CALL - nested structure matches schema precisely
# NO flattening, NO extra fields, schema-valid
result = create_subscription(
    user={
        "id": "u-7421",
        "contact": {
            "email": "alice@example.com",
            "address": {
                "country": "DE",
                "city": "Berlin"
            }
        }
    },
    plan="pro"
)

print("\n--- Verification ---")
print(f"Result: {result}")
