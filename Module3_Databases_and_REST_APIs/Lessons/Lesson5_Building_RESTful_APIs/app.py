from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from marshmallow import ValidationError
from typing import List, Optional
from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column


# Flask app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:<YOUR_PASSWORD>@localhost/flask_api_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Base model
class Base(DeclarativeBase):
    pass

# SQLAlchemy and Marshmallow init
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)

# Association table
user_pet = Table(
    "user_pet",
    Base.metadata,
    Column("user_id", ForeignKey("user_account.id"), primary_key=True),
    Column("pet_id", ForeignKey("pets.id"), primary_key=True)
)

# Models
class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = db.mapped_column(primary_key=True)
    name: Mapped[str] = db.mapped_column(String(30), nullable=False)
    email: Mapped[Optional[str]] = db.mapped_column(String(200))
    pets: Mapped[List["Pet"]] = relationship("Pet", secondary=user_pet, back_populates="owners")

class Pet(Base):
    __tablename__ = "pets"
    id: Mapped[int] = db.mapped_column(primary_key=True)
    name: Mapped[str] = db.mapped_column(String(200), nullable=False)
    animal: Mapped[str] = db.mapped_column(String(200), nullable=False)
    owners: Mapped[List["User"]] = relationship("User", secondary=user_pet, back_populates="pets")

# Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class PetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pet

user_schema = UserSchema()
users_schema = UserSchema(many=True)
pet_schema = PetSchema()
pets_schema = PetSchema(many=True)

# Routes go here...
