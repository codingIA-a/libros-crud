from flask_app import app
from flask import redirect, render_template, request
from ..models.book import Book

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