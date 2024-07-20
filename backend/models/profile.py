from app_init import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    summary = db.Column(db.Text, nullable=True)
    experience = db.Column(db.Text, nullable=True)
    education = db.Column(db.Text, nullable=True)
    skills = db.Column(db.Text, nullable=True)
    certifications = db.Column(db.Text, nullable=True)
    interests = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'summary': self.summary,
            'experience': self.experience,
            'education': self.education,
            'skills': self.skills,
            'certifications': self.certifications,
            'interests': self.interests
        }
