# Black in white image which all pixel between 0 or 1
# first we need to convert rgb image to grayscale image after convert the grayscale we will convert Black in White...

import  cv2
# convert grayscale
pic = cv2.imread("bharti.jpeg",0)
cv2.imshow("GrayScale",pic)
cv2.waitKey(0)

# Gray to Binary Img
# "ret" means return that a return a value in tuple form
ret, BW = cv2.threshold(pic,125, 255, cv2.THRESH_BINARY)
print(ret)
cv2.imshow("Black in white IMG",BW)
cv2.waitKey(0)

cv2.destroyAllWindows()