#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
until python manage.py migrate; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

# Collect static files
echo "Collect static files"s
python manage.py collectstatic --noinput

# Start server
echo "Starting server"
python manage.py runserver
