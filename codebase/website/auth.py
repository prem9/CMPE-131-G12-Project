from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Email
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from website import app
from werkzeug.utils import secure_filename
from .forms import ResetPasswordForm, ComposeForm
import os
import uuid

auth = Blueprint('auth', __name__)

# Route for the Inbox Page
@auth.route("/", methods=['GET', 'POST'])
@login_required 
def inbox():
    
    # Query the Email model for all emails belonging to the current user
    #sent_emails = Email.query.filter_by(user_id=current_user.id).all()
    sent_emails = current_user.get_sent_emails()

    # Query the Email model for all emails where the current user is a recipient
    received_emails = current_user.get_received_emails()

    # Render the inbox page template by passing the emails list to the template
    return render_template("home.html", user=current_user, sent_emails=sent_emails, 
                           received_emails=received_emails)

# Route for the Login Page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve the email from the login form
        email = request.form.get('email') 
        # Retrieve the password from the login form
        password = request.form.get('password')

        # Query the User model for a user with the provided email
        user = User.query.filter_by(email=email).first()
        if user:
            # Check if the provided password matches the user's hashed password
            if check_password_hash(user.password, password):
                # Display a success message
                flash('Logged in successfully!', category='success')
                # Log in the user and remember their session
                login_user(user, remember=True)
                # Redirect the user to the inbox page after successful login
                return redirect(url_for('auth.inbox'))
            else:
                # Display an error message if the password is incorrect
                flash('Incorrect password, try again.', category='error')
        else:
            # Display an error message if the email does not exist
            flash('Email does not exist.', category='error')
    # Render the login page template
    return render_template("login.html", user=current_user)

# Route for the Logout Page
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Route for the Delete User Page
@auth.route('/delete-user', methods=['GET', 'POST'])
@login_required
def delete_user():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Query the User model for a user with the provided email
        user = User.query.filter_by(email=email).first()
        if user:
            # Check if the provided password matches the user's hashed password
            if check_password_hash(user.password, password):
                # Display a success message
                flash('User deleted successfully!', category='success')
                # Delete the user from the database
                db.session.delete(user)
                # Commit the changes to the database
                db.session.commit()
                # Redirect the user to the login page after deleting their account
                return redirect(url_for('auth.login'))
            else:
                # Display an error message if the password is incorrect
                flash('Incorrect password, try again.', category='error')
        else:
            # Display an error message if the email does not exist
            flash('Email does not exist.', category='error')
    # Render the delete user page template
    return render_template("delete_user.html", user=current_user)

# Route for the Compose email page
@auth.route('/compose', methods=['GET', 'POST'])
@login_required
def compose():
    form = ComposeForm()
    error_message = None

    if form.validate_on_submit():
        recipient_email = form.recipient.data
        subject = form.subject.data
        body = form.body.data

        recipient = User.query.filter_by(email=recipient_email).first() 

        if recipient:
            # Create a new email and save it in the database
            new_email = Email(
                user_id=current_user.id, 
                recipient=recipient, 
                subject=subject, 
                body=body)
            db.session.add(new_email)
            db.session.commit()

            flash('Email sent!', category='success')
            return redirect(url_for('auth.inbox'))
        else:
            error_message = 'Recipient email does not exist.'

    return render_template("compose.html", form=form, error_message=error_message)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Query the User model for a user with the provided email
        user = User.query.filter_by(email=email).first()

        # Checks for empty fields
        if not email:
            flash('Email cannot be empty.', category='error')
        elif not first_name:
            flash('First name cannot be empty.', category='error')
        elif not password1 or not password2:
            flash('Password cannot be empty.', category='error')

        # Checks for fields filled by the user
        if user:
            # Display an error message if an email already exists
            flash('Email already exists.', category='error') 
        elif len(email) < 4:
            # Display an error message if email length is less than 4 characters
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            # Display an error message if username is less than 2 characters
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            # Display an error message if passwords do not match
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            # Display an error message if password length is less than 7 characters
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Create a new User object with the provided email, username, and hashed password
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256')) 
            # Add the new user to the database
            db.session.add(new_user) 
            # Commit the changes to the database
            db.session.commit()
            # Log in the registered user
            login_user(new_user, remember=True)
            # Display a success message to indicate successful login
            flash('Account created!', category='success')
            # Redirect the user to the inbox page upon log in
            return redirect(url_for('auth.inbox'))
    # Renders the html template for the sign-up page upon redirecting to the sign up route
    return render_template("sign_up.html", user=current_user)

# Route for the Profile Page     
@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = User.query.filter_by(id=current_user.id).first()
    return render_template("profile.html", user=current_user)

# Route for the page to update user's profile
@auth.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
    # Retrieve the updated name from the form
    name = request.form['name']
    # Retrieve the updated bio from the form
    bio = request.form['bio']
    # Retrieve the current user from the database
    user = User.query.filter_by(id=current_user.id).first()
    # Update the user's name with the provided value
    user.name = name
    # Update the user's bio with the provided value
    user.bio = bio
    # Commit the changes to the database
    db.session.commit()
    
    return redirect('/profile')

# Route for updating the user's profile picture
@auth.route('/upload_profile_picture', methods=['POST'])
def upload_profile_picture():
    file = request.files['file'] # Retrieve the uploaded file from the request
    if not file: # If no file is uploaded, redirect to the profile page
        return redirect(url_for('auth.profile'))

    filename = str(uuid.uuid4()) + '.' + file.filename.split('.')[-1]  # Generate a unique filename for the uploaded file
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save the file to the specified upload folder

    user = User.query.filter_by(id=current_user.id).first() # Retrieve the current user from the database
    old_profile_picture = user.profile_picture # Get the filename of the user's current profile picture

    if old_profile_picture != 'default.jpg': # Remove the previous profile picture if it's not the default image
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], old_profile_picture))

    user.profile_picture = filename # Update the user's profile picture with the new filename
    db.session.commit() # Commit the changes to the database

    return redirect(url_for('auth.profile')) # Redirect the user to the profile page

# Route for refreshing the inbox page
@auth.route('/refresh', methods=['POST'])
def refresh():
    return redirect('/')

# Route for the reset password page
@auth.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm() # Create an instance of the ResetPasswordForm
    if form.validate_on_submit(): # If the form is submitted and passes validation
        user = User.query.filter_by(email=form.email.data).first() # Retrieve the user with the given email
        if user:
            user.password = generate_password_hash(form.password.data) # Update the user's password with the hashed value of the new password
            db.session.commit()  # Commit the changes to the database
            db.session.commit()
            flash('Your password has been reset successfully!', 'success') # Display a success message
            return redirect(url_for('auth.login')) # Redirect the user to the login page
        else:
            flash('Email does not exist', 'error') # Display an error message if the email doesn't exist
    return render_template('reset_password.html', form=form, user=current_user) # Render the reset_password.html template with the form and the current user