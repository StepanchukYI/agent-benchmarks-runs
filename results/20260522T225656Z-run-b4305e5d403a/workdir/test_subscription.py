#!/usr/bin/env python3
"""
Benchmark test: Subscribe user u-7421 to pro plan with exact nested structure.
"""
import json

def create_subscription(user, plan):
    """Mock subscription creation (schema-validated by tools.json)."""
    return {"status": "success", "subscription_id": "sub-" + user["id"]}

# Issue exactly one call with EXACT nested structure
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

print(json.dumps({
    "call": "create_subscription",
    "args": {
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
    },
    "result": result
}, indent=2))
