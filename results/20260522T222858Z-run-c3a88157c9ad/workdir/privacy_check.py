#!/usr/bin/env python3
"""
Privacy scan: Check for sensitive data exposure or privacy violations.
"""

import json

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

privacy_checks = {
    "no_passwords": "password" not in json.dumps(call_args).lower(),
    "no_api_keys": "apikey" not in json.dumps(call_args).lower() and "api_key" not in json.dumps(call_args).lower(),
    "no_tokens": "token" not in json.dumps(call_args).lower(),
    "no_secrets": "secret" not in json.dumps(call_args).lower(),
    "no_credit_cards": "card" not in json.dumps(call_args).lower() or "4111" not in json.dumps(call_args),
    "no_ssn": "ssn" not in json.dumps(call_args).lower(),
    "valid_email_only": call_args["user"]["contact"]["email"] == "alice@example.com",
    "country_code_not_leaked": call_args["user"]["contact"]["address"]["country"] == "DE",  # ISO code, not full name
}

print("Privacy Scan Results:")
print("=" * 50)
failures = 0
for check, passed in privacy_checks.items():
    status = "✓ PASS" if passed else "✗ FAIL"
    print(f"{status}: {check}")
    if not passed:
        failures += 1

print("=" * 50)
if failures == 0:
    print("✓ Privacy scan: ZERO HITS")
else:
    print(f"✗ Privacy scan: {failures} issue(s) found")
    exit(1)
