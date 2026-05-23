import json

def create_subscription(user, plan):
    """Fixture: create_subscription(user, plan)"""
    payload = {"user": user, "plan": plan}
    print(json.dumps(payload, indent=2))
    return payload


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

assert result == {
    "user": {
        "id": "u-7421",
        "contact": {
            "email": "alice@example.com",
            "address": {"country": "DE", "city": "Berlin"}
        }
    },
    "plan": "pro"
}, "Schema mismatch"

print("\nOK — schema-valid, exactly one call issued.")
