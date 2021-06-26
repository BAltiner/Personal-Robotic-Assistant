# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:27:00 2021

@author: beste
"""
import cv2 
import os
import numpy as np
path = "CameraCapture/Pictures"

def blurring():
    
    cap = cv2.VideoCapture(0)
    file = os.listdir(path)
    last_image = file[-1]
    counter = 1
    saves = int(last_image[3:4]) +1
    
    while True:
        
        success, frame = cap.read()
        
        if success:
            
            frame = cv2.medianBlur(frame, ksize = 9)
            if cv2.waitKey(1) & 0xFF == ord("s"):
                if counter % 5 == 0 :
                    cv2.imwrite(path + "/IMG" + str(saves) + ".jpg", frame)
                    saves += 1
                counter += 1
                
                if len(os.listdir(path)) >= 50 : 
                    print("Too much pictures were recorded. For capture, please delete a picture.")
                    break
            if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                
            cv2.imshow("Blur Effect", frame)
    cap.release()
    cv2.destroyAllWindows()
# blurring()    


def blackWhite():
    
    cap = cv2.VideoCapture(0)
    file = os.listdir(path)
    last_image = file[-1]
    counter = 1
    saves = int(last_image[3:4]) +1
    
    while True:
        
        success, frame = cap.read()
        
        if success:
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if cv2.waitKey(1) & 0xFF == ord("s"):
                if counter % 5 == 0 :
                    cv2.imwrite(path + "/IMG" + str(saves) + ".jpg", frame)
                    saves += 1
                counter += 1
                
                if len(os.listdir(path)) >= 50 : 
                    print("Too much pictures were recorded. For capture, please delete a picture.")
                    break
            if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                
            cv2.imshow("Blur Effect", frame)
    cap.release()
    cv2.destroyAllWindows()
# blackWhite()










