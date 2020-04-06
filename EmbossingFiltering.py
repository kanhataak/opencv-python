# Embossing
# An embossing filter will take an image and convert it into an embossed image.
# We basically take each pixel and replace it with a shadow or a highligh
import cv2
import numpy as np

img_emboss_input = cv2.imread('image.jpg')

# generating the kernels
kernel_emboss_1 = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])
kernel_emboss_2 = np.array([[-1,-1,0],
                            [-1,0,1],
                            [0,1,1]])
kernel_emboss_3 = np.array([[1,0,0],
                            [0,0,0],])

sharpend_1 = cv2.filter2D(img_emboss_input, -1, kernel_emboss_1)
sharpend_2 = cv2.filter2D(img_emboss_input, -1, kernel_emboss_2)
sharpend_3 = cv2.filter2D(img_emboss_input, -1, kernel_emboss_3)

cv2.imshow("image sharpening_1", sharpend_1)
cv2.imshow("image sharpening_2", sharpend_2)
cv2.imshow("image sharpening_3", sharpend_3)
cv2.waitKey(0)
cv2.destroyAllWindows()
