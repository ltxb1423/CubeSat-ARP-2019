from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (2592,1944)
camera.framerate = 15


#enforcing the camera settings
camera.ISO = 800
camera.saturation= 50
camera.brightness= 0
camera.contrast= 0
camera.sharpness =0




for i in range(0,20):
    print("Taking picture in 5 seconds.")
    sleep(5)
    camera.capture('/home/pi/Desktop//Pictures/%d.jpg'%i)
    sleep(5)
    print("Picture %d taken. Cool down for 5 seconds."%i)
    sleep(5)

print("Pictures taken. Program ended.")
