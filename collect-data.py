# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 08:11:37 2021

@author: dell
"""

import cv2
import numpy as np
import os

#creating the directory structures
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    
    os.makedirs("data/test/0")
    os.makedirs("data/test/1")
    os.makedirs("data/test/2")
    os.makedirs("data/test/3")
    os.makedirs("data/test/4")
    os.makedirs("data/test/5")
    

#train or test
mode = 'test'
directory = 'data/'+ mode +'/'

cap=cv2.VideoCapture(0)

while True:
    _, frame=cap.read()
    
    #getting count of exixting images
    count = {'zero': len(os.listdir(directory+"/0")),
             'one': len(os.listdir(directory+"/1")),
             'two': len(os.listdir(directory+"/2")),
             'three': len(os.listdir(directory+"/3")),
             'four': len(os.listdir(directory+"/4"))
             
             
        }
    
    #printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10,50),cv2.FONT_HERSHEY_PLAIN,1,(0,255,255),1)
    cv2.putText(frame, "IMAGE COUNT : "+mode, (10,100),cv2.FONT_HERSHEY_PLAIN,1,(0,255,255),1)
    cv2.putText(frame, "ZERO : "+str(count['zero']),(10,120),cv2.FONT_HERSHEY_PLAIN,1,(0.255,255),1)
    cv2.putText(frame, "ONE : "+str(count['one']),(10,140),cv2.FONT_HERSHEY_PLAIN,1,(0.255,255),1)
    cv2.putText(frame, "TWO : "+str(count['two']),(10,160),cv2.FONT_HERSHEY_PLAIN,1,(0.255,255),1)
    cv2.putText(frame, "THREE : "+str(count['three']),(10,180),cv2.FONT_HERSHEY_PLAIN,1,(0.255,255),1)
    cv2.putText(frame, "FOUR : "+str(count['four']),(10,200),cv2.FONT_HERSHEY_PLAIN,1,(0.255,255),1)
    
    
    #coordinates of the ROI
    x1=int(0.5*frame.shape[1])
    y1=10
    x2=frame.shape[1]-10
    y2=int(0.5*frame.shape[1])
    
    #drawing the ROI
    #increment/decrement by 1 is to compensate the bounding box
    cv2.rectangle(frame,(x1-1,y1-1),(x2+1,y2+1),(255,0,0),1)
    #extracting the ROI
    roi=frame[y1:y2,x1:x2]
    roi=cv2.resize(roi,(250,250))
    
    cv2.imshow("Frame",frame)
    
    
    #doing the preprocessing after capturing the image
    roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi,200,255,cv2.THRESH_BINARY)
    cv2.imshow("ROI",roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF ==27: #esc key
        break
    
    if interrupt & 0xFF==ord('0'):
        cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg',roi)
    
    if interrupt & 0xFF==ord('1'):
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg',roi)
    
    if interrupt & 0xFF==ord('2'):
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg',roi)
    
    if interrupt & 0xFF==ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg',roi)
    
    if interrupt & 0xFF==ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg',roi)
    
    
        
    
    
cap.release()
cv2.destroyAllWindows()

    
    
    
    

    
    
    