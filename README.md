# Book Club Management Application  

## Overview  
This project is a **Book Club Management Application** that allows users to manage book clubs, their members, books, and discussions. It is built with a **Flask API backend** and a **React.js frontend**, styled with CSS. The app provides full CRUD (Create, Read, Update, Delete) functionality for managing users, clubs, books, memberships, and discussions.  

---

## Features  
- **User Management**: Add, view, edit, and delete users.  
- **Club Management**: Create and manage book clubs.  
- **Book Management**: Add, view, update, and delete books.  
- **Membership Management**: Track users' roles and memberships in clubs.  
- **Discussions**: Facilitate and manage book discussions within clubs.  

---

## Tech Stack  

### Backend  
- **Flask**: A lightweight Python web framework.  
- **SQLAlchemy**: ORM for interacting with the database.  
- **Flask-Migrate**: Handles database migrations.  
- **SQLite**: Simple, file-based relational database.  
- **Flask-CORS**: Enables cross-origin requests.  

### Frontend  
- **React.js**: JavaScript library for building user interfaces.  
- **Axios**: For making API requests.  
- **CSS**: For styling the application.  

---

## Installation  

### Prerequisites  
- Python 3.x  
- Node.js and npm  

---

### Backend Setup  

1. Clone the repository:  
   ```bash
   git clone <repository_url>
   cd backend
   ```

2. Create a virtual environment and activate it:  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # For Linux/Mac  
   venv\Scripts\activate     # For Windows  
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```

4. Run migrations:  
   ```bash
   flask db upgrade  
   ```

5. Start the backend server:  
   ```bash
   flask run  
   ```
   The server will run on `http://localhost:5000`.  

---

### Frontend Setup  

1. Navigate to the frontend directory:  
   ```bash
   cd ../frontend
   ```

2. Install dependencies:  
   ```bash
   npm install  
   ```

3. Start the development server:  
   ```bash
   npm start  
   ```
   The frontend will run on `http://localhost:3000`.  

---

## Usage  

1. Open the application in your browser at `http://localhost:3000`.  
2. Use the navigation menu to access the sections for **Users**, **Clubs**, **Books**, **Memberships**, and **Discussions**.  
3. Perform CRUD operations using the provided forms and action buttons.  

---

## Project Structure  

### Backend  
```
backend/  
├── app.py               # Flask app and routes  
├── models.py            # Database models  
├── migrations/          # Database migration files  
├── requirements.txt     # Backend dependencies  
└── bookclub.db          # SQLite database (auto-generated)  
```  

### Frontend  
```
frontend/  
├── src/  
│   ├── components/      # React components  
│   ├── App.jsx          # Main React component  
│   ├── index.jsx        # Entry point  
│   └── App.css          # Styles  
├── package.json         # Frontend dependencies  
└── public/              # Static files  
```  

---

## API Endpoints  

The backend exposes RESTful APIs for each resource.  

### Users  
- `GET /users` - Get all users.  
- `POST /users` - Create a new user.  
- `GET /users/<id>` - Get a user by ID.  
- `PUT /users/<id>` - Update a user by ID.  
- `DELETE /users/<id>` - Delete a user by ID.  

### Clubs  
- `GET /clubs` - Get all clubs.  
- `POST /clubs` - Create a new club.  
- `GET /clubs/<id>` - Get a club by ID.  
- `PUT /clubs/<id>` - Update a club by ID.  
- `DELETE /clubs/<id>` - Delete a club by ID.  

### Books  
- `GET /books` - Get all books.  
- `POST /books` - Create a new book.  
- `GET /books/<id>` - Get a book by ID.  
- `PUT /books/<id>` - Update a book by ID.  
- `DELETE /books/<id>` - Delete a book by ID.  

### Memberships  
- `GET /memberships` - Get all memberships.  
- `POST /memberships` - Add a membership.  

### Discussions  
- `GET /discussions` - Get all discussions.  
- `POST /discussions` - Create a discussion.  
- `GET /discussions/<id>` - Get a discussion by ID.  
- `PUT /discussions/<id>` - Update a discussion by ID.  
- `DELETE /discussions/<id>` - Delete a discussion by ID.  

## Future Enhancements  
- Implement user authentication and authorization.  
- Add search and filter features.  
- Enhance UI/UX with advanced styling and animations.  
