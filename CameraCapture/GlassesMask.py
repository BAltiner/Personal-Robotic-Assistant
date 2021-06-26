# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:53:41 2021

@author: beste
"""
import cv2
import warnings
warnings.simplefilter("ignore")

pic_path = "Pictures"

def glassesFilter():
    cap = cv2.VideoCapture(0)
    face = cv2.CascadeClassifier("FaceDetect/haarcascade_frontalface_default.xml")
    eye = cv2.CascadeClassifier("FaceDetect/haarcascade_eye.xml")
    
    while True:
        success, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        glasses1 = cv2.imread("Glasses/sunglasses_6.png")
        # glasses2 = cv2.imread("Glasses/Glasses2.jpg")
        saveCount = 1
        if success:
            detect_face = face.detectMultiScale(gray, 1.4, 7)
            
            for (x,y,w,h) in detect_face:
                # cv2.rectangle(frame, (x,y),(x+w, y+h),(255,255,255),10)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                
                eyes = eye.detectMultiScale(roi_gray, 1.5, 5)
                
                for (e_x, e_y, e_w, e_h) in eyes:
                    # cv2.rectangle(roi_color,(e_x,e_y),(e_x+e_w,e_y+e_h),(0,255,0),2)
                    
                    # glasses -> mask
                    glassesResized = cv2.resize(glasses1, (e_w, e_h))
                    glassesGray = cv2.cvtColor(glassesResized, cv2.COLOR_BGR2GRAY) 
                    _, glassesThresh = cv2.threshold(glassesGray, 20, 255, cv2.THRESH_BINARY_INV)
                    # glassesThresh=cv2.cvtColor(glassesThresh, cv2.COLOR_GRAY2BGR)
                    glassesInv = cv2.bitwise_not(glassesThresh)
                    
                    glassesThresh = cv2.resize(glassesThresh,(roi_gray.shape))
                    maskedRoi = cv2.bitwise_and(roi_gray, roi_gray, mask=glassesThresh)
                    
                    glassesResized = cv2.resize(glassesResized,(maskedRoi.shape))
                    maskedRoi=cv2.cvtColor(maskedRoi, cv2.COLOR_GRAY2BGR)
                    final = cv2.add(glassesResized, maskedRoi)
                    
                    g_w, g_h, g_c = glassesResized.shape
                    for i in range(0, g_w):
                        for j in range(0, g_h):
                            if glassesResized[i,j][2] != 0:
                                frame[e_y+i: e_x+j+10] = final[i,j]                                  
                        
                    if cv2.waitKey(1) & 0xFF == ord("s"):                 
                        path = "IMG"+ str(saveCount)+".jpg"
                        cv2.imwrite(pic_path+ "/" +path, frame)
                        saveCount += 1
                 
                    if cv2.waitKey(1) &0xFF == ord("q"): break           
            cv2.imshow("Filter",frame)
    cap.release()
    cv2.destroyAllWindows()
            
glassesFilter()            
            