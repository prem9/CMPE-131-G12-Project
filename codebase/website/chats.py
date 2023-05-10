from flask import  Blueprint, Flask, render_template, request, redirect, url_for, session, jsonify
from flask_login import login_required, current_user
from .models import Message, User
from . import db
import json
import sqlalchemy.sql 


#messages_BP = Blueprint('messages', __name__)
chats_BP = Blueprint('chats', __name__)

@chats_BP.route('/chathome', methods=['GET','POST'])
@login_required
def chat_home():
    pass
    return render_template('chathome.html', user=current_user)

# Define the messages route
@chats_BP.route('/chats', methods=['GET', 'POST'])
@login_required
def chats():

    user_id = current_user.id #session['user_id']
    user = User.query.filter_by(id=user_id).first()

    if request.method == 'POST':
        #db.select('user')
        #sql_str = text("select * from Message")
        #db.session.execute(sql_str).fetchall()a
        query = db.session.query(Message).filter_by(id=user_id)
        for cols in db.session.connection().execute(query):
            print(cols)

        receiver_username = request.form['receiver']
        receiver = User.query.filter_by(username=receiver_username).first()
        if not receiver:
            return render_template('chat.html', user=user, error='Invalid username')

        content = request.form['content']
        message = Message(sender_id=user_id, receiver_id=receiver.id, content=content)
        db.session.add(message)
        db.session.commit()
    else:
        return render_template('chat.html', user=user)

    messages_sent = Message.query.filter_by(sender_id=user_id).all()
    messages_received = Message.query.filter_by(receiver_id=user_id).all()
    return render_template('chat.html')
    #return render_template('messages.html', user=user, messages_sent=messages_sent, messages_received=messages_received)


