from flask import Blueprint, jsonify, request
from app import db
from app.models import User 



main = Blueprint('main', __name__)

@main.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    # Here you would typically verify the username and password
    # For simplicity, we will just return a mock token
    if username == "test" and password == "test":
        return jsonify({"token": "mock_token"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
    
@main.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Здесь можно просто возвращать сообщение
    return jsonify({"message": f"User {username} registered (mock)"}), 201