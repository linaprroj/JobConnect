# init_db.py
from app_init import create_app, db
from models.user import User
from models.profile import Profile
from models.resume import Resume
from models.employer import Employer
from models.job_posting import JobPosting
from models.application import Application

app = create_app()

with app.app_context():
    db.create_all()
    print("Database and tables created.")
