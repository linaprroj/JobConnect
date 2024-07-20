from app_init import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job_posting.id'), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    date_applied = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'job_id': self.job_id,
            'profile_id': self.profile_id,
            'date_applied': self.date_applied,
            'status': self.status
        }
