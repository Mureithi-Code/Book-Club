from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Club, Membership, Book, Discussion

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookclub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# --- RESTful Routes for Users ---
@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

    elif request.method == 'POST':
        data = request.json
        if not all([data.get('name'), data.get('email'), data.get('password')]):
            return jsonify({'message': 'Missing required fields'}), 400

        new_user = User(name=data['name'], email=data['email'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created!', 'user': {'id': new_user.id, 'name': new_user.name, 'email': new_user.email}}), 201


@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if request.method == 'GET':
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

    elif request.method == 'PUT':
        data = request.json
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)
        db.session.commit()
        return jsonify({'message': 'User updated!', 'user': {'id': user.id, 'name': user.name, 'email': user.email}})

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted!'})

# --- RESTful Routes for Clubs ---
@app.route('/clubs', methods=['GET', 'POST'])
def handle_clubs():
    if request.method == 'GET':
        clubs = Club.query.all()
        return jsonify([{'id': club.id, 'name': club.name, 'description': club.description} for club in clubs])

    elif request.method == 'POST':
        data = request.json
        if not all([data.get('name'), data.get('description')]):
            return jsonify({'message': 'Missing required fields'}), 400

        new_club = Club(name=data['name'], description=data['description'])
        db.session.add(new_club)
        db.session.commit()
        return jsonify({'message': 'Club created!', 'club': {'id': new_club.id, 'name': new_club.name, 'description': new_club.description}}), 201


@app.route('/clubs/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_club(id):
    club = Club.query.get(id)
    if not club:
        return jsonify({'message': 'Club not found'}), 404

    if request.method == 'GET':
        return jsonify({'id': club.id, 'name': club.name, 'description': club.description})

    elif request.method == 'PUT':
        data = request.json
        club.name = data.get('name', club.name)
        club.description = data.get('description', club.description)
        db.session.commit()
        return jsonify({'message': 'Club updated!', 'club': {'id': club.id, 'name': club.name, 'description': club.description}})

    elif request.method == 'DELETE':
        db.session.delete(club)
        db.session.commit()
        return jsonify({'message': 'Club deleted!'})

# --- RESTful Routes for Books ---
@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        books = Book.query.all()
        return jsonify([{'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre} for book in books])

    elif request.method == 'POST':
        data = request.json
        if not all([data.get('title'), data.get('author'), data.get('genre'), data.get('user_id')]):
            return jsonify({'message': 'Missing required fields'}), 400

        new_book = Book(title=data['title'], author=data['author'], genre=data['genre'], user_id=data['user_id'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book created!', 'book': {'id': new_book.id, 'title': new_book.title}}), 201


@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    if request.method == 'GET':
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre})

    elif request.method == 'PUT':
        data = request.json
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.genre = data.get('genre', book.genre)
        db.session.commit()
        return jsonify({'message': 'Book updated!', 'book': {'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre}})

    elif request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted!'})

# --- RESTful Routes for Memberships ---
@app.route('/memberships', methods=['GET', 'POST'])
def handle_memberships():
    if request.method == 'GET':
        memberships = Membership.query.all()
        result = []
        for membership in memberships:
            user = User.query.get(membership.user_id)
            result.append({
                'user_id': membership.user_id,
                'club_id': membership.club_id,
                'role': membership.role,
                'user_name': user.name if user else None
            })
        return jsonify(result)

    elif request.method == 'POST':
        data = request.json
        if not all([data.get('user_id'), data.get('club_id'), data.get('role')]):
            return jsonify({'message': 'Missing required fields'}), 400

        membership = Membership(user_id=data['user_id'], club_id=data['club_id'], role=data['role'])
        db.session.add(membership)
        db.session.commit()
        return jsonify({'message': 'Membership created!', 'membership': {'user_id': membership.user_id, 'club_id': membership.club_id, 'role': membership.role}}), 201

# --- RESTful Routes for Discussions ---
@app.route('/discussions', methods=['GET', 'POST'])
def handle_discussions():
    if request.method == 'GET':
        discussions = Discussion.query.all()
        return jsonify([{
            'id': discussion.id,
            'content': discussion.content,
            'date': discussion.date,
            'book_id': discussion.book_id,
            'club_id': discussion.club_id
        } for discussion in discussions])

    elif request.method == 'POST':
        data = request.json
        if not all([data.get('content'), data.get('book_id'), data.get('club_id'), data.get('date')]):
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

@app.route('/discussions/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_discussion(id):
    discussion = Discussion.query.get(id)
    if not discussion:
        return jsonify({'message': 'Discussion not found'}), 404

    if request.method == 'GET':
        return jsonify({
            'id': discussion.id,
            'content': discussion.content,
            'date': discussion.date,
            'book_id': discussion.book_id,
            'club_id': discussion.club_id
        })

    elif request.method == 'PUT':
        data = request.json
        discussion.content = data.get('content', discussion.content)
        discussion.date = data.get('date', discussion.date)
        discussion.book_id = data.get('book_id', discussion.book_id)
        discussion.club_id = data.get('club_id', discussion.club_id)
        db.session.commit()
        return jsonify({'message': 'Discussion updated!', 'discussion': {
            'id': discussion.id,
            'content': discussion.content,
            'date': discussion.date,
            'book_id': discussion.book_id,
            'club_id': discussion.club_id
        }})

    elif request.method == 'DELETE':
        db.session.delete(discussion)
        db.session.commit()
        return jsonify({'message': 'Discussion deleted!'})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
