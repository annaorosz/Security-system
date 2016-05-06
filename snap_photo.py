#!/usr/bin/env python

# this code is to take a picture with the webcam and save the image
# by the name 'security_image.jpg" to the home directoy of the pi user

# importing the necessary libraries
from subprocess import call

# defining the function to take the picture
def snap_photo():
    imagename = "/home/pi/security_image.jpg"
    call(["fswebcam", "-c", "/home/pi/.fswebcam.conf", imagename])

# calling the function and taking the picture
snap_photo()

