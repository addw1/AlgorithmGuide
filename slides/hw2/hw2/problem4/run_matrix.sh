#!/bin/bash

# Check if the executable file exists
if [ -f "./matrix" ]; then
    echo "Running ./matrix ..."
    ./matrix
else
    echo "Error: ./matrix file does not exist or is not executable."
fi