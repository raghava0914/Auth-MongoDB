import re
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
from models import users

# Email & Password Validation Regex
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PASSWORD_REGEX = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'  # Minimum 8 chars, 1 letter, 1 number

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email)

def is_valid_password(password):
    return re.match(PASSWORD_REGEX, password)

# Signup Function
def signup_user(email, password):
    if not is_valid_email(email) or not is_valid_password(password):
        return "Invalid email or password format"

    if users.find_one({"email": email}):
        return "Email already exists"

    hashed_pw = generate_password_hash(password)
    users.insert_one({"email": email, "password": hashed_pw})
    return "Signup successful"

# Login Function
def login_user(email, password):
    user = users.find_one({"email": email})
    if user and check_password_hash(user["password"], password):
        session["user"] = email
        return "Login successful"
    return "Invalid credentials"
