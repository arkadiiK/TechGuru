#!/bin/sh

set -o errexit
set -o nounset

echo "Collect static..."
python manage.py collectstatic --noinput &&

echo "Make migrations..."
python manage.py makemigrations --noinput &&

echo "Migrate..."
python manage.py migrate --noinput &&

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000