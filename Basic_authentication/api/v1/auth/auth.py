#!/usr/bin/env python3
"""Class Auth"""

from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None
