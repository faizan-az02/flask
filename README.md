Learning Flask and Posting whatever I do, here.

# Flask Customer Management App

A Flask web application for managing customers, their orders, and addresses. This project demonstrates user registration, login, and viewing all users with their associated orders and addresses. Data is stored in a MySQL database using SQLAlchemy ORM.

## Features
- User registration with password hashing
- User login and session management
- Add orders and addresses during registration
- View all users, their orders, and addresses in a styled table
- Clean, modern UI with custom CSS

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/faizan-az02/flask.git
   cd flask
   ```
   
2. **Install dependencies:**
   Create a `requirements.txt` file with the following content:
   ```
   Flask
   Flask-SQLAlchemy
   Werkzeug
   mysqlclient
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the database:**
   - Make sure you have MySQL installed and running.
   - Create a database named `test` (or change the name in `app.py`).
   - Place your MySQL root password in a file and update the path in `app.py`.

4. **Initialize the database:**
   Open a Python shell and run:
   ```python
   from app import db
   db.create_all(app=app)
   ```

6. **Run the application:**
   ```bash
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Usage
- Register a new user with an order and address.
- Log in with your credentials.
- After login, view all users, their orders, and addresses.

## License
This project is for learning purposes. Feel free to use and modify it.
