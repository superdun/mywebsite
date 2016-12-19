# -*- coding: utf-8 -*-

import requests
import math


class faceDetect(object):
    def __init__(self,file,apiKey,apiSecret):
        self.file=file
        self.apiKey=apiKey
        self.apiSecret=apiSecret
        self.payLoad = {'api_key': apiKey, 'api_secret': apiSecret
            , 'return_attributes': 'gender,age,smiling,glass,headpose','return_landmark':1}
        self.file = {'image_file': file}
    def postData(self):
        r = requests.post("https://api-cn.faceplusplus.com/facepp/v3/detect", data=self.payLoad, files=self.file)
        self.result = r.json()
        if self.result.has_key('error_message'):
            self.status =False
            self.error = self.result['error_message']
        else:
            self.status = True
            self.error = False

    def anayFace(self):
        if not self.error:
            face = self.result['faces'][0]
            self.faceNum = len(self.result['faces'])
            self.gender=face['attributes']['gender']
            self.age = face['attributes']['age']
            if face['attributes']['smile']['value']>face['attributes']['smile']['threshold']:
                self.isSmilling=True
            else:
                self.isSmilling = False
            headAngels=face['attributes']['headpose']
            self.headPutRight=True
            for i in headAngels.values():
                if i>=20:
                    self.headPutRight=False
            self.glassStatus = face['attributes']['glass']['value']
            self.faceLandmark =face['landmark']
            self.faceWidth = self.faceLandmark['contour_right1']['x']-self.faceLandmark['contour_left1']['x']
            self.noseWidth = self.faceLandmark['nose_right']['x']-self.faceLandmark['nose_left']['x']
            self.noseLength = self.faceLandmark['nose_contour_lower_middle']['y']-(self.faceLandmark['nose_contour_right1']['y']+self.faceLandmark['nose_contour_left1']['y'])/2
            self.leftEyeWidth =self.faceLandmark['left_eye_right_corner']['x']- self.faceLandmark['left_eye_left_corner']['x']
            self.rightEyeWidth = self.faceLandmark['right_eye_right_corner']['x']- self.faceLandmark['right_eye_left_corner']['x']
            self.chinMouthLength = self.faceLandmark['contour_chin']['y']-self.faceLandmark['mouth_lower_lip_bottom']['y']
            self.chinNoseLength = self.faceLandmark['contour_chin']['y']-self.faceLandmark['nose_contour_lower_middle']['y']
            self.quanWidth =  self.faceLandmark['contour_right2']['x']-self.faceLandmark['contour_left2']['x']
            self.heWidth1 =  self.faceLandmark['contour_right7']['x']-self.faceLandmark['contour_left7']['x']
            self.heWidth2 =  self.faceLandmark['contour_right8']['x']-self.faceLandmark['contour_left8']['x']
            self.chinAngle = math.atan2(((self.faceLandmark['contour_right9']['x']-self.faceLandmark['contour_left9']['x'])/2),self.faceLandmark['contour_chin']['y']-((self.faceLandmark['contour_right9']['y']+self.faceLandmark['contour_left9']['y'])/2))*360/math.pi


        else:
            self.faceNum=0
# class fortuneTelling(object):
#     def __init__(self,face):

file=open('C:/Users/lidad/Desktop/opt/mywebsite/static/uploadFace/123.jpg','rb')
d=faceDetect(file,'ZfZkvZVgtmq023KgiYjj8zYp-eGmG-wJ','F2pl2jjyeTtSFPIllQ-MCF9HT2DPqRv5')
d.postData()
d.anayFace()
print d.error
print d.chinAngle
