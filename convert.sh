#!/bin/bash

# Check if no arguments provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Extract filename from arguments
filename="$1"
filepath="$2"
# Check if file exists
if [ ! -f "$filename" ]; then
    echo "Error: File '$filename' not found"
    exit 2
fi

# Add your commands here, for example:
echo "Processing file: $filename"

# Example command to convert XLSX to PDF using LibreOffice
libreoffice --headless --convert-to pdf --outdir "$filepath" "$filename"

echo "Conversion complete"

# Add more commands as needed


exit 0
