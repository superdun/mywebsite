# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, jsonify, request, Response, redirect
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from wtforms import Form as wtForm
from dbORM import db, User, Post, Carousel
from wtforms import TextAreaField, SelectField
from wtforms.widgets import TextArea
import thumb
from flask_qiniustorage import Qiniu
from flask_admin import form
from flask_admin.form import rules
import flask_login
import os
import os.path as op
from moduleGlobal import app, qiniu_store, QINIU_DOMAIN, CATEGORY, UPLOAD_URL


def dashboard():

    admin = Admin(app)
    admin.add_view(ModelView(User, db.session))
    admin.add_view(PostView(Post, db.session))
    admin.add_view(CarouselView(Carousel, db.session))





class CKTextAreaWidget(TextArea):

    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class ImageUpload(form.ImageUploadField):

    def _save_file(self, data, filename):
        path = self._get_path(filename)
        if not op.exists(op.dirname(path)):
            os.makedirs(os.path.dirname(path), self.permission | 0o111)

        data.seek(0)
        data.save(path)
        with open(path, 'rb') as fp:
            ret, info = qiniu_store.save(fp, filename)
            if 200 != info.status_code:
                raise Exception("upload to qiniu failed", ret)
            # os.remove(path)
            return filename


class PostView(ModelView):

    # Override displayed fields
    column_list = ("title", "create_at", "view_count",
                   "category", "book_count", "max_book_count")

    form_overrides = {
        'content': CKTextAreaField
    }
    form_extra_fields = {
        'img': ImageUpload('Image', base_path=UPLOAD_URL, relative_path=thumb.relativePath()),
        'category': SelectField(u'category', choices=CATEGORY)
    }
    form_columns = ("title", "summary", "category",
                    "max_book_count", "content", "img")
    form_excluded_columns = ('create_at')
    create_template = 'admin/post/create.html'
    edit_template = 'admin/post/edit.html'


class CarouselView(ModelView):

    form_extra_fields = {
        'img': ImageUpload('Image', base_path=UPLOAD_URL, relative_path=thumb.relativePath())
    }
