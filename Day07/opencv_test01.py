# openCV 테스트
import cv2
from picamera2 import Picamera2

cam = Picamera2()
cam.preview_configuration.main.size =(800, 600)
cam.preview_configuration.main.format='RGB'
cam.preview_configuration.align()

cam.configure('priview')
cam.start()

while True:
    frame = cam.capture_array()
    cv2.imshow('piCam',frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()