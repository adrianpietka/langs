from os import environ
from application.api import app

if __name__ == '__main__':
    DEBUG = environ.get('SERVER_DEBUG', True)
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(debug=DEBUG, host=HOST, port=PORT)
