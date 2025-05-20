from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from app.schemas import UserSchema
from marshmallow import ValidationError

# Blueprint for user-related routes
user_routes = Blueprint('user_routes', __name__)

# Marshmallow schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# -------------------------------------
# CREATE USER
# -------------------------------------
@user_routes.route('/users', methods=['POST'])
def create_user():
    """Create a new user with JSON input"""
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_user = User(
        name=user_data['name'],
        address=user_data.get('address'),
        email=user_data['email']
    )
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 201

# -------------------------------------
# READ ALL USERS
# -------------------------------------
@user_routes.route('/users', methods=['GET'])
def get_users():
    """Get a list of all users"""
    users = User.query.all()
    return users_schema.jsonify(users), 200

# -------------------------------------
# READ SINGLE USER
# -------------------------------------
@user_routes.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """Get a specific user by ID"""
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user), 200

# -------------------------------------
# UPDATE USER
# -------------------------------------
@user_routes.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """Update an existing user's info"""
    user = User.query.get_or_404(id)

    try:
        user_data = user_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user.name = user_data['name']
    user.address = user_data.get('address')
    user.email = user_data['email']
    db.session.commit()
    return user_schema.jsonify(user), 200

# -------------------------------------
# DELETE USER
# -------------------------------------
@user_routes.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """Delete a user by ID"""
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'Deleted user {id}'}), 200
