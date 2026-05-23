#!/usr/bin/env python3
"""Fetch all pages and count items"""

# Fixture implementation based on tools.json definition
def fetch_page(cursor=None):
    """Fetch one page of results. Returns {items, has_more, cursor}."""
    pages = {
        None: {"items": ["A", "B"], "has_more": True, "cursor": "p2"},
        "p2": {"items": ["C", "D"], "has_more": True, "cursor": "p3"},
        "p3": {"items": ["E"], "has_more": False, "cursor": None},
    }
    return pages.get(cursor, {})


# Fetch all pages
total_items = 0
current_cursor = None

# Call 1: Fetch page 1
page1 = fetch_page(current_cursor)
print(f"Call 1: fetch_page(cursor={current_cursor!r}) → items={page1['items']}, has_more={page1['has_more']}, cursor={page1['cursor']!r}")
total_items += len(page1["items"])
current_cursor = page1["cursor"]

# Call 2: Fetch page 2
page2 = fetch_page(current_cursor)
print(f"Call 2: fetch_page(cursor={current_cursor!r}) → items={page2['items']}, has_more={page2['has_more']}, cursor={page2['cursor']!r}")
total_items += len(page2["items"])
current_cursor = page2["cursor"]

# Call 3: Fetch page 3
page3 = fetch_page(current_cursor)
print(f"Call 3: fetch_page(cursor={current_cursor!r}) → items={page3['items']}, has_more={page3['has_more']}, cursor={page3['cursor']!r}")
total_items += len(page3["items"])

# Stop because has_more is False
print(f"\nhas_more=False: STOP\n")
print(total_items)
