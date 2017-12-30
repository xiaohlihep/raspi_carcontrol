#!/usr/bin/python
import cgitb
from picamera import PiCamera
camera = PiCamera()
camera.capture('/var/www/html/cam.jpg')
print ('saved in /var/www/html/cam.jpg')
print 'done'
