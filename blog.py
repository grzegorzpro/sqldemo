from flask import Flask

from config import DEBUG, HOST, PORT
from models import db
from views import blog

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqldemo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(blog)

db.init_app(app)


if __name__ == '__main__':
    app.run(HOST, PORT, debug=DEBUG)
