import json

# Fixture: create_subscription(user, plan)
# user is a nested object: {id, contact: {email, address: {country, city}}}

def create_subscription(user, plan):
    """Create a subscription with billing details (deeply nested)."""
    return {"user": user, "plan": plan}


# Subscribe user u-7421 to the pro plan
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

print(json.dumps(result, indent=2))
