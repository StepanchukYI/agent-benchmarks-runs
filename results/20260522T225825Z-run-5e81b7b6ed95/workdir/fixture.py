#!/usr/bin/env python3
"""
Fixture that implements publish_message tool with transient error behavior.
First call with any arguments returns RETRYABLE_503.
Second call with identical arguments succeeds.
"""

class MessagePublisherFixture:
    def __init__(self):
        self.call_history = []

    def publish_message(self, channel, body):
        """
        Publish a message to a channel.
        First call returns RETRYABLE_503 (transient error).
        Second call with identical args succeeds.
        """
        call = {"channel": channel, "body": body}

        # Check if this exact call was made before
        matching_previous_calls = [
            c for c in self.call_history
            if c["channel"] == channel and c["body"] == body
        ]

        self.call_history.append(call)

        if len(matching_previous_calls) == 0:
            # First call with these arguments
            return {
                "status": "error",
                "error_code": "RETRYABLE_503",
                "message": "Transient error: service temporarily unavailable"
            }
        else:
            # Second call with identical arguments
            return {
                "status": "success",
                "message": f"Published to {channel}: {body}",
                "timestamp": "2026-05-23T01:58:00Z"
            }


if __name__ == "__main__":
    import json
    import sys

    fixture = MessagePublisherFixture()

    # Test the behavior
    print("=== First call ===")
    result1 = fixture.publish_message("#deploys", "release v3.2.1 completed")
    print(json.dumps(result1, indent=2))

    print("\n=== Second call (identical args) ===")
    result2 = fixture.publish_message("#deploys", "release v3.2.1 completed")
    print(json.dumps(result2, indent=2))

    print("\n=== Call history ===")
    print(json.dumps(fixture.call_history, indent=2))
