import json
import subprocess
import sys

# Patch publish_message.py to also log args
STATE_FILE = "verify_state.json"

def call_publish(channel, body):
    result = subprocess.run(
        [sys.executable, "publish_message.py", channel, body],
        capture_output=True, text=True
    )
    return json.loads(result.stdout)

calls = []

# Reset state
with open("publish_state.json", "w") as f:
    json.dump({"call_count": 0}, f)

for attempt in range(1, 3):
    response = call_publish("#deploys", "release v3.2.1 completed")
    calls.append({
        "attempt": attempt,
        "channel": "#deploys",
        "body": "release v3.2.1 completed",
        "response": response
    })
    if response.get("ok"):
        break

print("=== Verification ===")
print(f"Total calls: {len(calls)}")
print(f"All channels identical: {len(set(c['channel'] for c in calls)) == 1}")
print(f"All bodies identical: {len(set(c['body'] for c in calls)) == 1}")
print(f"First call error: {calls[0]['response'].get('error')}")
print(f"Second call success: {calls[1]['response'].get('ok')}")
print()
print("Detailed call log:")
for c in calls:
    print(json.dumps(c, indent=2))
