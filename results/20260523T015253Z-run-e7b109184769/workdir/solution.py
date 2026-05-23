"""
Solution: Three sequential tool calls for the support ticket workflow.

Step 1: open_ticket(subject="cannot login")
   → Returns a ticket_id (e.g. "TKT-123")

Step 2: add_comment(ticket_id=<returned_id>, body="tried in incognito too")
   → Uses the exact ticket_id returned by Step 1

Step 3: close_ticket(ticket_id=<same_returned_id>)
   → Uses the same ticket_id returned by Step 1

The ticket_id in steps 2 and 3 MUST be the value RETURNED by step 1.
"""

# Step 1: Open the support ticket
ticket_id = open_ticket(subject="cannot login")

# Step 2: Add a comment to the opened ticket using the returned ticket_id
add_comment(ticket_id=ticket_id, body="tried in incognito too")

# Step 3: Close the same ticket using the same ticket_id
close_ticket(ticket_id=ticket_id)
