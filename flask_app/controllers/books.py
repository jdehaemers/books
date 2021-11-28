from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.book import Book

@app.route('/books')
def books():
    books = Book.get_all()
    return render_template('books.html', books=books)

@app.route('/create_book', methods=['POST'])
def create_book():
    data = {
        'title' : request.form['title'],
        'num_of_pages' : request.form['num_of_pages']
        }
    Book.create(data)
    return redirect('/books')

@app.route('/books/<index_for_book_faves>')
def book_faves(index_for_book_faves):
    data = {'book_id' : index_for_book_faves }
    book = Book.get_one(data)[0]
    faves = Book.get_faves(data)
    options = Book.get_options(data)
    session['book_id'] = book['id']
    return render_template('book_faves.html', book=book, faves=faves, options=options)
