#!/usr/bin/env python3
"""create flask app"""

from auth import Auth
from flask import Flask, jsonify, redirect, request
from flask import abort

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home():
    """create home route"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route('/users', methods=['POST'])
def register_users():
    """define route users function"""
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    message = {"email": email, "message": "user created"}
    return jsonify(message), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
