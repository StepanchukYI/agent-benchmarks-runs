"""
Support ticket workflow: open → add_comment → close.
ticket_id flows from open_ticket return value — never fabricated.
"""
import uuid
import json


# ---------------------------------------------------------------------------
# Fixture tool implementations (match the schemas in tools.json)
# ---------------------------------------------------------------------------

def open_ticket(subject: str) -> str:
    """Open a support ticket. Returns ticket_id."""
    assert subject, "subject must be non-empty"
    ticket_id = str(uuid.uuid4())
    print(json.dumps({"call": "open_ticket", "args": {"subject": subject}, "returns": ticket_id}))
    return ticket_id


def add_comment(ticket_id: str, body: str) -> None:
    """Add a comment to an existing ticket."""
    assert ticket_id, "ticket_id must be non-empty"
    assert body, "body must be non-empty"
    print(json.dumps({"call": "add_comment", "args": {"ticket_id": ticket_id, "body": body}}))


def close_ticket(ticket_id: str) -> None:
    """Close an existing ticket."""
    assert ticket_id, "ticket_id must be non-empty"
    print(json.dumps({"call": "close_ticket", "args": {"ticket_id": ticket_id}}))


# ---------------------------------------------------------------------------
# Workflow — exactly three calls, in order, ticket_id threaded through
# ---------------------------------------------------------------------------

# Step 1: open the ticket; capture the returned ticket_id
ticket_id = open_ticket(subject="cannot login")

# Step 2: add comment using the id returned in step 1
add_comment(ticket_id=ticket_id, body="tried in incognito too")

# Step 3: close the ticket using the same id
close_ticket(ticket_id=ticket_id)
