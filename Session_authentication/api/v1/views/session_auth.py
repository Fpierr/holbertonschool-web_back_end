from flask import request, jsonify
from api.v1.app import auth
from models.user import User


@app.route('/api/v1/auth_session/login',
           methods=['POST'], strict_slashes=False)
def login():
    """ Logs a user in by creating a session """

    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if user is None:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, session_id)

    return response
