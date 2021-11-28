from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.author import Author

@app.route('/')
def open():
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = Author.get_all()
    return render_template('authors.html', authors=authors)

@app.route('/create_author', methods=['POST'])
def create_author():
    data = {'name' : request.form['name']}
    Author.create(data)
    return redirect('/authors')

@app.route('/authors/<index_for_author_faves>')
def author_faves(index_for_author_faves):
    data = {'author_id' : index_for_author_faves }
    author = Author.get_one(data)[0]
    faves = Author.get_faves(data)
    options = Author.get_options(data)
    session['author_id'] = author['id']
    return render_template('author_faves.html', author=author, faves=faves, options=options)
