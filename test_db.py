import os
from your_application import create_app, db
from your_application.models import User, JobSeeker, JobOfferer, JobPosting, Application, Interview, Message, Resume

app = create_app()
app.app_context().push()

# Test Create
new_user = User(email='testuser@example.com', password_hash='hashedpassword', user_type='job_seeker')
db.session.add(new_user)
db.session.commit()
print(f"User created with ID: {new_user.id}")

# Test Read
user = User.query.filter_by(email='testuser@example.com').first()
print(f"Read User: {user}")

# Test Update
user.email = 'updateduser@example.com'
db.session.commit()
print(f"Updated User Email: {user.email}")

# Test Delete
db.session.delete(user)
db.session.commit()
print("User deleted")

