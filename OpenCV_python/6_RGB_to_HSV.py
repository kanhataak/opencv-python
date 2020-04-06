import cv2
img = cv2.imread("bharti.jpeg")

imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# how to show HSV Images what is the output actually 
cv2.imshow("HSV image", imgHsv)
cv2.waitKey(0) # press enter
cv2.imshow("Hue CHANNEL :",imgHsv[:, :, 0])
cv2.waitKey(0) # press enter
cv2.imshow("Saturation CHANNEL :",imgHsv[:, :, 1])
cv2.waitKey(0) # press enter
cv2.imshow("Value CHANNEL :",imgHsv[:, :, 2])
cv2.waitKey(0) # press enter

cv2.destroyAllWindows()