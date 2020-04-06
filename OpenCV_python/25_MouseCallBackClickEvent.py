# I will show you how to implement mouse callback functions using OpenCV library and Python coding.
# Steps:
# Create window using cv2.namedWindow()
# Register mouse callback using cv2.setMouseCallback()
# Display Image using cv2.imshow()
# Wait for keyboard button press using cv2.waitKey()
# Exit window and destroy all windows using cv2.destroyAllWindows()
import cv2
import numpy as np

# Create a black image and a window
windowName = 'Drawing'
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(windowName)


# mouse callback function
# x – x coordinate of the mouse event
# y – y coordinate of the mouse event
# flags – Specific condition whenever a mouse event occurs
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 40, (0, 255, 0), -1)
    if event == cv2.EVENT_MBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (0, 0, 255), -1)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 30, (255, 0, 0), -1)

# bind the callback function to window
# Syntex --> cv2.setMouseCallback(windowName, onMouse[, param]) → None
cv2.setMouseCallback(windowName, draw_circle)

def main():
    while (True):
        cv2.imshow(windowName, img)
        if cv2.waitKey(20) == 27:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()