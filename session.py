#!/usr/bin/python
# -*- coding: utf-8 -*-

def authenticate(db, login, password):
    user = db.users.find_one({'login':login, 'password':password})
    if not user :
        return None
    return user
