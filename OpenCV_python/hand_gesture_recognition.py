# Hand Gesture recognition
import  cv2
import  numpy as np
import math

# "cap" it will be capture the live stream
# open camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # capture frame from the camera
    frame = cap.read()[1]

    #get hand data from the reectangle sub window
    cv2.rectangle(frame, (100, 100),(300,300),(0, 255, 0),0)
    crop_img = frame[100:300, 100:300]

    # apply gaussian blur  ---> kernel value(3x3) this is kernel value
    blur = cv2.GaussianBlur(crop_img, (3,3),0)

    # Bgr to HSV
    HSV = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    # define the lower and upper value
    # filter out the hand/skin color that is pass by HSV
    # Create a binary image with where white will be skin colore and rest is black
    mask = cv2.inRange(HSV, np.array([2,0,0]), np.array([20, 255,255]))

    # kernel for morphological transformation
    kernel = np.ones((5,5))
    # apply morphological transformations to filter out the background noise

    dilation = cv2.dilate(mask, kernel, iterations=2)
    erosion = cv2.erode(dilation, kernel,iterations=2)
    # Gaussian blur and threshold
    filtering = cv2.GaussianBlur(erosion,(3,3),0)
    thresholding = cv2.threshold(filtering, 127, 255, 0)[1]

# showing the threshold image
#     cv2.imshow("Thresholded image", thresholding)

    # finding the contours value
    # (contours, _)= cv2.findContours(thresholding.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    (contours, _) = cv2.findContours(thresholding.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    try:
        # Find contour with maximum area
        contour = max(contours, key=lambda x: cv2.contourArea(x))

        # Create bounding rectangle around the contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(crop_img, (x, y), (x + w, y + h), (0, 0, 255), 0)

        # Find convex hull
        hull = cv2.convexHull(contour)

        # Draw contour
        drawing = np.zeros(crop_img.shape, np.uint8)
        cv2.drawContours(drawing, [contour], -1, (0, 255, 0), 0)
        cv2.drawContours(drawing, [hull], -1, (0, 0, 255), 0)

        # Find convexity defects
        hull = cv2.convexHull(contour, returnPoints=False)
        defects = cv2.convexityDefects(contour, hull)

        # Use cosine rule to find angle of the far point from the start and end point i.e. the convex points (the finger
        # tips) for all defects
        count_defects = 0

        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])

            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14

            # if angle > 90 draw a circle at the far point
            if angle <= 90:
                count_defects += 1
                cv2.circle(crop_img, far, 1, [0, 0, 255], -1)

            cv2.line(crop_img, start, end, [0, 255, 0], 2)

        # Print number of fingers
        if count_defects == 0:
            cv2.putText(frame, "ONE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 1:
            cv2.putText(frame, "TWO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 2:
            cv2.putText(frame, "THREE", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 3:
            cv2.putText(frame, "FOUR", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 4:
            cv2.putText(frame, "FIVE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        else:
            pass
    except:
        pass

    # Show required images
    cv2.imshow("Gesture", frame)
    all_image = np.hstack((drawing, crop_img))
    cv2.imshow('Contours', all_image)

    # observe the keypress by the user
    keypress = cv2.waitKey(1) & 0xFF

    # if the user pressed "q", then stop looping
    if keypress == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


