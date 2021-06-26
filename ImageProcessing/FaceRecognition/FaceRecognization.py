# -*- coding: utf-8 -*-
"""
Created on Thu April 15 16:16:08 2021

@author: Beste
"""
import cv2
import os

def faceDetector():

    cap = cv2.VideoCapture(0)
    file = os.listdir("FaceRecognition/CreatedCascades")
    
    cascade_1 = file [0]
    name1 = cascade_1[:-12]
    name1Cascade = cv2.CascadeClassifier("FaceRecognition/CreatedCascades/" + cascade_1)
    
    cascade_2 = file [1]
    name2 = cascade_2[:-12]
    name2Cascade = cv2.CascadeClassifier("FaceRecognition/CreatedCascades/" + cascade_2)
    # face = created_cascade.detectMultiScale(gray, 50, 50)
    
    while True:
        ret, frame = cap.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
        
        if ret:
            face1 = name1Cascade.detectMultiScale(frame, 1.1, 14)
            face2 = name2Cascade.detectMultiScale(frame, 1.1, 14) 
            
            for (x,y,w,h) in face1:
                cv2.putText(frame, name1, (x+10,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 2)
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255), 5)
                print("Hi, "+name1)
                name = name1
                # if (x,y,w,h) in face1:
                #     print("Hi, "+name1)
                #     name = name1
                # else:   continue
            
            for (x,y,w,h) in face2:
                cv2.putText(frame, name2, (x+10,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0), 2)
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255), 5)
                print("Hi, "+name2)
                name = name2
                
                # if (x,y,w,h) in face2:
                #     print("Hi, "+name2)
                #     name = name2
                # else:   continue
            cv2.imshow("Face recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):   break
    cap.release()
    cv2.destroyAllWindows()
    return name
   
faceDetector()