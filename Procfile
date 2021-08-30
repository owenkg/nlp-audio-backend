init: pip install -r requirements.txt && python manage.py db migrate && python manage.py db upgrade
upgrade: pip install -r requirements.txt && python manage.py db upgrade
create_defaults: python manage.py create_defaults
web: source .env && gunicorn wsgi:app