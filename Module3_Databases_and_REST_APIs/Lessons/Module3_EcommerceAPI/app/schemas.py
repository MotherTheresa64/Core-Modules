from app import ma
from app.models import User, Product, Order
from marshmallow import fields, validates, ValidationError

# 🧍 User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True  # allows user_id in OrderSchema

# 🛒 Product Schema
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_fk = True

    @validates('price')
    def validate_price(self, value):
        if value <= 0:
            raise ValidationError('Price must be greater than zero.')

# 📦 Order Schema
class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_fk = True

    # Include related product data when serializing orders
    products = fields.Nested(ProductSchema, many=True)
