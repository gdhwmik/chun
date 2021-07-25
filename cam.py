import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("hsv_demo", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
