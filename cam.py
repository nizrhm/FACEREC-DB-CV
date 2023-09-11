#this code will take input, its just for understanding
import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

# makes the cap keep running
while True:
    success, img = cap.read()
    cv2.imshow("Face Attendace", img)
    cv2.waitKey(1)