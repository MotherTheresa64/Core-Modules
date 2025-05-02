from flask import Blueprint, request, jsonify
from app import db
from models import Order, Product, User
from schemas import OrderSchema
from sqlalchemy import select
from datetime import datetime

order_bp = Blueprint('order_bp', __name__)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(user_id=data['user_id'], order_date=datetime.strptime(data['order_date'], "%Y-%m-%d"))
    db.session.add(new_order)
    db.session.commit()
    return order_schema.jsonify(new_order), 201

@order_bp.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
def add_product_to_order(order_id, product_id):
    order = db.session.get(Order, order_id)
    product = db.session.get(Product, product_id)
    if product not in order.products:
        order.products.append(product)
        db.session.commit()
    return jsonify(message="Product added to order.")

@order_bp.route('/orders/<int:order_id>/remove_product', methods=['DELETE'])
def remove_product_from_order(order_id):
    data = request.json
    product_id = data.get('product_id')
    order = db.session.get(Order, order_id)
    product = db.session.get(Product, product_id)
    if product in order.products:
        order.products.remove(product)
        db.session.commit()
    return jsonify(message="Product removed from order.")

@order_bp.route('/orders/user/<int:user_id>', methods=['GET'])
def get_orders_for_user(user_id):
    orders = db.session.query(Order).filter_by(user_id=user_id).all()
    return orders_schema.jsonify(orders)

@order_bp.route('/orders/<int:order_id>/products', methods=['GET'])
def get_products_for_order(order_id):
    order = db.session.get(Order, order_id)
    products = order.products
    from schemas import ProductSchema
    return ProductSchema(many=True).jsonify(products)
