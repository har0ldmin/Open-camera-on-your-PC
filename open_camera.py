import sys
import cv2


# Open Camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()


# Set camera frame size
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))


# Run camera
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('frame', frame)

    # If you want to inverse the display (i.e. color)
    # inversed = ~frame 
    # cv2.imshow('inversed', inversed)


    # Escape route
    if cv2.waitKey(10) == 27:       # cv2.waitKey(value) :  value =     fps
                                    # 27 = ESC
        break

cap.release()                       # Close Camera
cv2.destroyAllWindows()
