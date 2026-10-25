# User Registration and Login API

## Project Overview

The User Registration and Login API is a backend application developed using Python, Flask, and SQLite. It provides API operations for user registration and login and demonstrates how a backend application processes user requests and interacts with a database.

This project was developed as part of the Web Development Technologies Lab practical assignment.

## Objectives

- Implement user registration functionality.
- Provide login-related API operations.
- Store and manage user records using SQLite.
- Handle HTTP requests and JSON responses.
- Test backend API operations using Python scripts.

## Technology Stack

- **Language:** Python
- **Backend Framework:** Flask
- **Database:** SQLite
- **Testing:** Python test script
- **Development Environment:** Visual Studio Code

## Features

- User registration and login API functionality.
- HTTP request and response handling.
- JSON-based communication.
- Database-backed user record management.
- API testing through a Python script.

## Project Structure

```text
user_login_backend1/
├── app.py
├── test_api.py
├── requirements.txt
└── README.md
```

*The file list may vary slightly depending on the final project files.*

## Installation and Setup

### 1. Install Python

Install Python and verify the installation:

```bash
python --version
```

### 2. Open the project folder

Open `user_login_backend1` in Visual Studio Code.

### 3. Install dependencies

If `requirements.txt` is present:

```bash
python -m pip install -r requirements.txt
```

Otherwise, install Flask:

```bash
python -m pip install flask
```

### 4. Start the server

```bash
python app.py
```

Use the host and port printed by the application.

### 5. Test the API

Open a second terminal and run:

```bash
python test_api.py
```

## API Endpoints

The application provides registration and login-related API operations. Refer to the route definitions in `app.py` and the requests in `test_api.py` for the exact HTTP methods, endpoint paths, and request fields.

## Testing

The API operations were tested using `test_api.py`. The project was observed returning the message:

```json
{
  "message": "User Registration and Login API is running"
}
```

The four API operations were reported to work during testing.

## Security Considerations

This is an educational project. A production authentication system should hash passwords securely, validate inputs, protect against common web vulnerabilities, and use appropriate session or token management. Never commit real passwords, secret keys, or personal user data to GitHub.

## Future Enhancements

- Add stronger input validation.
- Improve authentication and authorization.
- Add secure password hashing if not already implemented.
- Expand automated tests.
- Improve error handling and API documentation.

## Author

Developed as a Web Development Technologies Lab project.
