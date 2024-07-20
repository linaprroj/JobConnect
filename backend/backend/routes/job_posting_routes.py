#routes/job_posting_routes.py
from flask import Blueprint, request, jsonify
from models.job_posting import JobPosting
from app_init import db
from datetime import datetime

job_posting_bp = Blueprint('job_posting_bp', __name__)

@job_posting_bp.route('/job_postings', methods=['GET'])
def get_job_postings():
    job_postings = JobPosting.query.all()
    return jsonify([job_posting.to_dict() for job_posting in job_postings])

@job_posting_bp.route('/job_postings/<int:id>', methods=['GET'])
def get_job_posting_by_id(id):
    job_posting = JobPosting.query.get_or_404(id)
    return jsonify(job_posting.to_dict())

@job_posting_bp.route('/job_postings', methods=['POST'])
def create_job_posting():
    data = request.get_json()
    new_job_posting = JobPosting(
        employer_id=data['employer_id'],
        job_title=data['job_title'],
        job_desc=data.get('job_desc'),
        requirements=data.get('requirements'),
        location=data.get('location'),
        date_posted=datetime.fromisoformat(data['date_posted']),
        salary_range=data.get('salary_range'),
        job_type=data.get('job_type'),
        application_deadline=datetime.fromisoformat(data['application_deadline']) if data.get('application_deadline') else None
    )
    db.session.add(new_job_posting)
    db.session.commit()
    return jsonify(new_job_posting.to_dict()), 201

@job_posting_bp.route('/job_postings/<int:id>', methods=['PUT'])
def update_job_posting(id):
    job_posting = JobPosting.query.get_or_404(id)
    data = request.get_json()
    job_posting.employer_id = data.get('employer_id', job_posting.employer_id)
    job_posting.job_title = data.get('job_title', job_posting.job_title)
    job_posting.job_desc = data.get('job_desc', job_posting.job_desc)
    job_posting.requirements = data.get('requirements', job_posting.requirements)
    job_posting.location = data.get('location', job_posting.location)
    job_posting.date_posted = datetime.fromisoformat(data['date_posted']) if data.get('date_posted') else job_posting.date_posted
    job_posting.salary_range = data.get('salary_range', job_posting.salary_range)
    job_posting.job_type = data.get('job_type', job_posting.job_type)
    job_posting.application_deadline = datetime.fromisoformat(data['application_deadline']) if data.get('application_deadline') else job_posting.application_deadline
    db.session.commit()
    return jsonify(job_posting.to_dict())

@job_posting_bp.route('/job_postings/<int:id>', methods=['DELETE'])
def delete_job_posting(id):
    job_posting = JobPosting.query.get_or_404(id)
    db.session.delete(job_posting)
    db.session.commit()
    return jsonify({'message': 'Job posting deleted successfully'}), 204

# Helper method to convert JobPosting object to dictionary
def to_dict(self):
    return {
        'id': self.id,
        'employer_id': self.employer_id,
        'job_title': self.job_title,
        'job_desc': self.job_desc,
        'requirements': self.requirements,
        'location': self.location,
        'date_posted': self.date_posted.isoformat(),
        'salary_range': self.salary_range,
        'job_type': self.job_type,
        'application_deadline': self.application_deadline.isoformat() if self.application_deadline else None
    }

# Add to_dict method to JobPosting model
JobPosting.to_dict = to_dict
