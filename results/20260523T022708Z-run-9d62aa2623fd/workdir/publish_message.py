import json
import sys

STATE_FILE = "publish_state.json"

def get_state():
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {"call_count": 0}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def publish_message(channel, body):
    state = get_state()
    state["call_count"] += 1
    save_state(state)

    if state["call_count"] == 1:
        return {"ok": False, "error": "RETRYABLE_503", "status": 503}
    else:
        return {"ok": True, "status": 200, "message_id": "msg_abc123"}

if __name__ == "__main__":
    channel = sys.argv[1]
    body = sys.argv[2]
    result = publish_message(channel, body)
    print(json.dumps(result))
