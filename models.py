from datetime import datetime

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


if __name__ == '__main__':
    from app import app

    app.app_context().push()
    db.init_app(app)

    db.create_all()

    post1 = BlogPost(
        title='Welcome to PyLove!',
        content='Let\'s learn how to write web apps ;)',
        author='Hiromi Uehara',
        created=datetime(2018, 2, 7)
    )
    post2 = BlogPost(
        title='Example post',
        content='Example post content',
        author='Aaron Parks',
        created=datetime(2018, 2, 10)
    )
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
