from flask import Blueprint, request, jsonify
from app import db
from app.models import Product
from app.schemas import ProductSchema
from marshmallow import ValidationError

# Blueprint for product-related routes
product_routes = Blueprint('product_routes', __name__)

# Marshmallow schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# -------------------------------------
# CREATE PRODUCT
# -------------------------------------
@product_routes.route('/products', methods=['POST'])
def create_product():
    """Create a new product"""
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_product = Product(
        product_name=product_data['product_name'],
        price=product_data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product), 201

# -------------------------------------
# READ ALL PRODUCTS
# -------------------------------------
@product_routes.route('/products', methods=['GET'])
def get_products():
    """Get a list of all products"""
    products = Product.query.all()
    return products_schema.jsonify(products), 200

# -------------------------------------
# READ SINGLE PRODUCT
# -------------------------------------
@product_routes.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    """Get a specific product by ID"""
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product), 200

# -------------------------------------
# UPDATE PRODUCT
# -------------------------------------
@product_routes.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    """Update a product's details"""
    product = Product.query.get_or_404(id)

    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    product.product_name = product_data['product_name']
    product.price = product_data['price']
    db.session.commit()
    return product_schema.jsonify(product), 200

# -------------------------------------
# DELETE PRODUCT
# -------------------------------------
@product_routes.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    """Delete a product by ID"""
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': f'Deleted product {id}'}), 200
