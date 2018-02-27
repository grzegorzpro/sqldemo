from app import app, db
from models import Product, Review

app.app_context().push()

db.create_all()

mouse = Product(
    name='Myszka komputerowa',
    category='Gryzonie',
    description='Opis'
)
db.session.add(mouse)
db.session.add(Review(
    product=mouse.id,
    author='Grzegorz',
    content='Tresc',
    rating=3
))
db.session.commit()
