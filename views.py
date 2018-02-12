from datetime import datetime

from flask import render_template, redirect, Blueprint, request
from sqlalchemy import desc

from models import BlogPost, db

blog = Blueprint('blog', __name__)


@blog.route('/', methods=['GET'])
def redirect_to_posts():
    return redirect('/posts')


@blog.route('/posts', methods=['GET'])
def posts():
    posts = BlogPost.query.order_by(desc(BlogPost.created))
    return render_template('posts.html', posts=posts)


@blog.route('/post/<int:id>', methods=['GET'])
def post(id):
    post = BlogPost.query.get(id)
    return render_template('post.html', post=post)


@blog.route('/posts/create', methods=['POST'])
def create_post():
    new_post = BlogPost(
        title=request.form['title'],
        content=request.form['content'],
        author=request.form['author'],
        created=datetime.now(),
    )
    db.session.add(new_post)
    db.session.commit()
    return redirect('posts')
