# app.py
from sqlalchemy import text
from flask import Flask, jsonify  # Ensure you import jsonify
from app_init import create_app, db
from updated_routes.user_routes import user_bp
from updated_routes.resume_routes import resume_bp
from updated_routes.job_offerer_routes import job_offerer_bp
from updated_routes.job_posting_routes import job_posting_bp
from updated_routes.job_seeker_routes import job_seeker_bp
from updated_routes.interview_routes import interview_bp
from updated_routes.application_routes import application_bp
import os

print("Starting the Flask application...")

app = create_app()
app.register_blueprint(user_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(job_offerer_bp)
app.register_blueprint(job_posting_bp)
app.register_blueprint(job_seeker_bp)
app.register_blueprint(interview_bp)
app.register_blueprint(application_bp)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test_db')
def test_db():
    try:
        result = db.session.execute(text('SELECT 1'))
        return 'Database connection successful: {}'.format(result.fetchone())
    except Exception as e:
        return str(e)

@app.route('/env')
def show_env():
    return jsonify({
        'FLASK_APP': os.getenv('FLASK_APP'),
        'FLASK_ENV': os.getenv('FLASK_ENV'),
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'SECRET_KEY': os.getenv('SECRET_KEY')
    })

@app.route('/config')
def show_config():
    return jsonify(dict(app.config))

# Print out the registered routes for debugging purposes
print("Routes:")
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint}: {rule}")
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)

