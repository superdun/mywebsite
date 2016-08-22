from flask import Flask


SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost:3306/makersite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '123456'
QINIU_ACCESS_KEY = 'u1M-QQ-m0ciNAhDn2AZ6iODyKnjUmY7EW1uH2ZiZ'
QINIU_SECRET_KEY = 'QN3dDZvbX5MdDxfWsf4vua774Wz_5JFCZP78PGTU'
QINIU_BUCKET_NAME = 'makerimg'
QINIU_BUCKET_DOMAIN = 'oc1is8h9w.bkt.clouddn.com'

MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'ecust_maker@163.com'
MAIL_PASSWORD = 'ecustmaker1'