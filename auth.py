import jwt
from flask import request, jsonify
from functools import wraps
from model import db
from model import Book
from datetime import datetime, timedelta
from flask import current_app as app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            
        except Exception as e:
            print(e)
            return jsonify({'message': 'Token is invalid'}), 401

        return f(*args, **kwargs)

    return decorated


def generate_token(username, password):
    # Check if the user exists and the password is correct
    if username == 'admin' and password == 'admin':
        # Token expiration time (e.g., 1 hour)
        expiration = datetime.utcnow() + timedelta(hours=1)
        
        # Create JWT payload
        payload = {
            'username': username,
            'exp': expiration
        }
        
        # Generate JWT token
        token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        
        return token
    else:
        return None