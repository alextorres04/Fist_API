from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my API!"

# GET -> obtener datos
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Alexander",
        "email": "alex12@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200

# POST -> crear datos
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify({"message": "User created", "data": data}), 201

# PUT -> actualizar datos
@app.route("/update-user/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    return jsonify({"message": f"User {user_id} updated", "data": data}), 200

# DELETE -> eliminar datos
@app.route("/delete-user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify({"message": f"User {user_id} deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
