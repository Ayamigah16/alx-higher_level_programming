#!/bin/bash
# This script sends a request to a URL and displays only the status code of the response

url="$1"

# Send the request and extract the status code
curl -s -o /dev/null -w "%{http_code}" "$url"
