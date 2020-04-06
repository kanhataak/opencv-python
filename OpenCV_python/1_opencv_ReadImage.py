# how to read an image...
import cv2

# here we fatch image but we do not see a image, we will see matrix format
# store the image pixel value im image variable
image=cv2.imread("pic.png")

cv2.imshow("Output Image",image) # frame name " output image"
# waitkey is function that will wait of press any key
cv2.waitKey(0)

cv2.destroyAllWindows()