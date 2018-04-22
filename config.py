import os

DEBUG = os.environ.get('DEBUG', 'False') in ['True', 'true']
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 8080))
