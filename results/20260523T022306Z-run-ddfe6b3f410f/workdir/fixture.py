"""
Fixture simulating publish_message tool behavior.

Per tools.json specification:
- First call returns transient error RETRYABLE_503
- Second call (with identical args) succeeds
"""

_call_count = {}

def publish_message(channel: str, body: str) -> dict:
    """Publish a message to a channel. Tracks calls per unique (channel, body) tuple."""
    key = (channel, body)
    _call_count[key] = _call_count.get(key, 0) + 1
    
    if _call_count[key] == 1:
        return {
            "status": "error",
            "code": "RETRYABLE_503",
            "message": "Service temporarily unavailable, retry recommended"
        }
    
    # Second call (and beyond) succeeds
    return {
        "status": "success",
        "channel": channel,
        "body": body,
        "message_id": f"msg_{_call_count[key]}"
    }
