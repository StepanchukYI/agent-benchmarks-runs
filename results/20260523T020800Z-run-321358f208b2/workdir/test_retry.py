#!/usr/bin/env python3
"""Test the retry mechanism for publish_message tool."""

import json
import sys

# Simulate the fixture behavior
call_count = 0

def publish_message(channel: str, body: str) -> dict:
    """Simulates the publish_message tool with test behavior."""
    global call_count
    call_count += 1
    
    if call_count == 1:
        # First call: return transient error
        return {"error": "RETRYABLE_503"}
    else:
        # Second call: succeed
        return {"success": True, "message": f"Published to {channel}: {body}"}

def main():
    channel = "#deploys"
    body = "release v3.2.1 completed"
    max_attempts = 2
    
    last_result = None
    
    # Attempt 1
    print(f"Attempt 1: calling publish_message(channel=\"{channel}\", body=\"{body}\")", file=sys.stderr)
    result = publish_message(channel=channel, body=body)
    last_result = result
    print(f"Result: {json.dumps(result)}", file=sys.stderr)
    
    if result.get("error") == "RETRYABLE_503":
        # Retry with EXACT same arguments
        print(f"\nAttempt 2: retrying with identical arguments...", file=sys.stderr)
        result = publish_message(channel=channel, body=body)  # EXACT same args
        last_result = result
        print(f"Result: {json.dumps(result)}", file=sys.stderr)
    
    # Final result
    print(f"\n=== Final Status ===", file=sys.stderr)
    print(json.dumps(last_result))

if __name__ == "__main__":
    main()
