# Image cropping
import  cv2
img = cv2.imread("bharti.jpeg")
height, width = img.shape[:2]

# Lets get the starting pixel coordinates(top left, cropping rectangle)
startRowValue, startColumnValue = int(height*.10), int(width*.30)
# lets get the ending pixel coordinates(bottom right)
endRowValue, endColumnValue = int(height*.70),int(width*.70)


# above 70\30 redio according to change your cropping area...
# it is not hard and fast rule... you can change your choice...

# here we simply use indexing to crop the image using the list...
# SRW is stating row value initial to ending and SCV is column value where initial to ending Column...
croppedImg = img[startRowValue:endRowValue, startColumnValue:endColumnValue]

cv2.imshow("Original Image",img)
cv2.imshow("Cropped Image", croppedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
