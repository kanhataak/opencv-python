# how to write an image
import  cv2 # open cv lib
# read an image using imread function
img = cv2.imread("pic.png")

cv2.imshow("Actual Image", img)
# write an image png fromat
cv2.imwrite("output.png",img)
# write an image jpg format
cv2.imwrite("output2.jpg",img)

# wait for press any key
cv2.waitKey(0)
# close all open window
cv2.destroyAllWindows()
