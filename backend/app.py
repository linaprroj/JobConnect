# app.py
from app_init import create_app
from routes.user_routes import user_bp
from routes.profile_routes import profile_bp
from routes.resume_routes import resume_bp
from routes.employer_routes import employer_bp
from routes.job_posting_routes import job_posting_bp
from routes.application_routes import application_bp

app = create_app()
app.register_blueprint(user_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(employer_bp)
app.register_blueprint(job_posting_bp)
app.register_blueprint(application_bp)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True, port=8000)
