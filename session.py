#!/usr/bin/python
# -*- coding: utf-8 -*-

def authenticate(db, login, password):
    """looks for login and password in database to check authentication

        :param db: mongodb database
        :param login: login from html form
        :param password: password from html form
        :returns: None if no user is found otherwise the user
    """
    user = db.users.find_one({'login':login, 'password':password})
    if not user :
        return None
    return user
