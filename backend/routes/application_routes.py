from flask import Blueprint, request, jsonify
from models.application import Application
from app_init import db
from datetime import datetime

application_bp = Blueprint('application_bp', __name__)

@application_bp.route('/applications', methods=['GET'])
def get_applications():
    applications = Application.query.all()
    return jsonify([application.to_dict() for application in applications])

@application_bp.route('/applications/<int:id>', methods=['GET'])
def get_application_by_id(id):
    application = Application.query.get_or_404(id)
    return jsonify(application.to_dict())

@application_bp.route('/applications', methods=['POST'])
def create_application():
    data = request.get_json()
    new_application = Application(
        job_id=data['job_id'],
        profile_id=data['profile_id'],
        date_applied=datetime.fromisoformat(data['date_applied']),
        status=data.get('status')
    )
    db.session.add(new_application)
    db.session.commit()
    return jsonify(new_application.to_dict()), 201

@application_bp.route('/applications/<int:id>', methods=['PUT'])
def update_application(id):
    application = Application.query.get_or_404(id)
    data = request.get_json()
    application.job_id = data.get('job_id', application.job_id)
    application.profile_id = data.get('profile_id', application.profile_id)
    application.date_applied = datetime.fromisoformat(data['date_applied']) if data.get('date_applied') else application.date_applied
    application.status = data.get('status', application.status)
    db.session.commit()
    return jsonify(application.to_dict())

@application_bp.route('/applications/<int:id>', methods=['DELETE'])
def delete_application(id):
    application = Application.query.get_or_404(id)
    db.session.delete(application)
    db.session.commit()
    return jsonify({'message': 'Application deleted successfully'}), 204

# Helper method to convert Application object to dictionary
def to_dict(self):
    return {
        'id': self.id,
        'job_id': self.job_id,
        'profile_id': self.profile_id,
        'date_applied': self.date_applied.isoformat(),
        'status': self.status
    }

# Add to_dict method to Application model
Application.to_dict = to_dict
