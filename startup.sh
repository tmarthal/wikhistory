#!/bin/bash
python3 manage.py migrate && gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 4
