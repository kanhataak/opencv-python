import  cv2
pic = cv2.imread("pic.png")

cv2.imshow("Actual image", pic)

cv2.waitKey(0)

# convert RGB into grarScale image we need to a variable
gray_img = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

# first will be show actual image "press enter key" then gray scale image will show
cv2.imshow("Gray Scale Image", gray_img)

cv2.waitKey(0)

cv2.destroyAllWindows()

#-------------- Second method of convert gray scale image ------------
pic = cv2.imread("pic.png",0)
cv2.imshow("GrayScale Image", pic)
cv2.waitKey(0)
cv2.destroyAllWindows()