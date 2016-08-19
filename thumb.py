import os
import os.path as op
import string ,random
from werkzeug import secure_filename
from flask_qiniustorage import Qiniu


def relativePath():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))+'/'

def allowed_file(filename):
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def upload_file(file,path,domain,storeModel):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = path+'/'+relativePath()+filename
        if not op.exists(op.dirname(path)):
            os.makedirs(os.path.dirname(path))
        print domain+'/'+relativePath()+filename
        file.seek(0)
        file.save(path)
        with open(path, 'rb') as fp:
            ret, info = storeModel.save(fp, filename)
            print info
            if '200' in ret :
                os.remove(path)
                return filename
            raise Exception("upload to qiniu failed", info)
        localUrl =domain+relativePath()+filename
        title =  filename.rsplit('.', 1)[0]
        return {"title":title,"isImage":1,"fileName":filename,"localUrl":localUrl}
