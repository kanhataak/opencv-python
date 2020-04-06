import  matplotlib.pyplot as plt
import  cv2
# calling videocapture function
cap = cv2.VideoCapture(0)
# if through the cap variable video editor on so capture the video
if cap.isOpened():
    # read the capture video image
    ret, farme = cap.read()
    # "ret" value print
    print(ret)
    print(farme)
else:
    # if nothing is open then aall the return
    ret = False
img = cv2.cvtColor(farme, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.title("Camera Image One")
# which will be the pixel read then store here
plt.xticks([])
plt.yticks([])
plt.show()

cap.release()