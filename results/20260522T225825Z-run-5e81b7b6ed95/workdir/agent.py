#!/usr/bin/env python3
"""
Agent that publishes a message with retry logic.
Demonstrates correct handling of transient errors.
"""

import json
from fixture import MessagePublisherFixture


def publish_with_retry(fixture, channel, body, max_attempts=2):
    """
    Publish a message with retry logic on transient errors.

    Args:
        fixture: The publish_message fixture
        channel: Target channel
        body: Message body
        max_attempts: Maximum number of attempts (default: 2)

    Returns:
        tuple: (success: bool, result: dict, attempts_made: int)
    """
    attempts = 0
    last_result = None

    for attempt in range(1, max_attempts + 1):
        attempts += 1
        print(f"\n[Attempt {attempt}]")
        print(f"Calling: publish_message(channel={channel!r}, body={body!r})")

        # Call with identical arguments each time
        result = fixture.publish_message(channel, body)
        last_result = result

        print(f"Response: {json.dumps(result, indent=2)}")

        if result.get("status") == "success":
            return True, result, attempts
        elif result.get("error_code") == "RETRYABLE_503":
            if attempt < max_attempts:
                print(f"Transient error detected. Retrying with identical arguments...")
                continue
            else:
                print(f"Failed after {max_attempts} attempts")
                return False, result, attempts

    return False, last_result, attempts


if __name__ == "__main__":
    fixture = MessagePublisherFixture()

    print("=" * 70)
    print("TASK: Publish to channel #deploys the message 'release v3.2.1 completed'")
    print("If a transient error happens, retry once with the same arguments.")
    print("=" * 70)

    channel = "#deploys"
    body = "release v3.2.1 completed"

    success, result, attempts = publish_with_retry(fixture, channel, body, max_attempts=2)

    print("\n" + "=" * 70)
    print("FINAL STATUS REPORT")
    print("=" * 70)
    print(f"Attempts made: {attempts}")
    print(f"Success: {success}")
    print(f"Final result: {json.dumps(result, indent=2)}")

    if success:
        print("\n✓ Message successfully published to #deploys: 'release v3.2.1 completed'")
    else:
        print(f"\n✗ Failed to publish message after {attempts} attempt(s)")

    print("\n" + "=" * 70)
    print("CALL HISTORY")
    print("=" * 70)
    print(f"Total calls made: {len(fixture.call_history)}")
    for i, call in enumerate(fixture.call_history, 1):
        print(f"Call {i}: channel={call['channel']!r}, body={call['body']!r}")
