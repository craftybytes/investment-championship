from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

# Get the absolute path to the app directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')

# Create files directory if it doesn't exist
if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)


@app.route('/register')
def register():
    success = request.args.get('success')
    error = request.args.get('error')
    return render_template('register.html', success=success, error=error)


@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    try:
        # Get form data
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        university = request.form.get('university', '').strip()
        field_of_study = request.form.get('field_of_study', '').strip()
        year_of_study = request.form.get('year_of_study', '').strip()
        team_name = request.form.get('team_name', '').strip()
        experience = request.form.get('experience', '').strip()
        motivation = request.form.get('motivation', '').strip()

        # Get checkbox values
        sources = []
        if request.form.get('source_social'):
            sources.append('Social Media')
        if request.form.get('source_university'):
            sources.append('University')
        if request.form.get('source_friend'):
            sources.append('Friend/Colleague')
        if request.form.get('source_other'):
            sources.append('Other')

        sources_str = ', '.join(sources) if sources else 'Not specified'

        # Validate required fields
        if not all([first_name, last_name, email, university, field_of_study,
                    year_of_study, experience, motivation]):
            return redirect(url_for('register', error='Please fill in all required fields'))

        # Use absolute path for the registration file
        registration_file = os.path.join(FILES_DIR, 'registrations.txt')

        # Debug: Print the path being used
        print(f"Attempting to save to: {registration_file}")
        print(f"Directory exists: {os.path.exists(FILES_DIR)}")
        print(f"Directory writable: {os.access(FILES_DIR, os.W_OK)}")

        # Create file with header if it doesn't exist
        if not os.path.isfile(registration_file):
            with open(registration_file, 'w', encoding='utf-8') as f:
                f.write("SNIC 2026 REGISTRATIONS\n")
                f.write("=" * 80 + "\n\n")

        # Append registration data
        with open(registration_file, 'a', encoding='utf-8') as f:
            f.write(f"\n{'-' * 80}\n")
            f.write(f"Registration Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'-' * 80}\n")
            f.write(f"Name: {first_name} {last_name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Phone: {phone if phone else 'Not provided'}\n")
            f.write(f"University: {university}\n")
            f.write(f"Field of Study: {field_of_study}\n")
            f.write(f"Year of Study: {year_of_study}\n")
            f.write(f"Team Name: {team_name if team_name else 'Individual participant'}\n")
            f.write(f"Experience Level: {experience}\n")
            f.write(f"How Did You Hear: {sources_str}\n")
            f.write(f"\nMotivation:\n{motivation}\n")
            f.write(f"{'-' * 80}\n\n")

        print(f"Registration saved successfully for {email}")
        return redirect(url_for('register', success='true'))

    except Exception as e:
        print(f"Error processing registration: {e}")
        import traceback
        traceback.print_exc()
        return redirect(url_for('register', error='Something went wrong. Please try again.'))


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


if __name__ == '__main__':
    app.run(debug=True)