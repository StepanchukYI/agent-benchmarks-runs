#!/bin/bash

# Initialize
current_page="p1"
total_items=0

# Loop through pages
while true; do
    page_file="pages/${current_page}.json"
    
    # Read the page
    page_content=$(cat "$page_file")
    
    # Count items in this page
    items_count=$(echo "$page_content" | jq '.items | length')
    total_items=$((total_items + items_count))
    
    # Check has_more flag
    has_more=$(echo "$page_content" | jq '.has_more')
    
    # Stop if no more pages
    if [ "$has_more" = "false" ]; then
        break
    fi
    
    # Get next cursor for next iteration
    current_page=$(echo "$page_content" | jq -r '.cursor')
done

echo "$total_items"
