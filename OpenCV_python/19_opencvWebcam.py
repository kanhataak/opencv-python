# how to access webcam
import cv2

# using by cv2 class calling the videocapture function
cv2.namedWindow("Window1")
cap = cv2.VideoCapture(0)

while True:
#     in cap variable store videostrem we will read
# hold by frame variable
# "ret" variable retrun the cap variable value
    ret, frame = cap.read()
    cv2.imshow("Our Live Sketch", frame)
    try:
        cv2.waitKey(1)
    except KeyboardInterrupt:
        break
cap.release()
cv2.destroyWindow("Window1")
