# image translation ya image display
import  cv2
import  numpy as np
img = cv2.imread("bharti.jpeg")

# Store height and width of image value
# Read Height and width by using shape function...
H, W =img.shape[:2]
print("Img Height value :",H)
print("Img Width value :",W)

quarter_H, quarter_W = H/4, W/4
print("Quarter Height :",quarter_H)
print("Quarter width :",quarter_W)

# we will need a translation matrix

#       |1 0 Tx|  ---> Tx represent x Axis pixel
# TL =   |0 1 Ty|  ---> Ty represent y Axis pixel

#  TL is translation matrix.
# help with numpy create a float32 type matrix...
TL = np.float32([[1, 0, quarter_W],
                 [0, 1, quarter_H]])
print("Translation Matrix value :\n",TL)
# Two type of transformation  first is warpAffine and second is warpNonAffine
# Here we use warpAffine transformation to shift the image
# image W and H Both are linear/ parlor
img_translation = cv2.warpAffine(img, TL,(W,H))
cv2.imshow("Original image",img)
cv2.imshow('Translation image', img_translation)

cv2.waitKey(0)
cv2.destroyAllWindows()