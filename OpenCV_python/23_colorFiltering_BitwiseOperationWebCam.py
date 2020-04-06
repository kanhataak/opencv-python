import cv2
import numpy as np

capture = cv2.VideoCapture(0)
# print(capture)
while True:
    ret, frame = capture.read()
    # HSV thresholding to get rid of as much background as possible
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # print(hsv)
    # you can change array value(hsv hue sat value...)
    low_range = np.array([50, 50, 50])
    up_range = np.array([240, 255, 255])
    # print("High",high_range)
    # print("Low",low_range)
    #
    mask = cv2.inRange(hsv,low_range,up_range)
    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("First mask", mask) # filter output Black in white
    cv2.imshow("Second Frame", frame) # Real camera video output
    cv2.imshow("Result",result) # blue

    k = cv2.waitKey(5) & 0xFF
    if k == 13:
        break
capture.release()
cv2.destroyAllWindows()