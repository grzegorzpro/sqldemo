from flask import Flask

from config import DEBUG, HOST, PORT, DATABASE_URI
from models import db
from views import blog

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(blog)

db.init_app(app)


if __name__ == '__main__':
    app.run(HOST, PORT, debug=DEBUG)
