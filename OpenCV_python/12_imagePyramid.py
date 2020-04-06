# image resize using image pyramid this is image resize technique
# we wand to half or double an image we can without knows the dimnsation

import  cv2

pic = cv2.imread("bharti.jpeg")
small = cv2.pyrDown(pic)
large = cv2.pyrUp(pic)

cv2.imshow("Original",pic)
cv2.waitKey()
cv2.imshow("Smaller",small)
cv2.waitKey()
cv2.imshow("Larger", large)

cv2.waitKey()
cv2.destroyAllWindows()