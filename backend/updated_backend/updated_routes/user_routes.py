from flask import Blueprint, request, jsonify
from models.user import User
from app_init import db

user_bp = Blueprint('user_bp', __name__)

# Get all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Get user by ID
@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

# Create a new user
@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        email=data['email'],
        password=data['password'],
        user_type=data['user_type']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# Update user
@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.user_type = data.get('user_type', user.user_type)
    db.session.commit()
    return jsonify(user.to_dict())

# Delete user
@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 204

# Helper method to convert User object to dictionary
def to_dict(self):
    return {
        'id': self.id,
        'email': self.email,
        'user_type': self.user_type,
        'created_at': self.created_at.isoformat(),
        'updated_at': self.updated_at.isoformat(),
        'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None
    }

# Add to_dict method to User model
User.to_dict = to_dict

