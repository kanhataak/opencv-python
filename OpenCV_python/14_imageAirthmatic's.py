import  cv2
import  numpy as np

img = cv2.imread("bharti.jpeg")
cv2.imshow("Original",img)
cv2.waitKey(0)
# M = np.ones(img.shape, dtype="uint8") * 150
M = np.zeros(img.shape, dtype="uint8") + 150
added_img= cv2.add(img, M)
cv2.imshow("Added Image", added_img)
cv2.waitKey(0)

multed_img= cv2.multiply(img, M)
cv2.imshow("mult Image", multed_img)
cv2.waitKey(0)

subed_img= cv2.subtract(img, M)
cv2.imshow("Subtract Image", subed_img)
cv2.waitKey(0)

cv2.destroyAllWidows()