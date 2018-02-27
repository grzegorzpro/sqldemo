from flask import Blueprint, jsonify, request

from models import Product, db

api = Blueprint('api', __name__)


@api.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = [product.to_json() for product in products]
    return jsonify(result)


@api.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_json())


@api.route('/products', methods=['POST'])
def add_product():
    data = request.json
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return jsonify({
        'created': True,
        'id': product.id
    })
