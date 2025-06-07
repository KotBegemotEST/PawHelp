from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/pets", methods=["GET"])
def get_pets():
    pets = [
        {"id": 1, "name": "Buddy", "type": "Dog"},
        {"id": 2, "name": "Mittens", "type": "Cat"},
        {"id": 3, "name": "Goldie", "type": "Fish"}
    ]
    return jsonify(pets)

@app.route("/pets", methods=["POST"])
def add_pet():
    # In a real application, you would handle the request data to add a pet
    return jsonify({"message": "Pet added successfully"}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
