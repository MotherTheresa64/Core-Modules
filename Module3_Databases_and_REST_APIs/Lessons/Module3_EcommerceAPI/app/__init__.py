from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize extensions globally (but not bound to app yet)
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    # Configure the MySQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:<YOUR-PASSWORD>@localhost/ecommerce_api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app context
    db.init_app(app)
    ma.init_app(app)

    # Import models AFTER initializing extensions
    from app.models import User, Product, Order, order_product

    # Create database tables
    with app.app_context():
        db.create_all()
        
    from app.routes.users import user_routes
    app.register_blueprint(user_routes)

    from app.routes.products import product_routes
    app.register_blueprint(product_routes)

    from app.routes.orders import order_routes
    app.register_blueprint(order_routes)

    return app
