from ..config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []
    #crear después de la plantilla authors.html y el formulario que va dentro de authors.html 
    @classmethod
    def save(cls, data):
        query = 'insert into authors (name) values (%(name)s);'
        result = connectToMySQL('libros').query_db(query, data)
        return result
    @classmethod
    def get_all(cls):
        query = 'select * from authors;'
        authors = []
        results = connectToMySQL('libros').query_db(query)
        for i in results:
            authors.append(cls(i))
        return authors