from flask_app import app
from flask import redirect, render_template, request
from ..models.author import Author
from ..models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    autores = Author.get_all()
    return render_template('authors.html', autores=autores)

@app.route('/create/author', methods=['POST'])
def create_author():
    data = {
        'name' : request.form['nombre']
    }
    Author.save(data)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_author(id):
    data = {
        'id':id
    }
    return render_template('show_author.html', autor=Author.get_author_by_id(data),
                                                libros_no_favoritos = Book.libros_no_favoritos(data))
@app.route('/join/book', methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['id_autor'],
        'book_id': request.form['id_libro']
    }
    print(data)
    Author.add_favorite(data)
    return redirect(f"/authors/{request.form['id_autor']}")