#!/usr/bin/env python3
"""
Benchmark test for set_temperature tool call.
Demonstrates correct parsing and invocation.
"""

import json
import re


def parse_temperature_command(user_prompt: str) -> dict:
    """
    Parse user prompt like "Set the thermostat to '22 celsius'."
    Returns a tool call dict with properly typed celsius value.

    Acceptance criteria:
    1. Extract numeric value (22) from the string
    2. Convert to proper numeric type (not string)
    3. Validate against schema range [-50, 50]
    4. Return exactly one tool call
    """
    # Extract the numeric value from the prompt
    # Handles patterns like "22 celsius", "'22 celsius'", etc.
    match = re.search(r"['\"]?(\-?\d+(?:\.\d+)?)\s*(?:celsius|°C|c)?['\"]?", user_prompt.lower())

    if not match:
        raise ValueError(f"Could not parse temperature from: {user_prompt}")

    # Convert to float/int - NOT a string
    celsius_value = float(match.group(1))

    # If it's a whole number, convert to int
    if celsius_value == int(celsius_value):
        celsius_value = int(celsius_value)

    # Validate against schema constraints
    if celsius_value < -50 or celsius_value > 50:
        raise ValueError(f"Temperature {celsius_value} outside valid range [-50, 50]")

    # Return the tool call in the expected format
    return {
        "tool": "set_temperature",
        "params": {
            "celsius": celsius_value  # MUST be numeric, NOT a string
        }
    }


# Test case from benchmark
user_prompt = "Set the thermostat to '22 celsius'."
result = parse_temperature_command(user_prompt)

print("Input prompt:", user_prompt)
print("\nGenerated tool call:")
print(json.dumps(result, indent=2))

# Verify correctness
assert result["tool"] == "set_temperature"
assert result["params"]["celsius"] == 22
assert isinstance(result["params"]["celsius"], int), "celsius must be numeric, not string"
assert -50 <= result["params"]["celsius"] <= 50, "celsius must be in valid range"

print("\n✓ All assertions passed")
print(f"✓ Exactly one tool call issued")
print(f"✓ celsius={result['params']['celsius']} (numeric type: {type(result['params']['celsius']).__name__})")
print(f"✓ Value within schema range [-50, 50]")
