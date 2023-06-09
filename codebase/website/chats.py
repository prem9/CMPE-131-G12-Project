from flask import  Blueprint, Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_login import login_required, current_user
from .models import Message, User
from . import db
import json
import sqlalchemy.sql


chats_BP = Blueprint('chats', __name__)

@chats_BP.route('/chat-view', methods=['GET','POST'])
@login_required
def view_message():
    print('Get - related data')
    if request.method == 'POST':
        #Retrives email value from the chat-view.html
        input_value = request.form['email-in']
        #Checks if a value was inputted in the form
        if not input_value:
            #gives a popup message in error category and then goes back to chat-view page
            flash('No email provided',category='error')
            return render_template('chat-view.html',user=current_user)
        user = User.query.filter_by(email=input_value).first()
        if not user:
            # checks if email is invalid it gives pop up message of invalid
            flash("Invalid email..",category='error')
            return render_template('chat-view.html',user=current_user)
        message = Message.query.filter_by(sender_id=current_user.id, receiver_id=user.id).first()
        if not message:
            flash('No chat history with this user',category='error')
            return render_template('chat-view.html',user=current_user)
        return render_template('chat-view.html',user=current_user, message=message.content)
    return render_template('chat-view.html', user=current_user)

@chats_BP.route('/delete_chat', methods=['GET','POST'])
@login_required
def delete_message():
    user_id = current_user.id
    if request.method == "POST":
        email2 = request.form['email']
        if not email2:
            flash('No email provided', category='error')
            return render_template('delete_chat.html',user=current_user)
        user2 = User.query.filter_by(email=email2).first()
        if not user2:
            flash('No user with this email',category='error')
            return render_template('delete_chat.html',user=current_user)
        chat1 = Message.query.filter_by(sender_id=user_id, receiver_id=user2.id).first()
        chat2 = Message.query.filter_by(receiver_id=user_id, sender_id=user2.id).first()
        if not chat1:
            return render_template("delete_chat.html", user=current_user, error="No chat for this email")
        db.session.delete(chat1)
        db.session.delete(chat2)
        db.session.commit()
    else:
        return render_template("delete_chat.html", user=current_user)

    return render_template('delete_chat.html', user=current_user)
@chats_BP.route('/chathome', methods=['GET','POST'])
@login_required
def chat_home():
    user_id = current_user.id
    if request.method == "GET":
        msgs = Message.query.filter_by(sender_id=user_id).all()
        html = ""
        for row in msgs:
            print(row)
            user1 = User.query.filter_by(id=row.receiver_id).first()
            html += str(user1.email)+str("\n")

    elif request.method == "POST":
        msgs = Message.query.filter_by(sender_id=user_id).all()

        for row in msgs:
            html += "<tr>"
            html += str(row)
            '''
            for value in row:
                html += "<td>{}</td>".format(value)
            html += "</tr>"
            '''
    return render_template('chathome.html', user=current_user, table=html)

@chats_BP.route('/chat', methods=['GET', 'POST'])
@login_required
def chats():

    user_id = current_user.id

    if request.method == 'POST':
        receiver_username = request.form['email']
        receiver = User.query.filter_by(email=receiver_username).first()
        if not receiver:
            flash("Invalid email address",category='error')
            return render_template('chat.html', user=current_user, error='Invalid username')
        msg1 = Message.query.filter_by(sender_id=user_id, receiver_id=receiver.id).first()
        content = request.form['message']
        if not msg1:
            content  =  current_user.first_name +": "+ content
            message1 = Message(sender_id=user_id, receiver_id=receiver.id, content=content)
            message2 = Message(sender_id=receiver.id, receiver_id=user_id, content=content)
            db.session.add(message1)
            db.session.add(message2)
            db.session.commit()
        else:
            msg2 = Message.query.filter_by(sender_id=receiver.id,receiver_id=user_id).first()
            msg1.content += '\n'+ current_user.first_name + ": "+ content
            msg2.content += '\n'+ current_user.first_name + ": "+ content 
            db.session.commit()
    else:
        return render_template('chat.html', user=current_user)

    messages_sent = Message.query.filter_by(sender_id=user_id).all()
    messages_received = Message.query.filter_by(receiver_id=user_id).all()
    return render_template('chat.html',user=current_user)

@chats_BP.route('/get-related-data',methods=['GET','POST'])
@login_required
def get_related_data():
    print('Get - related data')
    input_value = request.form.get('email-in')
    user = User.query.filter_by(email=input_value).first()
    if not user:
        return jsonify({'error': 'Invalid email'}) 
    message = Message.query.filter_by(sender_id = current_user.id, receiver_id = user.id).first()
    if not message:
        return jsonify({'error': 'No chat history with this user yet'})
    return jsonify({'message':message.content})
