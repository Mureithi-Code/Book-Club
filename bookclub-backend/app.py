from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Club, Membership, Book, Discussion

# Initialize the Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookclub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# CRUD Routes for Users

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields'}), 400
    new_user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created!', 'user': {'id': new_user.id, 'name': new_user.name, 'email': new_user.email}}), 201

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

# Get a user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

# Update a user by ID
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.json
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)

    db.session.commit()
    return jsonify({'message': 'User updated!', 'user': {'id': user.id, 'name': user.name, 'email': user.email}})

# Delete a user by ID
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted!'})

# CRUD Routes for Clubs

# Create a new club
@app.route('/clubs', methods=['POST'])
def create_club():
    data = request.json
    if not data.get('name') or not data.get('description'):
        return jsonify({'message': 'Missing required fields'}), 400
    new_club = Club(name=data['name'], description=data['description'])
    db.session.add(new_club)
    db.session.commit()
    return jsonify({'message': 'Club created!', 'club': {'id': new_club.id, 'name': new_club.name, 'description': new_club.description}}), 201

# Get all clubs
@app.route('/clubs', methods=['GET'])
def get_clubs():
    clubs = Club.query.all()
    return jsonify([{'id': club.id, 'name': club.name, 'description': club.description} for club in clubs])

# Get a club by ID
@app.route('/clubs/<int:id>', methods=['GET'])
def get_club(id):
    club = Club.query.get(id)
    if not club:
        return jsonify({'message': 'Club not found'}), 404
    return jsonify({'id': club.id, 'name': club.name, 'description': club.description})

# Update a club by ID
@app.route('/clubs/<int:id>', methods=['PUT'])
def update_club(id):
    club = Club.query.get(id)
    if not club:
        return jsonify({'message': 'Club not found'}), 404

    data = request.json
    club.name = data.get('name', club.name)
    club.description = data.get('description', club.description)

    db.session.commit()
    return jsonify({'message': 'Club updated!', 'club': {'id': club.id, 'name': club.name, 'description': club.description}})

# Delete a club by ID
@app.route('/clubs/<int:id>', methods=['DELETE'])
def delete_club(id):
    club = Club.query.get(id)
    if not club:
        return jsonify({'message': 'Club not found'}), 404

    db.session.delete(club)
    db.session.commit()
    return jsonify({'message': 'Club deleted!'})

# CRUD Routes for Books

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    if not data.get('title') or not data.get('author') or not data.get('genre') or not data.get('user_id'):
        return jsonify({'message': 'Missing required fields'}), 400
    new_book = Book(title=data['title'], author=data['author'], genre=data['genre'], user_id=data['user_id'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created!', 'book': {'id': new_book.id, 'title': new_book.title}}), 201

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre} for book in books])

# Get a book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre})

# Update a book by ID
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.genre = data.get('genre', book.genre)

    db.session.commit()
    return jsonify({'message': 'Book updated!', 'book': {'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre}})

# Delete a book by ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted!'})

# CRUD Routes for Memberships

# Create a new membership
@app.route('/memberships', methods=['POST'])
def add_membership():
    data = request.json
    if not data.get('user_id') or not data.get('club_id') or not data.get('role'):
        return jsonify({'message': 'Missing required fields'}), 400
    membership = Membership(user_id=data['user_id'], club_id=data['club_id'], role=data['role'])
    db.session.add(membership)
    db.session.commit()
    return jsonify({'message': 'Membership created!', 'membership': {'user_id': membership.user_id, 'club_id': membership.club_id, 'role': membership.role}}), 201

# Get all memberships
@app.route('/memberships', methods=['GET'])
def get_memberships():
    memberships = Membership.query.all()
    result = []
    
    for membership in memberships:
        user = User.query.get(membership.user_id)  # Retrieve the user based on user_id in the membership
        if user:
            result.append({
                'user_id': membership.user_id,
                'club_id': membership.club_id,
                'role': membership.role,
                'member_name': user.name  # Add the member's name to the response
            })
    
    return jsonify(result)

# CRUD Routes for Discussions

# Create a new discussion
@app.route('/discussions', methods=['POST'])
def create_discussion():
    data = request.json
    if not data.get('content') or not data.get('book_id') or not data.get('club_id') or not data.get('date'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    new_discussion = Discussion(
        content=data['content'],
        date=data['date'],
        book_id=data['book_id'],
        club_id=data['club_id']
    )
    
    db.session.add(new_discussion)
    db.session.commit()
    
    return jsonify({
        'message': 'Discussion created!',
        'discussion': {
            'id': new_discussion.id,
            'content': new_discussion.content,
            'date': new_discussion.date,
            'book_id': new_discussion.book_id,
            'club_id': new_discussion.club_id
        }
    }), 201

# Get all discussions
@app.route('/discussions', methods=['GET'])
def get_all_discussions():
    discussions = Discussion.query.all()
    result = []
    for discussion in discussions:
        result.append({
            'id': discussion.id,
            'content': discussion.content,
            'date': discussion.date,
            'book_id': discussion.book_id,
            'club_id': discussion.club_id
        })
    return jsonify(result)

# Get a discussion by ID
@app.route('/discussions/<int:id>', methods=['GET'])
def get_discussion(id):
    discussion = Discussion.query.get(id)
    if not discussion:
        return jsonify({'message': 'Discussion not found'}), 404
    
    return jsonify({
        'id': discussion.id,
        'content': discussion.content,
        'date': discussion.date,
        'book_id': discussion.book_id,
        'club_id': discussion.club_id
    })

# Update a discussion by ID
@app.route('/discussions/<int:id>', methods=['PUT'])
def update_discussion(id):
    discussion = Discussion.query.get(id)
    if not discussion:
        return jsonify({'message': 'Discussion not found'}), 404

    data = request.json
    discussion.content = data.get('content', discussion.content)
    discussion.date = data.get('date', discussion.date)
    discussion.book_id = data.get('book_id', discussion.book_id)
    discussion.club_id = data.get('club_id', discussion.club_id)

    db.session.commit()
    return jsonify({
        'message': 'Discussion updated!',
        'discussion': {
            'id': discussion.id,
            'content': discussion.content,
            'date': discussion.date,
            'book_id': discussion.book_id,
            'club_id': discussion.club_id
        }
    })

# Delete a discussion by ID
@app.route('/discussions/<int:id>', methods=['DELETE'])
def delete_discussion(id):
    discussion = Discussion.query.get(id)
    if not discussion:
        return jsonify({'message': 'Discussion not found'}), 404

    db.session.delete(discussion)
    db.session.commit()
    return jsonify({'message': 'Discussion deleted!'})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
