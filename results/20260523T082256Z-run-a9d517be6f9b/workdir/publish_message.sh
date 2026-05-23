#!/usr/bin/env bash
# publish_message fixture — mirrors tools.json _test_behavior:
#   first call  → RETRYABLE_503
#   second call → success
# State is tracked via a counter file to survive across invocations.

set -euo pipefail

CHANNEL="$1"
BODY="$2"
COUNTER_FILE="$(dirname "$0")/.publish_call_count"

# Read and increment the call counter atomically (single-process context is fine here)
count=0
if [[ -f "$COUNTER_FILE" ]]; then
  count=$(cat "$COUNTER_FILE")
fi
count=$((count + 1))
echo "$count" > "$COUNTER_FILE"

if [[ $count -eq 1 ]]; then
  echo "ERROR: RETRYABLE_503 (attempt $count)" >&2
  exit 503
else
  echo "OK: message published to channel='$CHANNEL' body='$BODY' (attempt $count)"
  exit 0
fi
