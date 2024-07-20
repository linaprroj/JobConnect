from app_init import db

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    company_desc = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(255), nullable=True)
    industry = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'company_name': self.company_name,
            'company_desc': self.company_desc,
            'location': self.location,
            'industry': self.industry
        }
