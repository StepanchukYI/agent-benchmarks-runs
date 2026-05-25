#!/bin/bash

total=0
current_file="pages/p1.json"

while true; do
  # Read the current page
  data=$(cat "$current_file")
  
  # Extract items count
  items_count=$(echo "$data" | jq '.items | length')
  total=$((total + items_count))
  
  # Check if there are more pages
  has_more=$(echo "$data" | jq '.has_more')
  
  if [ "$has_more" = "false" ]; then
    break
  fi
  
  # Get the next cursor
  cursor=$(echo "$data" | jq -r '.cursor')
  current_file="pages/${cursor}.json"
done

echo "$total"
