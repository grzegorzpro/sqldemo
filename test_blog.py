import os
import tempfile
from datetime import datetime

import pytest

import blog
from models import BlogPost


@pytest.fixture()
def app():
    db_fd, db_filename = tempfile.mkstemp()
    blog.app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_filename}'
    blog.app.testing = True
    with blog.app.app_context():
        blog.db.create_all()

    yield blog.app.test_client()

    os.close(db_fd)
    os.unlink(db_filename)


@pytest.fixture()
def app_with_posts(app):
    post1 = BlogPost(
        title='Welcome to PyLove!',
        content="Let's learn how to write web apps ;)",
        author='Hiromi Uehara',
        created=datetime(2018, 2, 7)
    )
    post2 = BlogPost(
        title='Example post',
        content='Example post content',
        author='Aaron Parks',
        created=datetime(2018, 2, 10)
    )
    with blog.app.app_context():
        blog.db.session.add(post1)
        blog.db.session.add(post2)
        blog.db.session.commit()
    return app


def test_posts_empty(app):
    resp = app.get('/posts')
    assert resp._status_code == 200
    assert b'No posts yet' in resp.data


def test_posts(app_with_posts):
    resp = app_with_posts.get('/posts')
    assert resp._status_code == 200
    assert b'Example post' in resp.data
