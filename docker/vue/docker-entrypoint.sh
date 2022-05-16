#!/bin/sh

# Collect static files
echo "Build Vue Component"
npm run build

# Start server
echo "Starting server"
npm run serve