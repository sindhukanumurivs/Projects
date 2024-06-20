from flask import Flask, request, jsonify, redirect, url_for
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://sindhukanumurivs:sindhu123@cluster0.jsd84n0.mongodb.net/sample-mflix?retryWrites=true&w=majority"
  # Replace with your MongoDB URI
mongo = PyMongo(app)
CORS(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    password = generate_password_hash(data['password'])

    user = mongo.db.users.find_one({'email': email})

    if user:
        return jsonify({'message': 'User already exists'}), 409

    mongo.db.users.insert_one({
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'password': password
    })

    return jsonify({'message': 'Registration successful'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user = mongo.db.users.find_one({'email': email})

    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'message': 'Invalid email or password'}), 401
from flask import Flask, request, jsonify

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
