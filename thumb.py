import os
import os.path as op
import string ,random

def relativePath():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))+'/'