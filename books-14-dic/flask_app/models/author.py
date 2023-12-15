from ..config.mysqlconnection import connectToMySQL
from flask_app.models import book
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
    ##obtener id de autor, y datos de libros favoritos para añadirlos a la lista favorite_books
    @classmethod
    def get_author_by_id(cls, data):
        query = 'select * from authors left join favorites on authors.id = favorites.fk_author_id left join books on books.id = favorites.fk_book_id where authors.id = %(id)s;'
        results = connectToMySQL('libros').query_db(query,data)

        if results:
            author = cls(results[0])
            for row in results:
                if row['books.id'] == None:
                    break
                data = {
                    'id': row['books.id'],
                    'title': row['title'],
                    'num_of_pages' : row['num_of_pages'],
                    'created_at' : row['created_at'],
                    'updated_at' : row['updated_at']
                }
                author.favorite_books.append(book.Book(data))
            return author
        
