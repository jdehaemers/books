from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM authors;'
        results = connectToMySQL('books_schema').query_db(query)
        return results
    
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO authors (name) VALUES ( %(name)s );'
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM authors WHERE id = %(author_id)s;'
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def get_faves(cls, data):
        query = 'SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(author_id)s;'
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def get_options(cls, data):
        query = 'SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id from favorites WHERE favorites.author_id = %(author_id)s);'
        return connectToMySQL('books_schema').query_db(query, data)
    
    