#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, session, redirect, url_for
from bson.objectid import ObjectId
import pymongo

from session import authenticate
from manage_posts import add_post as add_new_post

#init app
app_name = "flask_experiment"
app = Flask(app_name)
#configure app for session
secret_key = "YZC2GwVUyMFY6fWFyrPjJpJy"
app.secret_key = secret_key
#init db
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.flask_experiment

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
            warning = u"Tous les champs sont obligatoires."
        user = authenticate(db, login, password)
        if user is None :
            warning = u"L'autentification a échoué."
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
def hello_world(page_number=0):
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
