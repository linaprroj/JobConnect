from app_init import db

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    file_location = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'profile_id': self.profile_id,
            'file_location': self.file_location
        }
