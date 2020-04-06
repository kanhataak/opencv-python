import  cv2

hand = cv2.imread("hand2.jfif",0)
# threshold the hand image so that we get the foreground
#end of line [1] ret value
thresh = cv2.threshold(hand,70 ,255, cv2.THRESH_BINARY)[1]
# get the contours in the thresholded image
coutours,_ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
hull = [cv2.convexHull(c) for c in coutours]

final = cv2.drawContours(hand, hull, -1, (255,0,0))

cv2.imshow("Real Image", hand)
cv2.waitKey(0)
# show the thresholded image
cv2.imshow("Thteshold", thresh)
cv2.waitKey(0)
cv2.imshow("convexhull", final)
cv2.waitKey(0)
# free up memory
cv2.destroyAllWindows()