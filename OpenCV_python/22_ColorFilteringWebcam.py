import cv2
import numpy as np

capture = cv2.VideoCapture(0)
# print(capture)
while True:
    ret, frame = capture.read()
    # print(ret)
    # print(frame)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # print(hsv)
    # you can change array value
    low_range = np.array([110, 80, 80])
    high_range = np.array([140, 255, 255])
    # print("High",high_range)
    # print("Low",low_range)
    #
    drow = cv2.inRange(hsv,low_range,high_range)

    cv2.imshow("First", drow) # filter output
    cv2.imshow("Second", frame) # Real camera video output
    if cv2.waitKey(1)==13:
        break
capture.release()
cv2.destroyAllWindows()