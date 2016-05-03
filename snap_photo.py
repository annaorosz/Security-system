
from subprocess import call


def snap_photo():
    imagename = "/home/pi/test.jpg"
    call(["fswebcam", "-c", "/home/pi/.fswebcam.conf", imagename])


snap_photo()

