#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me

# Send a PUT request with a custom header to cause the server to respond with "You got me!"
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
