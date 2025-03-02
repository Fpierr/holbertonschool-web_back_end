#!/usr/bin/env python3
"""hash pasword"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> str:
    hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hash


def _generate_uuid() -> str:
    """Generate a new UUID as a string

    Returns:
        str: A string representation of a UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user"""

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login credentials"""
        try:
            user = self._db.find_user_by(email=email)

            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
            return False

        except NoResultFound:
            return False
