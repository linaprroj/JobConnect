# models/user.py
from app_init import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.Enum('Jobseeker', 'Employer', name='user_type'), nullable=False)
    contact_info = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'user_type': self.user_type,
            'contact_info': self.contact_info
        }

    def __repr__(self):
        return f'<User {self.name}>'
