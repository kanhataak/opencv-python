# How to image Transpose...
import  cv2
img = cv2.imread("bharti.jpeg")
# rotated image by using transpose function in which one argument original image...
rotated_img = cv2.transpose(img)

cv2.imshow("Rotated Image",rotated_img)
cv2.imshow("Actual Image",img)
cv2.waitKey(0)
cv2.destroyAllwindows()