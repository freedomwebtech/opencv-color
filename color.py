import numpy as np
import cv2

lower_range = np.array([49,0,0])
upper_range = np.array([86,255,255])

cap = cv2.VideoCapture('lambgreen.avi')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
#    frame1 = cv2.flip(frame, flipCode = -1)




    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_range, upper_range)
    _,mask1 = cv2.threshold(mask, 254,255,cv2.THRESH_BINARY)
    cnts,h = cv2.findContours(mask1,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
 
      
    for c in cnts:
        x = 6000.0
        if cv2.contourArea(c) > x:
           x,y,w,h = cv2.boundingRect(c)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
           cv2.putText(frame,("DETECT"), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,255),2)
        
   
       
    cv2.imshow("Frame", frame);
    key = cv2.waitKey(1) & 0xFF
   
    if key == ord("q"):
       break
