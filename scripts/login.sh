#!/bin/bash

# Check if exactly two arguments are given (for username and password)
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <username> <password>"
    exit 1
fi

# Assign command line arguments to variables
username="$1"
password="$2"

# Construct and execute the curl command with the provided username and password
curl "http://localhost:8000/service/doctor?username=$username&password=$password" | json
