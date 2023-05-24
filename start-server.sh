#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd rfp_app; python manage.py createsuperuser --no-input)
fi
(cd rfp_app; gunicorn KPM.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3) &
nginx -g "daemon off;"