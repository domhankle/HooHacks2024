#!/bin/bash

# Read the list of JSON files from file_list.json
files=$(jq -r '.[]' testfiles/fileList.json)

# Loop through each JSON file
for file in $files; do
  # Run the curl command with the current JSON file as input
  curl -X POST -H "Content-Type: application/json" -d @testfiles/$file http:/localhost:8000/service/createPatient | json
done