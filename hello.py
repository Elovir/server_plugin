#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World Bis!'

from flask import Flask, session, redirect, url_for, escape, request
import os
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)

@app.route('/t')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

# @app.route('/')
# def index():
#     if 'username' in session:
#         return 'Logged in as %s' % escape(session['username'])
#     return 'You are not logged in'

@app.route('/plugin', methods=['GET', 'POST'])
def test():
	print("test")
	print(request.form)
	return "Received"


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = '\xbd\xd2\xe7RlP\x13P$\xf7%\xca2\xf5\xec\xd6|\xb6\xfdf\x9b\xcap\x99'

if __name__ == "__main__":
    app.run()
