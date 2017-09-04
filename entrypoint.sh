#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn adn3.wsgi \
    --name adn3 \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-file -
