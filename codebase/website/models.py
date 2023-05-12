from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model): # Database used to store data relating to creating a list on the website
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin): # Database used to store data relating to users on the website
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    bio = db.Column(db.String(1000))
    first_name = db.Column(db.String(150))
    profile_picture = db.Column(db.String(150), default='default.jpg')
    notes = db.relationship('Note')

    # One-to-many relationship between User & Email
    sent_emails = db.relationship('Email', foreign_keys='Email.user_id', backref='user_sent_emails', lazy=True)
    received_emails = db.relationship('Email', foreign_keys='Email.recipient_id', backref='emailed_recipient', lazy=True)
    
    #db.relationship('Email', foreign_keys='Email.recipient_id', backref='recipient')

class Message(db.Model): # Database used to store data relating to the chat feature
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Message {self.id}>'

class Email(db.Model): # Database used to store data relating to the email feature
    # Unique identifier for each email
    id = db.Column(db.Integer, primary_key=True)

    # User who sent/received the email
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Email content
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(10000), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())

    # Many-to-one relationship between Email & User
    sender = db.relationship('User', foreign_keys=[user_id], backref='sent_emails')
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='received_emails')

    # For debugging/Logging purposes to output the email object
    def __repr__(self):
        return f'<Email {self.id}>'