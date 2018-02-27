from flask import Flask

from models import db
from rest_api import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqldemo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(api)

db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
