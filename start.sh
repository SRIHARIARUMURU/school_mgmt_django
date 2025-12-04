#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn scl_mgmt.wsgi:application --bind 0.0.0.0:$PORT