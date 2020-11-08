#!/bin/bash

# Waiting for postgres
echo "Waiting for postgres..."
sleep 10

# Apply database migrations
echo "Apply database migrations"
until python manage.py migrate; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
