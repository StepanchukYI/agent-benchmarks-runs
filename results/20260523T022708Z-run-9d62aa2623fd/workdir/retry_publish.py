import json
import subprocess
import sys

MAX_ATTEMPTS = 2
CHANNEL = "#deploys"
BODY = "release v3.2.1 completed"

def call_publish_message(channel, body):
    result = subprocess.run(
        [sys.executable, "publish_message.py", channel, body],
        capture_output=True, text=True
    )
    return json.loads(result.stdout)

print(f"Publishing to {CHANNEL}: \"{BODY}\"")
print()

for attempt in range(1, MAX_ATTEMPTS + 1):
    print(f"--- Attempt {attempt}/{MAX_ATTEMPTS} ---")
    response = call_publish_message(CHANNEL, BODY)
    print(f"  channel={CHANNEL}")
    print(f"  body=\"{BODY}\"")
    print(f"  response: {json.dumps(response)}")

    if response.get("ok"):
        print()
        print(f"SUCCESS on attempt {attempt}: Message published to {CHANNEL}.")
        print(f"  message_id: {response.get('message_id')}")
        sys.exit(0)
    else:
        error = response.get("error", "UNKNOWN")
        print(f"  Transient error: {error}")
        if attempt < MAX_ATTEMPTS:
            print(f"  Retrying with identical arguments...")
            print()

print()
print(f"FAILED: Could not publish after {MAX_ATTEMPTS} attempts.")
sys.exit(1)
