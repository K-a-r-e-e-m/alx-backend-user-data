#!/usr/bin/env python3
""" Module of authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class for authentication system """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ validating if endpoint requires auth or not """
        return False

    def authorization_header(self, request=None) -> str:
        """ handles authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates for current user """
        return None
