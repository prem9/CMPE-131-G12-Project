from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, session
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)

@views.route('/list', methods=['GET', 'POST'])
@login_required
def list():
    if request.method == 'POST': 
        note = request.form.get('note')  # Retrieve value of form field submitted in HTTP POST request
        deadline_data = {}

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
           new_note = Note(data=note, user_id=current_user.id)  # Providing the schema for the note 
           db.session.add(new_note)                             # adding the note to the database 
           db.session.commit()

           for note_id, deadline in deadline_data.items():
                if deadline:
                    note = Note.query.filter_by(id=note_id).first()
                    note.deadline = deadline
                    db.session.commit()

           flash('Note added!', category='success')

        return redirect(url_for('views.list'))  # Used to ensure previous objectives added to the list will not be 
                                                # added again upon redirect
    return render_template("list.html", user=current_user)


@views.route('/delete-note', methods=['POST']) # Script used to delete a note from a list (Incorporated for Add Objective in list.html)
def delete_note():  
    note = json.loads(request.data) # This function expects a JSON from the Index.js file located in static folder
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:                            # Deletes note after verifying that the note belongs to the currently logged in user
        if note.user_id == current_user.id:  
            db.session.delete(note)
            db.session.commit()

    return jsonify({})