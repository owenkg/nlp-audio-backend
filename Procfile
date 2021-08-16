init: pip install -r requirements.txt && source .deploy && python manage.py db init && python manage.py db migrate && python manage.py db upgrade
web: gunicorn wsgi:app
