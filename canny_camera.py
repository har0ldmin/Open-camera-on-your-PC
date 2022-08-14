import sys
import cv2
from cv2 import CAP_PROP_FPS

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Camera open failed!")
    sys.exit()

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


while True:
    ret, frame = capture.read()     # frame : is an image array vector captured based on the default frames per second defined explicitly or implicitly

    if not ret:     # ret : a boolean variable that returns true if the frame is available.
        break   

    '''
    msec = capture.get(cv2.CAP_PROP_POS_MSEC) 
    print(msec)
    '''

    # Display normal camera
    # cv2.imshow("frame", frame)
    
    # Display Canny
    edge = cv2.Canny(frame, 50, 20)
    cv2.imshow("edge", edge)


    if cv2.waitKey(20) == 27: 
        break


capture.release()
cv2.destroyAllWindows()


