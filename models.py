from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text())
    author = db.Column(db.String(30), nullable=False)
    created = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return "BlogPost(id={}, title='{}', author='{}'".format(self.id, self.title, self.author)
