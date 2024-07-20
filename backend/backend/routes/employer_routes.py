#routes/employer_routes.py
from flask import Blueprint, request, jsonify
from models.employer import Employer
from app_init import db

employer_bp = Blueprint('employer_bp', __name__)

@employer_bp.route('/employers', methods=['GET'])
def get_employers():
    employers = Employer.query.all()
    return jsonify([employer.to_dict() for employer in employers])

@employer_bp.route('/employers/<int:id>', methods=['GET'])
def get_employer_by_id(id):
    employer = Employer.query.get_or_404(id)
    return jsonify(employer.to_dict())

@employer_bp.route('/employers', methods=['POST'])
def create_employer():
    data = request.get_json()
    new_employer = Employer(
        user_id=data['user_id'],
        company_name=data['company_name'],
        company_desc=data.get('company_desc'),
        location=data.get('location'),
        industry=data.get('industry')
    )
    db.session.add(new_employer)
    db.session.commit()
    return jsonify(new_employer.to_dict()), 201

@employer_bp.route('/employers/<int:id>', methods=['PUT'])
def update_employer(id):
    employer = Employer.query.get_or_404(id)
    data = request.get_json()
    employer.user_id = data.get('user_id', employer.user_id)
    employer.company_name = data.get('company_name', employer.company_name)
    employer.company_desc = data.get('company_desc', employer.company_desc)
    employer.location = data.get('location', employer.location)
    employer.industry = data.get('industry', employer.industry)
    db.session.commit()
    return jsonify(employer.to_dict())

@employer_bp.route('/employers/<int:id>', methods=['DELETE'])
def delete_employer(id):
    employer = Employer.query.get_or_404(id)
    db.session.delete(employer)
    db.session.commit()
    return jsonify({'message': 'Employer deleted successfully'}), 204

# Helper method to convert Employer object to dictionary
def to_dict(self):
    return {
        'id': self.id,
        'user_id': self.user_id,
        'company_name': self.company_name,
        'company_desc': self.company_desc,
        'location': self.location,
        'industry': self.industry
    }

# Add to_dict method to Employer model
Employer.to_dict = to_dict
