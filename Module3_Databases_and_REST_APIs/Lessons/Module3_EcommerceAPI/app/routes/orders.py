from flask import Blueprint, request, jsonify
from app import db
from app.models import Order, Product, User
from app.schemas import OrderSchema
from marshmallow import ValidationError
from datetime import datetime

# Blueprint for order-related routes
order_routes = Blueprint('order_routes', __name__)

# Marshmallow schema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# -------------------------------------
# CREATE ORDER
# -------------------------------------
@order_routes.route('/orders', methods=['POST'])
def create_order():
    """Create a new order for a user"""
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_order = Order(
        order_date=datetime.strptime(order_data['order_date'], "%Y-%m-%d"),
        user_id=order_data['user_id']
    )
    db.session.add(new_order)
    db.session.commit()
    return order_schema.jsonify(new_order), 201

# -------------------------------------
# ADD PRODUCT TO ORDER
# -------------------------------------
@order_routes.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
def add_product_to_order(order_id, product_id):
    """Associate a product with an order"""
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)

    if product in order.products:
        return jsonify({'message': 'Product already in order'}), 400

    order.products.append(product)
    db.session.commit()
    return jsonify({'message': f'Added product {product_id} to order {order_id}'}), 200

# -------------------------------------
# REMOVE PRODUCT FROM ORDER
# -------------------------------------
@order_routes.route('/orders/<int:order_id>/remove_product/<int:product_id>', methods=['DELETE'])
def remove_product_from_order(order_id, product_id):
    """Remove a product from an order"""
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)

    if product not in order.products:
        return jsonify({'message': 'Product not in order'}), 400

    order.products.remove(product)
    db.session.commit()
    return jsonify({'message': f'Removed product {product_id} from order {order_id}'}), 200

# -------------------------------------
# GET ALL ORDERS FOR A USER
# -------------------------------------
@order_routes.route('/orders/user/<int:user_id>', methods=['GET'])
def get_orders_for_user(user_id):
    """Get all orders placed by a user"""
    orders = Order.query.filter_by(user_id=user_id).all()
    return orders_schema.jsonify(orders), 200

# -------------------------------------
# GET ALL PRODUCTS IN AN ORDER
# -------------------------------------
@order_routes.route('/orders/<int:order_id>/products', methods=['GET'])
def get_products_in_order(order_id):
    """Get all products in a specific order"""
    order = Order.query.get_or_404(order_id)
    return jsonify([{
        'id': product.id,
        'product_name': product.product_name,
        'price': product.price
    } for product in order.products]), 200
