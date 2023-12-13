from flask_app import app
from flask import redirect, render_template, request
from ..models.book import Book

@app.route('/books')
def books():
    return render_template('books.html')