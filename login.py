from flask import Flask, render_template, url_for, jsonify, request, Response, redirect
import flask_login
from moduleGlobal import app


login_manager = flask_login.LoginManager()

login_manager.init_app(app)

users = {'admin': {'pw': 'password'}}


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return

    user = User()
    user.id = username
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('username')
    if email not in users:
        return

    user = User()
    user.id = username

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form[
        'password'] == users[email]['password']

    return user



