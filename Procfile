init: python manage.py db init && python manage.py db migrate && python manage.py db upgrade
upgrade: pip install -r requirements.txt && python manage.py db upgrade
create_defaults: python manage.py create_defaults
web: gunicorn wsgi:app