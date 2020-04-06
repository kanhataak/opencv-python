import cv2
# create a function
def sketch(img):
    # first we convert video strimmer in gray strem
    ima_gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ima_grayblur =cv2.GaussianBlur(ima_gray,(5,5), 0)
    # canny edge for edge detection you know how is work
    canny_edge = cv2.Canny(ima_grayblur, 10,70)
    # convert black in white because clear output can see..
    ret, mask = cv2.threshold(canny_edge,75, 255,cv2.THRESH_BINARY)
    # return the value of mask variable
    return  mask
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("Our Live Sketch", sketch(frame))
    if cv2.waitKey(1) ==13:
        break
cap.release()
cv2.destroyAllWindows()
