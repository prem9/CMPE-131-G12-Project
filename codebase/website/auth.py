from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from faker import Faker
from website import app
from werkzeug.utils import secure_filename
from .forms import ResetPasswordForm
import os
import uuid

auth = Blueprint('auth', __name__)

fake = Faker()
def generate_emails(num_emails):
    emails = []
    for _ in range(num_emails):
        email = {
            'from': fake.email(),
            'subject': fake.sentence(),
            'body': fake.paragraph()
        }
        emails.append(email)
    return emails

@auth.route("/", methods=['GET', 'POST'])
@login_required
def inbox():
    num_emails = 10
    emails = generate_emails(num_emails)
    return render_template("home.html", emails=emails, user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.inbox'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/delete-user', methods=['GET', 'POST'])
@login_required
def delete_user():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('User deleted successfully!', category='success')
                db.session.delete(user)
                db.session.commit()
                return redirect(url_for('auth.login'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("delete_user.html", user=current_user)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if not email:
            flash('Email cannot be empty.', category='error')
        elif not first_name:
            flash('First name cannot be empty.', category='error')
        elif not password1 or not password2:
            flash('Password cannot be empty.', category='error')

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('auth.inbox'))

    return render_template("sign_up.html", user=current_user)
           
@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = User.query.filter_by(id=current_user.id).first()
    return render_template("profile.html", user=current_user)

@auth.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
    name = request.form['name']
    bio = request.form['bio']
    user = User.query.filter_by(id=current_user.id).first()
    user.name = name
    user.bio = bio
    db.session.commit()
    return redirect('/profile')

@auth.route('/upload_profile_picture', methods=['POST'])
def upload_profile_picture():
    file = request.files['file']
    if not file:
        return redirect(url_for('auth.profile'))

    filename = str(uuid.uuid4()) + '.' + file.filename.split('.')[-1]  # Generate a unique filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    user = User.query.filter_by(id=current_user.id).first()
    old_profile_picture = user.profile_picture

    if old_profile_picture != 'default.jpg':
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], old_profile_picture))

    user.profile_picture = filename
    db.session.commit()

    return redirect(url_for('auth.profile'))

@auth.route('/refresh', methods=['POST'])
def refresh():
    return redirect('/')

@auth.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            user.password = generate_password_hash(form.password.data)
            db.session.commit()
            flash('Your password has been reset successfully!', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Email does not exist', 'error')
    return render_template('reset_password.html', form=form, user=current_user)