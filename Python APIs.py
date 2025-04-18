from flask import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "author": self.author,
            "publisher": self.publisher
        }
from flask import Flask, request, jsonify
from models.book_model import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        book_name=data.get('book_name'),
        author=data.get('author'),
        publisher=data.get('publisher')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201


@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict()), 200


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    book = Book.query.get_or_404(id)

    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)

    db.session.commit()
    return jsonify(book.to_dict()), 200


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)