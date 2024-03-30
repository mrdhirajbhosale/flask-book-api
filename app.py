from flask import Flask, request, jsonify
from auth import token_required, generate_token
from model import db
from model import Book

app = Flask(__name__)
app.config['SECRET_KEY'] = 'seckey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    token = generate_token(username, password)
    if token:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/books', methods=['POST'])
@token_required
def create_book():
    data = request.get_json()
    new_book = Book(
        name=data['name'],
        description=data['description'],
        pages=data['pages'],
        author=data['author'],
        publisher=data['publisher']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully'}), 201

@app.route('/api/books', methods=['GET'])
@token_required
def get_books():
    author = request.args.get('author')
    publisher = request.args.get('publisher')

    query = Book.query
    if author:
        query = query.filter_by(author=author)
    if publisher:
        query = query.filter_by(publisher=publisher)

    books = query.all()
    return jsonify([{
        'name': book.name,
        'description': book.description,
        'pages': book.pages,
        'author': book.author,
        'publisher': book.publisher
    } for book in books])

@app.route('/api/books/<int:id>', methods=['DELETE'])
@token_required
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'}), 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
