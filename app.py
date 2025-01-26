from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rest.db'

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    genre = db.Column(db.String(250), nullable=False)

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


@app.route('/books', methods=['GET', 'POST'])
def add_get_books():
    if request.method == 'POST':
        title = request.json['title']
        author = request.json['author']
        genre = request.json['genre']

        new_book = Book(title=title, author=author, genre=genre)

        db.session.add(new_book)
        db.session.commit()

        return 'Book created', 201

    elif request.method == 'GET':
        book_list = Book.query.all()
        
        books = []

        for book in book_list:
            books.append({
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'genre': book.genre
        })    
            
        return jsonify({'books': books})    
    
    

db.init_app(app)