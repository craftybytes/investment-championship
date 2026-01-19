from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-this'  # Change this to a random secret key


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/information')
def information():
    return render_template('information.html')


@app.route('/rules')
def rules():
    return render_template('rules.html')


@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


# NEW: Registration page
@app.route('/register')
def register():
    return render_template('register.html')


# Handle registration form submission
@app.route('/submit-registration', methods=['POST'])
def submit_registration():
    try:
        # Get form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        university = request.form.get('university')
        field_of_study = request.form.get('field_of_study')
        year_of_study = request.form.get('year_of_study')
        team_name = request.form.get('team_name')
        experience = request.form.get('experience')
        motivation = request.form.get('motivation')
        sources = request.form.getlist('source')
        terms = request.form.get('terms')

        # For now, just print to console (for testing)
        print(f"New registration: {first_name} {last_name} - {email}")

        # Redirect back to register page with success message
        return render_template('register.html', success=True)

    except Exception as e:
        print(f"Error: {e}")
        return render_template('register.html', error="Something went wrong. Please try again.")


if __name__ == '__main__':
    app.run(debug=True, port=5001)