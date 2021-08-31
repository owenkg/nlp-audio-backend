from server import create_app

test_app = create_app('testing')
prod_app = create_app('production')

if __name__ == '__main__':                            
    test_app.run()

# gunicorn --bind 0.0.0.0:5000 wsgi:app
# uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app