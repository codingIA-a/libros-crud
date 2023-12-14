from flask_app import app
from flask import redirect, render_template, request
from ..models.author import Author

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