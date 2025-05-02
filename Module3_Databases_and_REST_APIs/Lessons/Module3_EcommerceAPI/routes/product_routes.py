from flask import Blueprint, request, jsonify
from app import db
from models import Product
from schemas import ProductSchema

product_bp = Blueprint('product_bp', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = db.session.query(Product).all()
    return products_schema.jsonify(products)

@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = db.session.get(Product, id)
    return product_schema.jsonify(product)

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return product_schema.jsonify(product), 201

@product_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = db.session.get(Product, id)
    data = request.json
    product.product_name = data['product_name']
    product.price = data['price']
    db.session.commit()
    return product_schema.jsonify(product)

@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = db.session.get(Product, id)
    db.session.delete(product)
    db.session.commit()
    return jsonify(message=f"Product {id} deleted.")
