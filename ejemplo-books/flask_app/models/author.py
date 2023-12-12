from ..config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    #método de clase para guardar datos
    @classmethod
    def save(cls, data):
        query = 'insert into authors (name) values (%(name)s)'
        return connectToMySQL('libros').query_db(query, data)