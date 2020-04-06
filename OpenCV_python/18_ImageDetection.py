import  cv2
import  numpy as np
img = cv2.imread("bharti.jpeg",0)# covert into gray scale image we cant do any operation on image without grayscale..

H, W =img.shape
# extract slop edges
#variablename= cv2.Sobel(img_name, cv2.datatypename, widthpixel, 0, kernal_size=5)
# this is edge detection poor technique
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow("Sobel x img", sobelX)
cv2.waitKey(0)
cv2.imshow("Sobel y img", sobelY)
cv2.waitKey(0)
# combine operation perform...
sobelOR = cv2.bitwise_or(sobelX,sobelY)
cv2.imshow("Sobel Bitwise Or img", sobelOR)
cv2.waitKey(0)
# laplacian technique
# arg---> first is image and second is datatype two arg requrid
lap_imag= cv2.Laplacian(img, cv2.CV_32F)
cv2.imshow("Laplacian img", lap_imag)
cv2.waitKey(0)

# canny edge detection uses gradiant values as thresholds
# no need to given data type its requried two thresholds
# this img detection very efficitve img detected technique
canny_imag= cv2.Canny(img, 10,300)
cv2.imshow("Canny edge img", canny_imag)
cv2.waitKey(0)
cv2.destroyAllWindows()