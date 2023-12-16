from flask_app import app
from flask import redirect, render_template, request
from ..models.book import Book
from ..models.author import Author
@app.route('/books')
def books():
    libros = Book.get_all()
    return render_template('books.html', libros=libros)

@app.route('/create/book', methods=['POST'])
def create_book():
    data = {
        'titulo' : request.form['titulo'],
        'n_paginas' : request.form['n-paginas']
    }
    print(data)
    Book.save(data)
    return redirect('/books')
@app.route('/book/<int:id>')
def show_book(id):
    data = {
        'id':id
    }
    return render_template('show_books.html', book=Book.get_by_id(data), 
                           unfavorited_authors=Author.unfavorited_authors(data))

@app.route('/join/author' , methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")