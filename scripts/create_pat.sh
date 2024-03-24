#!/bin/bash

# Check if exactly one argument (the file path) is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 path_to_json_file"
    exit 1
fi

# The first command line argument is the path to the JSON file
json_file_path="$1"

# Ensure the file exists
if [ ! -f "$json_file_path" ]; then
    echo "Error: File not found at $json_file_path"
    exit 1
fi

# Use curl to send a POST request with the JSON content
curl -X POST -H "Content-Type: application/json" -d @"$json_file_path" http://localhost:8000/service/createPatient | json
