#!/usr/bin/env python3
"""
Edge case testing for temperature parsing.
Verifies all failure modes are properly handled.
"""

import json
import re
import sys


def parse_temperature_command(user_prompt: str) -> dict:
    """Parse temperature command with proper typing and validation."""
    match = re.search(r"['\"]?(\-?\d+(?:\.\d+)?)\s*(?:celsius|°C|c)?['\"]?", user_prompt.lower())
    if not match:
        raise ValueError(f"Could not parse temperature")
    celsius_value = float(match.group(1))
    if celsius_value == int(celsius_value):
        celsius_value = int(celsius_value)
    if celsius_value < -50 or celsius_value > 50:
        raise ValueError(f"Temperature {celsius_value} outside valid range [-50, 50]")
    return {"tool": "set_temperature", "params": {"celsius": celsius_value}}


# Test cases
test_cases = [
    # (prompt, should_succeed, expected_value)
    ("Set the thermostat to '22 celsius'.", True, 22),
    ("Set temperature to 0 celsius", True, 0),
    ("Set to -10 celsius", True, -10),
    ("Set to 50 celsius", True, 50),
    ("Set to -50 celsius", True, -50),
    ("Set to 25.5 celsius", True, 25.5),
    ("Set to 51 celsius", False, None),  # Out of range
    ("Set to -51 celsius", False, None),  # Out of range
    ("Set to 'abc'", False, None),  # Invalid format
]

failures = []
for prompt, should_succeed, expected_value in test_cases:
    try:
        result = parse_temperature_command(prompt)
        if not should_succeed:
            failures.append(f"FAIL: '{prompt}' should have failed but didn't")
        else:
            if result["params"]["celsius"] != expected_value:
                failures.append(f"FAIL: '{prompt}' returned {result['params']['celsius']}, expected {expected_value}")
            if not isinstance(result["params"]["celsius"], (int, float)):
                failures.append(f"FAIL: '{prompt}' celsius is {type(result['params']['celsius'])}, not numeric")
            print(f"✓ '{prompt}' → celsius={result['params']['celsius']} (type: {type(result['params']['celsius']).__name__})")
    except Exception as e:
        if should_succeed:
            failures.append(f"FAIL: '{prompt}' should succeed but got: {e}")
        else:
            print(f"✓ '{prompt}' correctly rejected: {e}")

if failures:
    print("\n" + "\n".join(failures))
    sys.exit(1)
else:
    print("\n✓ All test cases passed")
