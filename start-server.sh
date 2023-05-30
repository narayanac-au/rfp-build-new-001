echo $DJANGO_SUPERUSER_PASSWORD
echo $DJANGO_SUPERUSER_USERNAME

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]
then
    # cd app;
    python manage.py createsuperuser --no-input;
fi
# cd /usr/src/app;
gunicorn KPM.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3;
nginx -g "daemon off";