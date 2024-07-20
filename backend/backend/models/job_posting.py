#models/job_posting.py
from app_init import db

class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)
    job_title = db.Column(db.String(255), nullable=False)
    job_desc = db.Column(db.Text, nullable=True)
    requirements = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(255), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False)
    salary_range = db.Column(db.String(50), nullable=True)
    job_type = db.Column(db.String(50), nullable=True)
    application_deadline = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'employer_id': self.employer_id,
            'job_title': self.job_title,
            'job_desc': self.job_desc,
            'requirements': self.requirements,
            'location': self.location,
            'date_posted': self.date_posted,
            'salary_range': self.salary_range,
            'job_type': self.job_type,
            'application_deadline': self.application_deadline
        }
