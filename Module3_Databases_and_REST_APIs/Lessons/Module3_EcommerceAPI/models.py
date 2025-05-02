from app import db
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey, Table
from typing import List
from datetime import datetime

class Base(DeclarativeBase):
    pass

# Association Table
order_product = Table(
    "order_product",
    Base.metadata,
    db.Column("order_id", ForeignKey("orders.id"), primary_key=True),
    db.Column("product_id", ForeignKey("products.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(100), unique=True)

    orders: Mapped[List["Order"]] = relationship("Order", back_populates="user", cascade="all, delete")

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship("User", back_populates="orders")
    products: Mapped[List["Product"]] = relationship("Product", secondary=order_product, backref="orders")
