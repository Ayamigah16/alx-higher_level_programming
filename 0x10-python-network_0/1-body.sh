#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response (only for a 200 status code)
curl -sL "$1"
