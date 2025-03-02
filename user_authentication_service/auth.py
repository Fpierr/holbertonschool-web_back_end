#!/usr/bin/env python3
"""hash pasword"""

import bcrypt


def _hash_password(password: str) -> str:
    hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hash
