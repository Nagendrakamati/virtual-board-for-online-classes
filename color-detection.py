import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

def empty(a):
    pass
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("Hue Min","HSV",0,179,empty)
cv2.createTrackbar("Sat Min","HSV",110,255,empty)
cv2.createTrackbar("Val Min","HSV",153,255,empty)
cv2.createTrackbar("Hue Max","HSV",19,179,empty)
cv2.createTrackbar("Sat Max","HSV",240,255,empty)
cv2.createTrackbar("Val Max","HSV",255,255,empty)

while True:
    _,img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "HSV")
    h_max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_min = cv2.getTrackbarPos("Val Min", "HSV")
    v_max = cv2.getTrackbarPos("Val Max", "HSV")
    print(h_min)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    mask=cv2.inRange(imgHsv,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hStack=np.hstack([img,mask,result])
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) and 0xFF == ord('q'):
         break
cap.release()
cv2.destroyAllWindows()


    # cv2.imshow("Original",img)
    # cv2.imshow("HSV",imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", imgResult)

    # imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    # cv2.imshow("Stacked Images", imgStack)
    # cv2.waitKey(1)
