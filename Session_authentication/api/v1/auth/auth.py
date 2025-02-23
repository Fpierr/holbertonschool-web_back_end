#!/usr/bin/env python3
"""Class Auth"""

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """To manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not path.endswith("/"):
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request"""
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None

    def session_cookie(self, request=None):
        """Retrieve the session cookie value from the request"""
        if request is None:
            return None
        session_name = getenv("SESSION_NAME")
        if session_name is None:
            return None
        return request.cookies.get(session_name)
