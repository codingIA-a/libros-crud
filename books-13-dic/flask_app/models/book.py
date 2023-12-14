from ..config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data) :
        self.id = data['id']
        self.name = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
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