#!/usr/bin/python
# -*- coding: utf-8 -*-

def add_post(db, data):
    post = {
        'title': data['title'],
        'short': data['short'],
        'body': data['body'],
        'date': data['date']
    }
    a = db.posts.insert(post)
    return a
