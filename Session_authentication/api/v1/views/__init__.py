#!/usr/bin/env python3
"""Initialize API v1 blueprint and routes.
"""

from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *
from models.user import User

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

User.load_from_file()
