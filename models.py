from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.Text())
    category = db.Column(db.String(30), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
        }

    def __repr__(self):
        return "Product(id={}, name='{}'".format(self.id, self.name)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text())
    rating = db.Column(db.Integer, nullable=False)
    product = db.ForeignKey('product.id')

    def __repr__(self):
        return "Review(id={}, product='{}', rating={}".format(
            self.id, self.product, self.rating
        )

    def to_json(self):
        return {
            'id': self.id,
            'author': self.author,
            'content': self.content,
            'rating': self.rating,
            'product': self.product,
        }
