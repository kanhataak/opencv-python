import  cv2
import  numpy as np

img = cv2.imread("bharti.jpeg")
cv2.imshow("Original",img)
cv2.waitKey(0)

# create 3x3 kernel matrix..
ker_8x8 = np.ones((8,8), np.float32) / 64

# we use the cv2.filte2D to convolve the kernel with an image....
# cv2.filter2D(image, depthsize, kernelsize)
blurred = cv2.filter2D(img, -1, ker_8x8)
cv2.imshow("Kernel Blurring Img", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()