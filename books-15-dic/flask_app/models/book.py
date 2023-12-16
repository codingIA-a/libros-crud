from ..config.mysqlconnection import connectToMySQL
from flask_app.models import author
class Book:
    def __init__(self, data) :
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.autotes_favoritos = []
    @classmethod
    def save(cls, data):
        query = 'insert into books (title, num_of_pages) values (%(titulo)s,%(n_paginas)s);'
        results = connectToMySQL('libros').query_db(query,data)
        return results
    @classmethod
    def get_all(cls):
        query = 'select * from books;'
        libros = []
        resultados = connectToMySQL('libros').query_db(query)
        for i in resultados:
            libros.append(cls(i))
        return resultados
    @classmethod
    def libros_no_favoritos(cls, data):
        query = 'select * from books where books.id not in (select fk_book_id from favorites where fk_author_id = %(id)s);'
        results = connectToMySQL('libros').query_db(query, data)
        books = []
        for row in results:
            books.append(cls(row))
            print(books)
        return books
    @classmethod
    def get_by_id(cls, data):
        query = 'select * from books left join favorites on books.id = favorites.fk_book_id left join authors on authors.id = favorites.fk_author_id where books.id = %(id)s ;' 
        results = connectToMySQL('libros').query_db(query, data)
        book = cls(results[0])

        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                'id': row['authors.id'],
                'name' : row['name'],
                'created_at': row['authors.created_at'],
                'updated_at' : row['authors.updated_at']
            }
            book.autotes_favoritos.append(author.Author(data))
        return book