#!/usr/bin/env python3
"""Retry mechanism test for publish_message tool."""

import json
import sys

def publish_message(channel: str, body: str) -> dict:
    """Call the publish_message tool. Returns response from tool invocation."""
    tool_call = {
        "name": "publish_message",
        "parameters": {
            "channel": channel,
            "body": body
        }
    }
    print(json.dumps(tool_call), file=sys.stderr)
    return json.loads(sys.stdin.readline().strip())

def main():
    channel = "#deploys"
    body = "release v3.2.1 completed"
    max_attempts = 2
    
    last_result = None
    for attempt in range(1, max_attempts + 1):
        result = publish_message(channel=channel, body=body)
        last_result = result
        
        if result.get("error") == "RETRYABLE_503":
            if attempt < max_attempts:
                # Retry with exact same arguments
                continue
        break
    
    # Output final result
    print(json.dumps(last_result))

if __name__ == "__main__":
    main()
