# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config


access_key = 'u1M-QQ-m0ciNAhDn2AZ6iODyKnjUmY7EW1uH2ZiZ'
secret_key = 'QN3dDZvbX5MdDxfWsf4vua774Wz_5JFCZP78PGTU'


q = Auth(access_key, secret_key)


bucket_name = 'makerimg'


key = 'my-python-logo.png';


token = q.upload_token(bucket_name, key, 3600)


localfile = './sync/bbb.jpg'

ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
