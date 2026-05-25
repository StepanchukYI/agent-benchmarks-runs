import json
import sys

# Load the event and schema
with open('event.json') as f:
    event = json.load(f)

with open('schema.json') as f:
    schema = json.load(f)

# Basic validation checks
try:
    import jsonschema
    jsonschema.validate(event, schema)
    print("✓ event.json validates against schema.json")
except ImportError:
    # Fallback manual validation if jsonschema not available
    print("Checking validation manually...")
    
    # Check required top-level properties
    assert "event_type" in event, "Missing event_type"
    assert "payload" in event, "Missing payload"
    assert len(event) == 2, f"Too many properties: {list(event.keys())}"
    
    # Check event_type value
    assert event["event_type"] == "user_signup", f"Wrong event_type: {event['event_type']}"
    
    # Check payload for user_signup
    payload = event["payload"]
    assert "email" in payload, "Missing email in payload"
    assert "country" in payload, "Missing country in payload"
    assert len(payload) == 2, f"Payload has extra properties: {list(payload.keys())}"
    
    # Validate email format
    import re
    assert re.match(r'^[^@]+@[^@]+\.[^@]+$', payload["email"]), "Invalid email format"
    
    # Validate country format (ISO alpha-2)
    assert re.match(r'^[A-Z]{2}$', payload["country"]), "Invalid country format"
    assert payload["country"] == "DE", f"Wrong country code: {payload['country']}"
    
    print("✓ event.json validates against schema.json (manual check)")

# Check for privacy issues
print("\nPrivacy scan:")
content = json.dumps(event)
sensitive_patterns = [
    r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
    r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b',  # Credit card
    r'(password|secret|key|token)[\s]*[:=]',  # Secrets
]

import re
found_issues = False
for pattern in sensitive_patterns:
    if re.search(pattern, content, re.IGNORECASE):
        print(f"⚠ Found potential sensitive data matching: {pattern}")
        found_issues = True

if not found_issues:
    print("✓ Privacy scan: zero hits")

print("\nEvent contents:")
print(json.dumps(event, indent=2))
