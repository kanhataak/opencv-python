import  cv2
import  numpy as np # import numpy Lib because we need to create numpy array

pic = cv2.imread("bharti.jpeg")  # reading the image
cv2.imshow("Actual image", pic)  # Show the Actual image
cv2.waitKey(0)

# split the image into B, G, R variable by using the split function
B,G,R = cv2.split(pic)
# Create a zeros matrix array that a same shape
# "np.zeros" this is function of numpy with the help of create a zeros matrix
zeros = np.zeros(pic.shape[:2], dtype="uint8")
# Here we start Extract the image color by using marge function.
# In the first one we have visualized the blue plane...
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
# In the second one we have visualized the green plane...
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.waitKey(0)
# In the threed one we have visualized the red plane...
cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
cv2.waitKey(0)

cv2.destroyAllWindows()