from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    def __init__(self, data):
        self.book_id = data['book_id']
        self.author_id = data['author_id']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM favorites;'
        results = connectToMySQL('books_schema').query_db(query)
        return results
    
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO favorites (author_id, book_id) VALUES ( %(author_id)s, %(book_id)s );'
        return connectToMySQL('books_schema').query_db(query, data)