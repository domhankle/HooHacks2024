#!/bin/bash

# Check if exactly three arguments are given
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <name> <username> <password>"
    exit 1
fi

# Assign command line arguments to variables
name="$1"
username="$2"
password="$3"

# Use variables in the curl command
curl -X POST -H "Content-Type: application/json" \
     -d "{\"name\": \"$name\", \"username\": \"$username\", \"password\": \"$password\"}" \
     http://localhost:8000/service/createDoctor | json
