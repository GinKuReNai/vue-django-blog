#!/bin/sh

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --noinput

# Apply database migrations
# echo "Apply database migrations"
# python3 manage.py makemigrations

# Apply database migrate
echo "Apply database migrate"
python3 manage.py migrate

# Start server
echo "Starting server"
uwsgi --socket :8001 --module app.wsgi --py-autoreload 1 --logto /tmp/uwsgi.log
