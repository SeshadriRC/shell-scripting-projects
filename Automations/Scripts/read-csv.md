#!/bin/bash

CSV_FILE="names.csv"

# Read the CSV file and skip the header
tail -n +2 "$CSV_FILE" |
while IFS=',' read -r base cluster ns; do

    # Print individual column values
    echo "Base: $base"
    echo "Cluster: $cluster"
    echo "Namespace: $ns"
    echo "----------------------"

done
