#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file and displays the body of the response

url="$1"
file="$2"

# Check if the file is a valid JSON
if jq empty < "$file" >/dev/null 2>&1; then
    # Send the POST request with the file contents in the body
    curl -sX POST -H "Content-Type: application/json" -d @"$file" "$url"
else
    echo "Not a valid JSON"
fi
