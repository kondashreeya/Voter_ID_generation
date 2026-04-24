python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn voter_id.wsgi:application --bind 0.0.0.0:$PORT 