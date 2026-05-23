"""
Demonstrates correct handling of user intent mapping to valid enum values.

User request: "Mark issue JIRA-42 as urgent."
Valid enum: low | medium | high | critical

Mapping: "urgent" -> "high" (or "critical" are both defensible)
Invalid: "urgent" is NOT in the enum and MUST NOT be sent.
"""

# Simulated tool call that would be issued:
TOOL_CALL = {
    "tool": "set_priority",
    "arguments": {
        "issue_id": "JIRA-42",
        "priority": "high"  # Mapped from "urgent" - valid enum value
    }
}

def demonstrate_correct_mapping():
    """Shows the single correct tool call."""
    valid_priorities = {"low", "medium", "high", "critical"}
    
    user_urgent_priority = "urgent"
    
    # Intent mapping: "urgent" maps to "high" (defensible choice)
    # Could also be "critical" - both are valid mappings
    mapped_priority = "high"
    
    assert mapped_priority in valid_priorities, "Must be valid enum"
    assert user_urgent_priority not in valid_priorities, "urgent is not valid"
    
    print("✅ Correct tool call issued:")
    print(f"   set_priority(issue_id='JIRA-42', priority='{mapped_priority}')")
    print(f"\n   'urgent' -> '{mapped_priority}' (valid enum member)")
    print(f"   Rejected values: 'urgent', 'medium', 'low', '' (none)")
    
    return TOOL_CALL

if __name__ == "__main__":
    demonstrate_correct_mapping()
