from flask import Blueprint, request, jsonify
from models.profile import Profile
from app_init import db

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/profiles', methods=['GET'])
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([profile.to_dict() for profile in profiles])

@profile_bp.route('/profiles/<int:id>', methods=['GET'])
def get_profile_by_id(id):
    profile = Profile.query.get_or_404(id)
    return jsonify(profile.to_dict())

@profile_bp.route('/profiles', methods=['POST'])
def create_profile():
    data = request.get_json()
    new_profile = Profile(
        user_id=data['user_id'],
        summary=data.get('summary'),
        experience=data.get('experience'),
        education=data.get('education'),
        skills=data.get('skills'),
        certifications=data.get('certifications'),
        interests=data.get('interests')
    )
    db.session.add(new_profile)
    db.session.commit()
    return jsonify(new_profile.to_dict()), 201

@profile_bp.route('/profiles/<int:id>', methods=['PUT'])
def update_profile(id):
    profile = Profile.query.get_or_404(id)
    data = request.get_json()
    profile.summary = data.get('summary', profile.summary)
    profile.experience = data.get('experience', profile.experience)
    profile.education = data.get('education', profile.education)
    profile.skills = data.get('skills', profile.skills)
    profile.certifications = data.get('certifications', profile.certifications)
    profile.interests = data.get('interests', profile.interests)
    db.session.commit()
    return jsonify(profile.to_dict())

@profile_bp.route('/profiles/<int:id>', methods=['DELETE'])
def delete_profile(id):
    profile = Profile.query.get_or_404(id)
    db.session.delete(profile)
    db.session.commit()
    return jsonify({'message': 'Profile deleted successfully'}), 204
