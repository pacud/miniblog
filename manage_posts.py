#!/usr/bin/python
# -*- coding: utf-8 -*-

def add_post(db, data):
    """add a post in the mongo database

    :param db: mongodb database
    :param data: data directly from the html form
    :returns: returns the post id post insert
    """
    post = {
        'title': data['title'],
        'short': data['short'],
        'body': data['body'],
        'date': data['date']
    }
    a = db.posts.insert(post)
    return a
