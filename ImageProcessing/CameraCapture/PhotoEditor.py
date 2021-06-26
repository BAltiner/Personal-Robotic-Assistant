# -*- coding: utf-8 -*-
"""
Created on Wed April 28 16:52:11 2021

@author: beste
"""
import cv2
import numpy as np
import os


path = "CameraCapture/Pictures"

def empty(a):pass

def edit(image):
    
    img = cv2.imread(image)
    
    file = os.listdir(path)
    last_image = file[-1]
    saves = int(last_image[3:4]) +1
    
    ksize = (3,3)
    
    cv2.namedWindow("Adjust")
    cv2.resizeWindow("Adjust", 800, 1000)
    cv2.createTrackbar("Blur","Adjust",0,20,empty)
    cv2.createTrackbar("Sharpness","Adjust",0,50,empty)    
    cv2.createTrackbar("Contrast","Adjust",0,50,empty)
    cv2.createTrackbar("Brightness","Adjust",0,50,empty)
    cv2.createTrackbar("BlackWhite","Adjust",0,1,empty)
    
    
    while True:
        # img = cv2.imread("Pictures\catwithhat.jpg")
        # img = cv2.imread("Pictures\Alenna.jpg")
        
        sharpness = cv2.getTrackbarPos("Sharpness","Adjust")
        ksize = cv2.getTrackbarPos("Blur","Adjust")
        contrast = cv2.getTrackbarPos("Contrast","Adjust")
        brightness = cv2.getTrackbarPos("Brightness","Adjust")
        blackWhite = cv2.getTrackbarPos("BlackWhite","Adjust")
        
        # blur
        if ksize % 2 == 0:
            ksize += 1
            img = cv2.medianBlur(img, ksize)
        else :  pass
        
        # img = cv2.medianBlur(img, (-1)*ksize)
        
        #Sharpness      original- gaussianblur
        if sharpness == 0:
            cv2.imshow("Adjust", img)
        else:
            SharphenFilter = (np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])*sharpness)
            img=cv2.filter2D(img,-1,SharphenFilter)
        
        #Contrast
        if contrast == 0:
            pass
        constAlpha = float(130*(contrast+127)) / (127*(130-contrast))
        constGamma = 127*(1-constAlpha)
        img = cv2.addWeighted(img, constAlpha, img, 0, constGamma)
        
        #Brightness
        img = cv2.addWeighted(img, 1.01, img, brightness,0)
        
        #BlackWhite
        if blackWhite == 0:
            pass
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("Adjust", img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        if k == ord("s"):
            img = cv2.imwrite(path + "/IMG" + str(saves) + ".jpg",img)
            saves += 1
        
    cv2.destroyAllWindows()

# edit()    

def resizeAndCrop(image):
    
    img = cv2.imread(image)
    
    file = os.listdir(path)
    last_image = file[-1]
    saves = int(last_image[3:4]) +1
    
    w,h,c = img.shape
    
    cv2.namedWindow("Editor")
    cv2.resizeWindow("Editor", w, h)
    
    
    cv2.createTrackbar("Width","Editor",w,750,empty)
    cv2.createTrackbar("Height","Editor",h,750,empty)
    
    cv2.createTrackbar("CropWidth","Editor",w,800,empty)
    cv2.createTrackbar("CropHeight","Editor",h,800,empty)
    
    while True:
        # img = cv2.imread("Pictures\catwithhat.jpg")
        
        width = cv2.getTrackbarPos("Width","Editor")
        height = cv2.getTrackbarPos("Height","Editor")
        
        w = cv2.getTrackbarPos("CropWidth","Editor")
        h = cv2.getTrackbarPos("CropHeight","Editor")
        
        if width == 0 | height == 0 | w == 0 | h == 0:
            continue
        
        img = cv2.resize(img, (width,height))
        
        img = img[:w,:h]
        
        cv2.imshow("Editor", img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        if k == ord("s"):
            img = cv2.imwrite(path + "/IMG" + str(saves) + ".jpg",img)
            saves += 1
            
        if image is None:
            break
        
    cv2.destroyAllWindows()
    
# resizeAndCrop()
   