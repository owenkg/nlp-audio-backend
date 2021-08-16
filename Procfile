init: pip install -r requirements.txt 
upgrade: pip install -r requirements.txt && python3 manage.py db upgrade
create_defaults: python manage.py create_defaults
web: gunicorn wsgi:app
