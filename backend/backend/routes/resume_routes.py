from flask import Blueprint, request, jsonify
from models.resume import Resume
from app_init import db

resume_bp = Blueprint('resume_bp', __name__)

@resume_bp.route('/resumes', methods=['GET'])
def get_resumes():
    resumes = Resume.query.all()
    return jsonify([resume.to_dict() for resume in resumes])

@resume_bp.route('/resumes/<int:id>', methods=['GET'])
def get_resume_by_id(id):
    resume = Resume.query.get_or_404(id)
    return jsonify(resume.to_dict())

@resume_bp.route('/resumes', methods=['POST'])
def create_resume():
    data = request.get_json()
    new_resume = Resume(
        profile_id=data['profile_id'],
        file_location=data['file_location']
    )
    db.session.add(new_resume)
    db.session.commit()
    return jsonify(new_resume.to_dict()), 201

@resume_bp.route('/resumes/<int:id>', methods=['PUT'])
def update_resume(id):
    resume = Resume.query.get_or_404(id)
    data = request.get_json()
    resume.profile_id = data.get('profile_id', resume.profile_id)
    resume.file_location = data.get('file_location', resume.file_location)
    db.session.commit()
    return jsonify(resume.to_dict())

@resume_bp.route('/resumes/<int:id>', methods=['DELETE'])
def delete_resume(id):
    resume = Resume.query.get_or_404(id)
    db.session.delete(resume)
    db.session.commit()
    return jsonify({'message': 'Resume deleted successfully'}), 204

# Helper method to convert Resume object to dictionary
def to_dict(self):
    return {
        'id': self.id,
        'profile_id': self.profile_id,
        'file_location': self.file_location
    }

# Add to_dict method to Resume model
Resume.to_dict = to_dict
