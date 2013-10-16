#!/bin/bash
source venv/bin/activate
python manage.py syncdb --noinput
python manage.py migrate
python manage.py runserver