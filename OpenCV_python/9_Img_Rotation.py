# How to image rotation..
import  cv2
img = cv2.imread("bharti.jpeg")
# Extract the Height and width by using shape method...
H, W = img.shape[:2]
# Here we will rotate the matrix, opencv provide a very useful function "getRotationMatrix2D"
# height and width will be half in the tuple format...
# 70 Rotation Angle if we will rotate around 360' till...
# 0.5 is scaling factor this value we can very and changes we can see...
rotation_matrix = cv2.getRotationMatrix2D((W/3,H/3),50, 0.5)

# you will have to apply warpAffine because it is binary image
rotation_img = cv2.warpAffine(img, rotation_matrix,(W, H))

cv2.imshow("Rotated image", rotation_img)
cv2.imshow("Actual Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

