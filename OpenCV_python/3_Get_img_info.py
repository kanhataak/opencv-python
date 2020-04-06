# How to find image information
import cv2

img = cv2.imread("pic.png")
cv2.imshow("output ", img)

# How to find length, width and how many pixel, Layers in image
# Height, width and layers(RGB)
print(img.shape)# here get info in tuple format because not we can change---> (405, 348, 3)

print("Height pixel values :", img.shape[0])
print("width pixel values :", img.shape[1])
print("Image Layers :", img.shape[2])

cv2.waitKey(0)
cv2.destroyAllWindows()
