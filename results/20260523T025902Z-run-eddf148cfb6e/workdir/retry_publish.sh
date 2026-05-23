#!/usr/bin/env bash
set -euo pipefail

# --- Simulated fixture state ---
ATTEMPT=0
CHANNEL=""
BODY=""
FINAL_STATUS=""

# --- Simulated publish_message tool ---
# First call  -> returns RETRYABLE_503 (transient error)
# Second call -> succeeds
publish_message() {
  local ch="$1"
  local bd="$2"
  ATTEMPT=$((ATTEMPT + 1))
  echo "[Attempt $ATTEMPT] publish_message(channel=\"$ch\", body=\"$bd\")"

  if [ "$ATTEMPT" -eq 1 ]; then
    echo "  -> Response: RETRYABLE_503  (transient error)"
    return 1
  else
    echo "  -> Response: SUCCESS"
    FINAL_STATUS="success"
    return 0
  fi
}

# --- Agent logic (max 2 attempts, retry once on transient error) ---
CHANNEL="#deploys"
BODY="release v3.2.1 completed"
MAX_ATTEMPTS=2

for (( i=1; i<=MAX_ATTEMPTS; i++ )); do
  if publish_message "$CHANNEL" "$BODY"; then
    break
  else
    if [ "$i" -lt "$MAX_ATTEMPTS" ]; then
      echo "  -> Retrying with identical arguments..."
    else
      FINAL_STATUS="failed after $MAX_ATTEMPTS attempts"
    fi
  fi
done

# --- Final status report ---
echo ""
echo "=== Final Status Report ==="
echo "Channel : $CHANNEL"
echo "Body    : $BODY"
echo "Attempts: $ATTEMPT"
echo "Status  : $FINAL_STATUS"
