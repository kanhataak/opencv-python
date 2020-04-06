# How to image scaling or resizing and interplotation ...
import  cv2
img = cv2.imread("bharti.jpeg")

cv2.imshow("original img",img) # calling the original img...
cv2.waitKey()


# in opencv a inbuilt function work on interplotation technique
# lets make the size of our image 3/4 of its original size.
img_scaled = cv2.resize(img,None, fx = 0.75, fy = 0.75)
cv2.imshow("scaling Linear interpolaton", img_scaled)
cv2.waitKey()

# lets doubled the size of our image/ incresing the size...
img_double_scaled = cv2.resize(img, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_CUBIC)
cv2.imshow("scaling Cubic interpolaton", img_double_scaled)
cv2.waitKey()

# lets skew the re-sizing by setting exact dimensions...
img_scaled2 = cv2.resize(img, (350, 600), interpolation = cv2.INTER_AREA)
cv2.imshow("scaling Skewed size interpolaton", img_scaled2)
cv2.waitKey()

cv2.destroyAllWindows()