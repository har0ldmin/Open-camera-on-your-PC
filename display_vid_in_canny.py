from cgi import print_form
import sys
import cv2
from cv2 import CAP_PROP_FPS

capture = cv2.VideoCapture("vid1.mp4")

if not capture.isOpened():
    print("Camera open failed..!")
    sys.exit()

# Set camera frame size
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# print camera frame size
w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("width: %d, height: %d" % (w,h))

while True:
    ret, frame = capture.read()
    if not ret: break

    # cv2.imshow("frame", frame)
    
    edge = cv2.Canny(frame, 50, 150)
    cv2.imshow("edge", edge)

    if cv2.waitKey(10) == 27: break 

capture.release()
cv2.destroyAllWindows()


