#coding:utf-8  
  
import os  
from PIL import Image
def main(name,types):
	global pics
	pics=[]
	pics_handled=[]
	check_list=[]

	for root,dirs,files in os.walk(name):
		for i in files:  
			if os.path.splitext(i)[1][1:] == types :  
				pics.append(i)
				for k in range(len(pics)):
					check_list.append('%d.jpg'%k)
				if i not in check_list:
					pics_handled.append(i)
	change_size(pics)
	change_names(pics)
def change_names(pics):
	count=1
	for j in pics: 
		try:
			os.rename(j,'%d.jpg'%count)
		except WindowsError:
			print '%d.jpg exist'%count
		finally:
			count+=1
def change_size(pics):
	print pics
	for i in pics:
		im=Image.open(i)
		im=im.resize((1360,600),Image.ANTIALIAS)
		print im.size
		im.save(i)

if __name__ == '__main__':  
	main(os.getcwd(),"jpg")