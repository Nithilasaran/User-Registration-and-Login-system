from flask import Flask, request, jsonify
import sqlite3
import hashlib
import hmac
import os
import re

app = Flask(__name__)

DATABASE = os.path.join(os.path.dirname(__file__), "database.db")


# ---------- DATABASE ----------

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)


# ---------- PASSWORD HASHING ----------

def hash_password(password):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        os.urandom(16),
        600000
    )


def verify_password(password, salt, stored_hash):
    calculated = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600000
    )
    return hmac.compare_digest(calculated, stored_hash)


# ---------- HOME ----------

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "User Registration and Login API is running"
    })


# ---------- REGISTER ----------

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"message": "Send valid JSON data"}), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not all(isinstance(x, str) for x in (name, email, password)):
        return jsonify({"message": "All fields are required"}), 400

    name = name.strip()
    email = email.strip().lower()

    if not name or len(name) > 100:
        return jsonify({"message": "Enter a valid name"}), 400

    if len(email) > 254 or not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+", email
    ):
        return jsonify({"message": "Enter a valid email"}), 400

    if len(password) < 8 or len(password) > 128:
        return jsonify({
            "message": "Password must be 8 to 128 characters"
        }), 400

    salt = os.urandom(16)
    password_hash = hash_password(password)

    # Store salt and hash together as hexadecimal text.
    stored_hash = salt.hex() + ":" + password_hash.hex()

    try:
        with get_db() as conn:
            conn.execute(
                """INSERT INTO users (name, email, password_hash)
                   VALUES (?, ?, ?)""",
                (name, email, stored_hash)
            )

        return jsonify({"message": "Registration successful"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"message": "Email already registered"}), 409


# ---------- LOGIN ----------

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"message": "Send valid JSON data"}), 400

    email = data.get("email")
    password = data.get("password")

    if not isinstance(email, str) or not isinstance(password, str):
        return jsonify({
            "message": "Email and password are required"
        }), 400

    email = email.strip().lower()

    with get_db() as conn:
        user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

    if user is None:
        return jsonify({"message": "Invalid email or password"}), 401

    try:
        salt_hex, hash_hex = user["password_hash"].split(":")
        valid = verify_password(
            password,
            bytes.fromhex(salt_hex),
            bytes.fromhex(hash_hex)
        )
    except (ValueError, TypeError):
        valid = False

    if not valid:
        return jsonify({"message": "Invalid email or password"}), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        }
    }), 200


# ---------- LIST USERS (NO PASSWORDS) ----------

@app.route("/users", methods=["GET"])
def get_users():
    with get_db() as conn:
        users = conn.execute(
            "SELECT id, name, email FROM users ORDER BY id"
        ).fetchall()

    return jsonify([dict(user) for user in users])


# ---------- START SERVER ----------

create_table()

if __name__ == "__main__":
    app.run(debug=True)
