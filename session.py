#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import wraps
from flask import render_template


def authenticate(db, login, password):
    """looks for login and password in database to check authentication

        :param db: mongodb database
        :param login: login from html form
        :param password: password from html form
        :returns: None if no user is found otherwise the user
    """
    user = db.users.find_one({'login': login, 'password': password})
    if not user:
        return None
    return user


def check_authentication(session):
    """decorator designed to check if user is authenticated

    :param session: flask session
    :returns: not_logged_in page if authentication fails or the decorated
    function otherwise
    """
    def wrapper(decorated):
        @wraps(decorated)
        def wrapped(*args, **kwargs):
            if session.get('username', None):
                return decorated(*args, **kwargs)
            return render_template("not_logged_in.html")
        return wrapped
    return wrapper
