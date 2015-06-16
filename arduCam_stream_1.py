'''
Created 2014

@author: BOIRUM

Edited June 15, 2015
@author	KRENTZ
'''

import serial

import cv2
import urllib
import numpy as np
import time
import datetime
import os

stream_url = "192.168.1.3"
bytes=''
dt = 0.1 #10ms
#vsfmDelay = 5 #secs
outputType = 'ocam'

rawImDir = r'/home/tim/Pictures/arduStream'

#Initialize the serial object, set port and baudrate
ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
#ser.baudrate(115200)
#ser.port(dev/ttyACM0)

count = 0;

#prevTsec = time.time()
while True:
	print 'reading stream\n'	
	bytes+=ser.read(1024)
	a = bytes.find('\xff\xd8')
	b = bytes.find('\xff\xd9')
	count = count + 1	
	print 'count = ',count 
	print 'a = ',a
	print 'b = ',b
	if a!=-1 and b!=-1:
		jpg = bytes[a:b+2]
		bytes= bytes[b+2:]
		print 'go!\n'

		img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
		#cv2.imshow('i',i)
		if cv2.waitKey(1) ==27:
			exit(0)

		tsec = time.time()
		if outputType == 'ocam':
			timeStr = datetime.datetime.fromtimestamp(tsec).strftime('%Y-%m-%d_%H-%M-%S-%f')
			print 'writing image...\n'	
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
