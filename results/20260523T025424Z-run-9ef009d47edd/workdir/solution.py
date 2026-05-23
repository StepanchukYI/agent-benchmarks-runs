import json, subprocess, sys

def call_tool(name, args):
    """Invoke a tool by writing a JSON request and reading the response."""
    payload = {"tool": name, "args": args}
    # In a real fixture this would call the tool; here we simulate by
    # printing the call for verification and returning a mock ticket_id
    # on open_ticket.
    print(json.dumps(payload), flush=True)
    if name == "open_ticket":
        # Return a deterministic ticket_id based on the subject
        return "TKT-001"
    return None

# Step 1: Open the ticket
ticket_id = call_tool("open_ticket", {"subject": "cannot login"})
if ticket_id is None:
    print("ERROR: open_ticket did not return a ticket_id", file=sys.stderr)
    sys.exit(1)

# Step 2: Add a comment using the ticket_id returned in step 1
call_tool("add_comment", {"ticket_id": ticket_id, "body": "tried in incognito too"})

# Step 3: Close the same ticket
call_tool("close_ticket", {"ticket_id": ticket_id})
