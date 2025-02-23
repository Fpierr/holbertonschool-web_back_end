#!/usr/bin/env python3
""" Module of Session authentication views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.app import auth
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def login():
    """ POST /auth_session/login
    Return
        - Logged in user
    """
    email = request.form.get('email')

    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')

    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        found_users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not found_users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in found_users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

    user = found_users[0]
    session_id = auth.create_session(user.id)

    SESSION_NAME = getenv("SESSION_NAME", "_my_session_id")

    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, session_id, httponly=True,
                        secure=True, samesite="Lax")

    return response


@app_views.route('/api/v1/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ DELETE /api/v1/auth_session/logout
    Returns:
        - An empty dictionary if successful
    """
    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
