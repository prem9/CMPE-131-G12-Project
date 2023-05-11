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

class Message(db.Model): # Database used to store data relating to the chat feature
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Message {self.id}>'

