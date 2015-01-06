import cv2
import numpy as np
import urllib

stream=urllib.urlopen('http://192.168.10.1:8080/?action=stream')
bytes=''

while True:
    bytes+=stream.read(1080)
    # b = bytes.find('--markmarkmark')
    # print bytes
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_GRAYSCALE)
        if frame!= None:
			print "hi"
			cv2.imshow('authenticated cam',frame)
    	if cv2.waitKey(1) ==27:
    	    exit(0) 