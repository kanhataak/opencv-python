# How to image smooting in opencv lib...
import  cv2
img = cv2.imread("bharti.jpeg")
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# Averaging done by convolving the image with a normalize box filter
#This takes the pixels under the box and replace the central element
# Box size needs to odd and positive
# --------------------- Applying image filter's on the Image --------
blurImg = cv2.blur(img,(7,7))
cv2.imshow("blur Image", blurImg)
cv2.waitKey(0)

# Insted of using box filter use gaussian kernel this is more effictive campare to blur...
gaussionImg = cv2.GaussianBlur(img, (5,5),0)
cv2.imshow("gaussion Image", gaussionImg)
cv2.waitKey(0)
# take median of all the pixels under kernel area and central.
# Elenent is replaced with this median value
# more efficent campare to above two(blur and gaussionBlur)
# find out the average of set to keep center apply the every pixel...
medianImg = cv2.medianBlur(img, 9)
cv2.imshow("median Image", medianImg)
cv2.waitKey(0)

# Bitateral is very effective in nose removal
# very useful filter campare to another...
# A bilateral filter is used for smoothening images and reducing noise, while preserving edges
# bilateralFilter(src, dst, d, sigmaColor, sigmaSpace, borderType)
"""
This method accepts the following parameters −
src − A Mat object representing the source (input image) for this operation.
dst − A Mat object representing the destination (output image) for this operation.
d − A variable of the type integer representing the diameter of the pixel neighborhood.
sigmaColor − A variable of the type integer representing the filter sigma in the color space.
sigmaSpace − A variable of the type integer representing the filter sigma in the coordinate space.
borderType − An integer object representing the type of the border used.
"""
bilaterlImg = cv2.bilateralFilter(img, 5,50,50)
cv2.imshow("Bitateral Image", bilaterlImg)
cv2.waitKey(0)
cv2.destroyAllWindows()