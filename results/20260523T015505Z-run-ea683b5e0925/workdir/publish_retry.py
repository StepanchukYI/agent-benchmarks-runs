"""
Demonstrates the correct retry-on-transient-error pattern:

1. Call publish_message(channel="#deploys", body="release v3.2.1 completed")
   → returns RETRYABLE_503 (transient)
2. Retry with EXACT same arguments
   → succeeds
3. Report final status

Acceptance: exactly 2 calls, identical args, success reported.
"""

call_count = 0
MAX_ATTEMPTS = 2

def publish_message(channel: str, body: str) -> dict:
    """
    Fixture: returns RETRYABLE_503 on the first call,
    succeeds on the second call with identical arguments.
    """
    global call_count
    call_count += 1

    if call_count == 1:
        # First call → transient error
        return {"status": "error", "error_code": "RETRYABLE_503", "message": "Service temporarily unavailable"}
    else:
        # Second call → success
        return {"status": "ok", "message_id": "msg_abc123", "channel": channel, "body": body}


def main():
    channel = "#deploys"
    body = "release v3.2.1 completed"
    attempts = 0
    last_result = None
    succeeded = False

    while attempts < MAX_ATTEMPTS:
        attempts += 1
        print(f"Attempt {attempts}: publish_message(channel={channel!r}, body={body!r})")
        result = publish_message(channel, body)
        last_result = result
        print(f"  → Result: {result}")

        if result.get("status") == "ok":
            succeeded = True
            break
        elif result.get("error_code") == "RETRYABLE_503" and attempts < MAX_ATTEMPTS:
            print("  → Transient error detected, retrying with same arguments...")
        else:
            print("  → Non-retryable error or max attempts reached.")

    # --- Final status report ---
    print()
    if succeeded:
        print(f"✅ SUCCESS after {attempts} attempt(s). Message published to {channel!r}.")
        print(f"   message_id: {last_result.get('message_id')}")
    else:
        print(f"❌ FAILURE after {attempts} attempt(s). Last error: {last_result}")

    # Verification
    assert call_count == 2, f"Expected exactly 2 calls, got {call_count}"
    assert succeeded, "Expected final success"
    print("\n[Verification passed: exactly 2 calls, identical args, success on retry]")


if __name__ == "__main__":
    main()
