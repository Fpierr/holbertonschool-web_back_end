#!/usr/bin/env python3
"""SessionAuth Module"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session authentication class, inheriting from Auth."""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session ID for a given user ID
        Args:
            user_id (str): ID of the user
        Returns:
            str: The created session ID, or None if invalid
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieve the User ID based on the given Session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str: The associated User ID, or None if not found.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
