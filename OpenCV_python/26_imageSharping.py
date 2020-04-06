# Applying the sharpening filter will sharpen the edges in the image.
# This filter is very useful when we want to enhance the edges in an image that's not crisp
import cv2
import numpy as np
img = cv2.imread("image.jpg")
cv2.imshow("Actual image", img)
cv2.waitKey(0)
# create our sharpening kernel, we dont normalize since the caluies in the matrix sum to 1...
# kre_sharpening = np.array([[-1,-1,-1,-1,-1],
#                            [-1,-1,-1,-1,-1],
#                            [-1,-1,25,-1,-1],
#                            [-1,-1,-1,-1,-1],
#                            [-1,-1,-1,-1,-1],])
# kre_sharpening = np.array([[-1,-1,-1],
#                            [-1,9,-1,],
#                            [-1,-1,-1],])
kre_sharpening = np.array([[1,1,1],
                           [1,-8,1,],
                           [1,1,1],])

# Applying different kernel to the different image...
sharpend = cv2.filter2D(img, -1, kre_sharpening)

cv2.imshow("image sharpening", sharpend)
cv2.waitKey(0)
cv2.destroyAllWindows()

# As you can see in the preceding figure, the level of sharpening depends on the type of kernel we use.
# We have a lot of freedom to customize the kernel here, and each kernel will give you a different kind
# of sharpening. To just sharpen an image, like we are doing in the top right image in the preceding picture...