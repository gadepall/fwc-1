#!/bin/bash

# Ensure a URL is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <GitHub_URL>"
    exit 1
fi

# Extract GitHub URL from command-line argument
github_url="$1"

# Extracting repository URL
REPO_URL=$(echo "$github_url" | awk -F'/tree' '{print $1}')

# Extracting branch name
BRANCH=$(echo "$github_url" | awk -F'/tree/' '{print $2}' | cut -d'/' -f1)

# Extracting directory path and name
DIRECTORY_PATH=$(echo "$github_url" | awk -F'/tree/' '{print $2}' | cut -d'/' -f2-)
DESTINATION_DIR_NAME=$(basename "$DIRECTORY_PATH")
FIRST_DIR_NAME=$(echo "$DIRECTORY_PATH" | cut -d'/' -f1)

# Destination directory to save the downloaded files
DESTINATION_DIR="$DESTINATION_DIR_NAME"

## Clone the repository and fetch only the specified directory
#
git clone --depth 1 --no-checkout -b "$BRANCH" "$REPO_URL" "$DESTINATION_DIR"
#
cd "$DESTINATION_DIR"
git config core.sparsecheckout true
echo "$DIRECTORY_PATH/*" > .git/info/sparse-checkout
git read-tree -mu HEAD
mv "$DIRECTORY_PATH"/* .
rm -rf "$FIRST_DIR_NAME" .git
