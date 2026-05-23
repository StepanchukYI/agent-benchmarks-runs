#!/usr/bin/env python3
"""
Simulates the ticket workflow:
  1. open_ticket(subject="cannot login")  → returns ticket_id
  2. add_comment(ticket_id=<id>, body="tried in incognito too")
  3. close_ticket(ticket_id=<same id>)
"""
import json, uuid

# ── simulated fixture (mimics what the real backend would do) ──
_TICKETS: dict = {}

def open_ticket(subject: str) -> str:
    ticket_id = str(uuid.uuid4())[:8]
    _TICKETS[ticket_id] = {"subject": subject, "comments": [], "status": "open"}
    print(json.dumps({"tool": "open_ticket", "args": {"subject": subject}, "result": ticket_id}))
    return ticket_id

def add_comment(ticket_id: str, body: str) -> None:
    assert ticket_id in _TICKETS, f"ticket {ticket_id} not found"
    _TICKETS[ticket_id]["comments"].append(body)
    print(json.dumps({"tool": "add_comment", "args": {"ticket_id": ticket_id, "body": body}, "result": "ok"}))

def close_ticket(ticket_id: str) -> None:
    assert ticket_id in _TICKETS, f"ticket {ticket_id} not found"
    _TICKETS[ticket_id]["status"] = "closed"
    print(json.dumps({"tool": "close_ticket", "args": {"ticket_id": ticket_id}, "result": "ok"}))

# ── agent logic: three calls in order, ticket_id chained ──
if __name__ == "__main__":
    # Step 1
    ticket_id = open_ticket(subject="cannot login")

    # Step 2 – uses the real ticket_id returned by step 1
    add_comment(ticket_id=ticket_id, body="tried in incognito too")

    # Step 3 – same ticket_id
    close_ticket(ticket_id=ticket_id)

    print("\n# Final state:", json.dumps(_TICKETS, indent=2))
