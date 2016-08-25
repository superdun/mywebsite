#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, jsonify, request, Response, redirect
from moduleMail import mail
from flask_bootstrap import Bootstrap
from dbORM import db, User, Post, Carousel
import thumb
from moduleGlobal import app, bootstrap, qiniu_store, QINIU_DOMAIN, CATEGORY, UPLOAD_URL
import moduleAdmin as admin
import flask_login
import os
import os.path as op
from moduleWechat import wechat_resp
#debug in wsgi
# from werkzeug.debug import DebuggedApplication

# app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

#

application = app


@app.route('/')
def index(carousels=None, img_domain=QINIU_DOMAIN, thumbnail=''):
    carousels = Carousel.query.all()
    thumbnail = app.config.get('CAROUSEL_THUMBNAIL')
    return render_template('index.html', carousels=carousels, img_domain=img_domain, thumbnail=thumbnail)


@app.route('/show_works')
def show_works(items=None, img_domain=QINIU_DOMAIN, thumbnail=''):
    thumbnail = app.config.get('PREVIEW_THUMBNAIL')
    print CATEGORY[0][0]
    items = Post.query.filter_by(
        category=CATEGORY[0][0], status='published').all()

    return render_template('show_works.html', items=items, img_domain=img_domain, thumbnail=thumbnail)


@app.route('/apply')
def apply(items=None, img_domain=QINIU_DOMAIN, thumbnail=''):
    thumbnail = app.config.get('PREVIEW_THUMBNAIL')
    items = Post.query.filter_by(
        category=CATEGORY[1][0], status='published').all()
    return render_template('apply.html', items=items, img_domain=img_domain, thumbnail=thumbnail)


@app.route('/book_tools')
def book_tools(items=None, img_domain=QINIU_DOMAIN, thumbnail=''):
    thumbnail = app.config.get('PREVIEW_THUMBNAIL')
    items = Post.query.filter_by(
        category=CATEGORY[2][0], status='published').all()
    return render_template('book_tools.html', items=items, img_domain=img_domain, thumbnail=thumbnail)


@app.route('/our_cool')
def our_cool(items=None, img_domain=QINIU_DOMAIN, thumbnail=''):
    thumbnail = app.config.get('PREVIEW_THUMBNAIL')
    items = Post.query.filter_by(
        category=CATEGORY[3][0], status='published').all()
    return render_template('our_cool.html', items=items, img_domain=img_domain, thumbnail=thumbnail)


@app.route('/container_ajax')  # ajax
def apply_ajax():
    res = get_file_for_ajax(request.args.get('source'))
    return jsonify(pics=res[0], heads=res[1], introduction=res[2])


@app.route('/joinus')
def joinin():  # ajax....
    if request.args.get('name') and request.args.get('phone').isdigit():
        text = request.args.get(
            'name') + u'申请加入' + request.args.get('goal') + u'，电话:' + request.args.get('phone')
        mail(request.args.get('goal'), text)
        return jsonify(status='OK', result=u'欢迎你!!  ' + request.args.get('name') + u'  你的信息已经提交，我们会尽快联系你')
    else:
        return jsonify(status='NO', result=u'请正确完整输入个人信息！')

# IoT


@app.route('/iot')
def iot():
    return render_template('iot.html')


@app.route('/iot/wechat')
def iot_bath_temp():
    token = app.config.get('WECHAT_TOKEN')
    appid = app.config.get('WECHAT_APPID')
    appsecret = app.config.get('WECHAT_APPSECRET')
    encoding_aes_key = app.config.get('WECHAT_AESKEY')
    encrypt_mode = app.config.get('WECHAT_ENC_MODE')
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    return wechat_resp(token, appid, appsecret,
                       encoding_aes_key, encrypt_mode,signature,timestamp,nonce,echostr)


@app.route('/admin/upload', methods=['POST'])
def upload():
    file = request.files.to_dict()['files[]']
    result = thumb.upload_file(file, UPLOAD_URL, QINIU_DOMAIN, qiniu_store)
    return jsonify(result)

# personal


@app.route('/stationmaster')  # personal
def stationmaster():
    return render_template('stationmaster.html')


@app.route('/guess_num')
def guess_num():
    return render_template('guess_num/guess_num.html')


@app.route('/marysue')
def marysue():
    return render_template('marysue/marysue.html')


@app.route('/spacebattle')
def spacebattle():
    return render_template('spacebattle/spacebattle.html')


@app.route('/eros')
def eros():
    return render_template('eros/eros.html')


@app.route('/refine')
def refine():
    return render_template('refine/refine.html')


@app.route('/dragonboat')
def dragonboat():
    return render_template('dragonboat/dragonboat.html')


@app.route('/fiveson')
def fiveson():
    return render_template('fiveson/fiveson.html')


@app.route('/mosquito')
def mosquito():
    return render_template('mosquito/mosquito.html')

# admin
admin.dashboard()

# login


login_manager = flask_login.LoginManager()

login_manager.init_app(app)
users = {}
raw_users = User.query.all()
for user in raw_users:
    users[user.name] = {'password': user.password}


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if flask_login.current_user.is_authenticated:
            return redirect('/admin')
        return render_template('login.html')

    username = request.form['username']
    if request.form['password'] == users[username]['password']:
        user = User()
        user.id = username
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return redirect('/admin')


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'
app.debug = True
if __name__ == '__main__':
    app.run()
