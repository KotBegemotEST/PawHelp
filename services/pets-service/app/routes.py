from flask import Blueprint, jsonify, request
from app import db
from app.models import Pet

main = Blueprint('main', __name__)

@main.route("/health")
def health():
    return jsonify({"status": "ok"})

@main.route("/pets", methods=["GET"])
def get_pets():
    pets = Pet.query.all()
    return jsonify([pet.to_dict() for pet in pets])

@main.route("/pets", methods=["POST"])
def add_pet():
    data = request.json
    pet = Pet(name=data["name"], type=data["type"])
    db.session.add(pet)
    db.session.commit()
    return jsonify(pet.to_dict()), 201
