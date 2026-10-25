
# User Registration and Login System

## Aim
To develop a backend API for user registration and login using Python Flask and SQLite.

## Technologies Used
- Python
- Flask
- SQLite
- REST API
- PBKDF2-HMAC-SHA256 password hashing

## Features
1. User registration
2. User login and password verification
3. Email uniqueness validation
4. Input validation
5. Secure password hashing with a random salt
6. Retrieve registered users without exposing passwords

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | / | Check server status |
| POST | /register | Register a new user |
| POST | /login | Authenticate a user |
| GET | /users | List registered users |

## Installation

Install dependencies:

    python -m pip install -r requirements.txt

## Execution

Run the application:

    python app.py

Server address:

    http://127.0.0.1:5000

## Testing
Use Postman to send JSON requests to the registration and login endpoints. Verify successful registration, duplicate email rejection, successful login and rejection of an incorrect password.

## Result
The project implements a basic user registration and login backend with SQLite database storage and salted password hashing.
