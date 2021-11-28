from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM books;'
        results = connectToMySQL('books_schema').query_db(query)
        return results
    
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO books (title, num_of_pages) VALUES ( %(title)s, %(num_of_pages)s );'
        return connectToMySQL('books_schema').query_db(query, data)