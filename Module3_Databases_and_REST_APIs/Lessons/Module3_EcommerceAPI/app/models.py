from app import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

# Association table for Orders and Products (Many-to-Many)
order_product = Table(
    'order_product',
    db.Model.metadata,
    Column('order_id', Integer, ForeignKey('orders.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200))
    email = Column(String(120), unique=True, nullable=False)

    orders = relationship('Order', back_populates='user')

class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)

    orders = relationship('Order', secondary=order_product, back_populates='products')

class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='orders')
    products = relationship('Product', secondary=order_product, back_populates='orders')
