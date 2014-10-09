#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, session, redirect, url_for
from bson.objectid import ObjectId
import pymongo
import ConfigParser

from session import authenticate
from manage_posts import add_post as add_new_post

#init config
config = ConfigParser.SafeConfigParser()
if config.read('config.ini') == [] :
    config.add_section('miniblog')
    config.set('miniblog', 'app_name', 'miniblog')
    config.set('miniblog', 'secret_key', 'RAE9Td7BEUy8xCmT4Hm5wXCR')
#init app
app = Flask(config.get('miniblog', 'app_name'))
#configure app for session
app.secret_key = config.get('miniblog', 'secret_key')
#init db
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.miniblog

@app.route('/add_post')
def add_post():
    add_new_post(db)
    return "add post"

@app.route('/logout')
def logout():
    del session['username']
    return redirect('/index/0')

@app.route('/login', methods=['GET', 'POST'])
def login():
    warning=None
    if request.method == "POST":
        try:
            login = request.form['login']
            password = request.form['password']
        except KeyError:
            warning = u"Every field is mandatory."
        user = authenticate(db, login, password)
        if user is None :
            warning = u"Authentication failed."
        else :
            session['username'] = user['login']
            return redirect('/index/0') #TODO : make it use url_for
    return render_template("login_form.html", warning=warning)

@app.route('/post/<post_id>')
def show_post(post_id):
    """show the post with the given post_id"""
    post = db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("post.html", post=post)

@app.route('/')
@app.route('/index/<int:page_number>')
def index(page_number=0):
    nb_posts_by_page = 5
    offset = page_number * nb_posts_by_page
    limit = (page_number + 1) * nb_posts_by_page
    first = False if offset > 0 else True
    last = False if limit < db.posts.count() else True
    posts = [post for post in db.posts.find()]
    return render_template("home.html", title="home", posts=posts[offset:limit],
    			current_page=page_number, first=first, last=last)

if __name__ == '__main__':
    app.run(debug=True)
