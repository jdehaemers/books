from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.favorite import Favorite

@app.route('/authors/add_fave', methods=['POST'])
def add_author_fave():
    data = {
        'author_id' : session['author_id'],
        'book_id' : request.form['favorite']
    }
    Favorite.create(data)
    return redirect('/authors/' + str(session['author_id']))

@app.route('/books/add_fave', methods=['POST'])
def add_book_fave():
    data = {
        'book_id' : session['book_id'],
        'author_id' : request.form['favorite']
    }
    Favorite.create(data)
    return redirect('/books/' + str(session['book_id']))