from datetime import datetime

from blog import app, db
from models import BlogPost

app.app_context().push()

db.create_all()

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
db.session.add(post1)
db.session.add(post2)
db.session.commit()

print('DB set up successfully!')
