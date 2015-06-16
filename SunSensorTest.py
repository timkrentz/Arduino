'''
Created on Jul 31, 2014

@author: BOIRUM
'''

import cv2
import urllib
import numpy as np
import time
import datetime
import os

stream_url = "192.168.1.3"
bytes=''
dt = 1 #10ms
#vsfmDelay = 5 #secs
outputType = 'ocam'

rawImDir = r'Z:\Planetary Rover Localization\Calibration\2015-6-4 Sun Sensor Test'
#vsfmImDir = r'/home/glxp/Desktop/robot-city/unrectified-images/'

prevTsec = time.time()
while True:
    stream=urllib.urlopen('http://192.168.1.3/axis-cgi/jpg/image.cgi?resolution=640x480')
    while True:
        #print 'reading stream'
        bytes+=stream.read(1024)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
            jpg = bytes[a:b+2]
            bytes= bytes[b+2:]

            img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
            #cv2.imshow('i',i)
            if cv2.waitKey(1) ==27:
                exit(0)

            tsec = time.time()
            if outputType == 'ocam':
				timeStr = datetime.datetime.fromtimestamp(tsec).strftime('%Y-%m-%d_%H-%M-%S-%f')
				cv2.imwrite(os.path.join(rawImDir,'image'+timeStr+'.jpg'), img)
            else:
				timeStr = datetime.datetime.fromtimestamp(tsec).strftime('%Y-%m-%d_%H-%M-%S-%f')
				cv2.imwrite(os.path.join(rawImDir,'image'+timeStr+'.jpg'), img)
            #cv2.imshow('Raw from camera',img)
            print "image%s saved"%timeStr

            #write to vsfm directory only at every vsfmDelay seconds
            #if tsec-prevTsec > vsfmDelay:
               # cv2.imwrite(os.path.join(vsfmImDir,'image'+timeStr+'.jpg'), img)
                #prevTsec = tsec

            time.sleep(dt)
            break
