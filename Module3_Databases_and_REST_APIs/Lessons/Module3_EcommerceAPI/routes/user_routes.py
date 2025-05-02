from flask import Blueprint, request, jsonify
from app import db
from models import User
from schemas import UserSchema

user_bp = Blueprint('user_bp', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = db.session.query(User).all()
    return users_schema.jsonify(users)

@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = db.session.get(User, id)
    return user_schema.jsonify(user)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = db.session.get(User, id)
    data = request.json
    user.name = data['name']
    user.address = data['address']
    user.email = data['email']
    db.session.commit()
    return user_schema.jsonify(user)

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = db.session.get(User, id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(message=f"User {id} deleted.")
