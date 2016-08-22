from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('localConfig.py')
db = SQLAlchemy(app)

#db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    auth = db.Column(db.String(120))
    password = db.Column(db.String(120))

    def __init__(self, name='', auth=1, password=''):
        self.name = name
        self.auth = auth
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name
#Flask-Admin can't create model if it has constructor with non-default parameters
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(2000))
    create_at = db.Column(db.Integer)
    img = db.Column(db.String(120))
    view_count = db.Column(db.Integer)
    summary = db.Column(db.String(255))
    category = db.Column(db.String(120))
    book_count = db.Column(db.Integer)
    max_book_count = db.Column(db.Integer)
    status = db.Column(db.String(120))
    is_full = db.Column(db.String(120))
    def __init__(self, title='', content='', img='', view_count=0, summary='', category='', book_count=0, max_book_count=0,status='',is_full='no'):
        self.title = title
        self.content = content
        self.create_at = time.time()
        self.img = img
        self.view_count = view_count
        self.summary = summary
        self.category = category
        self.book_count = book_count
        self.max_book_count = max_book_count
        self.status = status
        self.is_full = is_full
    def __repr__(self):
        return '<post %r>' % self.title
class Carousel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(80))
    title = db.Column(db.String(120))
    content = db.Column(db.String(120))

    def __init__(self, img='', title=1, content=''):
        self.img = img
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Carousel %r>' % self.title