from server import create_app

#test_app = create_app('production')
app = create_app('testing')

if __name__ == '__main__':                            
    app.run()

# gunicorn --bind 0.0.0.0:5000 wsgi:app
# uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app