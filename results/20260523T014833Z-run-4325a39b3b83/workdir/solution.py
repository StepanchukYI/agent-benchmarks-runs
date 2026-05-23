#!/usr/bin/env python3
"""
Simulates the two tool calls required by the task:
  1. create_order(customer_id="C-42", items=["SKU-1", "SKU-2"]) -> order_id
  2. send_confirmation_email(order_id=<returned order_id>)
"""

import json
import uuid

# ── Tool implementations ──────────────────────────────────────────

def create_order(customer_id: str, items: list) -> str:
    """Create a new order. Returns order_id."""
    order_id = f"ORD-{uuid.uuid4().hex[:8].upper()}"
    print(f"[create_order] customer_id={customer_id!r}, items={items!r}")
    print(f"[create_order] => order_id: {order_id}")
    return order_id

def send_confirmation_email(order_id: str) -> None:
    """Send a confirmation email for an existing order."""
    print(f"[send_confirmation_email] order_id={order_id!r}")
    print("[send_confirmation_email] => Confirmation email sent.")


# ── Execute the workflow ──────────────────────────────────────────

if __name__ == "__main__":
    # Step 1: create_order
    returned_order_id = create_order(
        customer_id="C-42",
        items=["SKU-1", "SKU-2"],
    )

    # Step 2: send_confirmation_email using the *exact* order_id from step 1
    send_confirmation_email(order_id=returned_order_id)
