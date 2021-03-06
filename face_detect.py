import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def human_face_detect(img):
    resize_img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 2)

    face_num = len(faces)
    max_area = 0
    if face_num  > 0:
        for (x,y,w,h) in faces:
            x = x*2
            y = y*2
            w = w*2
            h = h*2
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    return img

#init camera
print("start human face detect")
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=camera.resolution)

for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
    img = frame.array
    img =  human_face_detect(img)
    cv2.imshow("video", img)
    rawCapture.truncate(0)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        camera.close()
        break
