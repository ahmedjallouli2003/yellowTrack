import cv2 as cv 
from PIL import Image
import numpy as np 

def get_limits(color):
    c=np.uint8([[color]])
    hsvC=cv.cvtColor(c,cv.COLOR_BGR2HSV)

    lowerLimit=hsvC[0][0][0] -10,100,100 
    upeerLimit = hsvC[0][0][0] + 10,255,255

    lowerLimit =np.array(lowerLimit,dtype=np.uint8)
    upeerLimit=np.array(upeerLimit , dtype=np.uint8)

    return lowerLimit,upeerLimit



yellow =[0,255,255]

cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read()
    hsvImage=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lowerLimit,upeerLimit=get_limits(color=yellow)

    mask =cv.inRange(hsvImage,lowerLimit,upeerLimit)
    mask_= Image.fromarray(mask)

    bbox=mask_.getbbox()
    print(bbox)
    if bbox is not None :
        x1,y1,x2,y2 =bbox
        frame=cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()

cv.destroyAllWindows()


