from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Import and register blueprints
from routes.user_routes import user_bp
from routes.product_routes import product_bp
from routes.order_routes import order_bp

app.register_blueprint(user_bp)
app.register_blueprint(product_bp)
app.register_blueprint(order_bp)

with app.app_context():
    from models import Base
    Base.metadata.create_all(db.engine)
