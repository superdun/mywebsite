#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template ,url_for,jsonify,request,Response
from flask.ext.mail import Mail ,Message
from flask.ext.bootstrap import Bootstrap 
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from wtforms import Form as wtForm
from dbORM import db,User,Post,Carousel
from wtforms import TextAreaField
from wtforms.widgets import TextArea
import thumb
from flask_qiniustorage import Qiniu
from flask_admin import form
from flask_admin.form import rules
import os
import os.path as op





app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('localConfig.py')

bootstrap = Bootstrap(app)
admin = Admin(app)
qiniu_store = Qiniu(app)

UPLOAD_URL=app.config.get('UPLOAD_URL', '')
QINIU_DOMAIN = app.config.get('QINIU_BUCKET_DOMAIN', '')




def mail(goal,text):
	app.config['MAIL_SERVER'] = 'smtp.163.com'
	app.config['MAIL_PORT'] = 465
	app.config['MAIL_USE_SSL'] = True
	app.config['MAIL_USERNAME'] = 'ecust_maker@163.com'
	app.config['MAIL_PASSWORD'] = 'ecustmaker1'
	mail=Mail(app)
	msg = Message(u'申请加入%s'%goal, sender='ecust_maker@163.com',recipients=['ecust_maker@163.com']) 
	msg.body = text
	with app.app_context():
		mail.send(msg)	

def get_file_for_ajax(source_name):#change the html's ajax arg sourse 
	pics=[]
	heads=[]
	introduction=[]	
	for root,dirs,files in os.walk(os.getcwd()+'/static/%s'%source_name): 
		for i in files:
			if os.path.splitext(i)[1][1:] == 'jpg':
				pics.append(url_for('static',filename='%s/%s'%(source_name,i)))
				txt=open(os.getcwd()+'/static/%s/%s.txt'%(source_name,os.path.splitext(i)[0]),'rb')
				lines=txt.readlines()
				heads.append(lines[0].decode("gb2312").encode("utf-8"))
				introduction.append(''.join(lines[1:]).decode("gb2312").encode("utf-8"))
				txt.close()
	return [pics,heads,introduction]
	
	#
@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/show_works')
def show_works():
	return render_template('show_works.html')
	
@app.route('/apply')
def apply():
	return render_template('apply.html')
	
@app.route('/book_tools')
def book_tools():
	return render_template('book_tools.html')
	
@app.route('/our_cool')
def our_cool():
	return render_template('our_cool.html')
	
@app.route('/stationmaster')#personal
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
	
	
@app.route('/container_ajax')#ajax
def apply_ajax():
	res=get_file_for_ajax(request.args.get('source'))
	return jsonify(pics=res[0],heads=res[1],introduction=res[2])
	
@app.route('/joinus')
def joinin():#ajax....
	if request.args.get('name') and request.args.get('phone').isdigit():
		text=request.args.get('name')+u'申请加入'+request.args.get('goal')+u'，电话:'+request.args.get('phone')
		mail(request.args.get('goal'),text)
		return jsonify(status='OK',result=u'欢迎你!!  '+request.args.get('name')+u'  你的信息已经提交，我们会尽快联系你')
	else:
		return jsonify(status='NO',result=u'请正确完整输入个人信息！')

@app.route('/admin/upload',methods = ['POST'])
def upload():
    file = request.files.to_dict()['files[]']
    result = thumb.upload_file(file,UPLOAD_URL,QINIU_DOMAIN,qiniu_store)	
    return jsonify(result)

#admin	


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
            if '200' in ret :
                os.remove(path)
                return filename
            raise Exception("upload to qiniu failed", ret)

class PostView(ModelView):


    # Override displayed fields
    column_list = ("title", "create_at", "view_count", "category", "book_count", "max_book_count")

    form_overrides = {
        'content': CKTextAreaField
    }
    form_extra_fields = {
        'img': ImageUpload('Image',base_path=UPLOAD_URL,relative_path = thumb.relativePath())
    }
    form_columns = ("title", "summary", "category",  "max_book_count", "content", "img")
    form_excluded_columns = ('create_at')
    create_template = 'admin/post/create.html'
    edit_template = 'admin/post/edit.html'
    @expose('/upload')
    def test(self):
        return self.render('admin/test.html')




class CarouselView(ModelView):

    form_extra_fields = {
        'img': form.ImageUploadField('Image',base_path=UPLOAD_URL)
    }


admin.add_view(ModelView(User, db.session))
admin.add_view(PostView(Post,db.session))
admin.add_view(CarouselView(Carousel,db.session))









if __name__ == '__main__':
	app.run(port=8081,debug=True)
