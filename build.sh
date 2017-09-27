#!/bin/bash

# Moves all the static files into static/
python manage.py collectstatic --noinput
