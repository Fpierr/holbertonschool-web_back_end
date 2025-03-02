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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
