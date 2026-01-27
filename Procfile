web: python manage.py collectstatic --noinput && python manage.py migrate && gunicorn ecommerce_site.wsgi --bind 0.0.0.0:$PORT


