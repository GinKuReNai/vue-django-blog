#!/bin/sh

# Package依存関係の修正
echo "Fix Package Dependencies"
npm audit fix

# Collect static files
# echo "Build Vue Component"
# npm run build

# Start server
echo "Starting server"
npm run serve