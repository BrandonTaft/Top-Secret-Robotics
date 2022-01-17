from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.stop_preview()

# rotate cam
#camera = PiCamera()
#camera.rotation = 180

#make preview see thru
#camera.start_preview(alpha=200)

#take pic every 5 seconds up to 5 pics
#camera.start_preview()
# for i in range(5):
#     sleep(5)
#     camera.capture('/home/pi/Desktop/image%s.jpg' % i)
# camera.stop_preview()

#record 5 second video
# camera.start_preview()
# camera.start_recording('/home/pi/Desktop/video.h264')
# sleep(5)
# camera.stop_recording()
# camera.stop_preview()

