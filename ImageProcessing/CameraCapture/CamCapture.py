# -*- coding: utf-8 -*-
"""
Created on Wed April 26 12:35:02 2021

@author: beste
"""

import cv2
import datetime
import os
import shutil
pic_path = "CameraCapture/Pictures"
vid_path = "CameraCapture/Videos"

def cap_picture():
    if not os.path.exists("Pictures"):
        os.makedirs("Pictures")
        
    file = os.listdir(pic_path)
    last_image = file[-1]
        
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("camera does not turn on")
        # exit()
    saves=int(last_image[3:4]) +1
    counter = 1    
    
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("picture", frame)
            if cv2.waitKey(1) & 0xFF == ord("s"):  
                if counter % 1 == 0:
                    img = "IMG"+ str(saves)+".jpg"
                    cv2.imwrite(pic_path+ "/" +img,frame)
                    saves += 1
                counter += 1   
            elif len(os.listdir(pic_path)) == 50 : 
                print("Too much pictures were recorded. For capture, please delete a picture.")
                break
                    
            elif cv2.waitKey(1) & 0xFF == ord("q"):
                break            
    cap.release()
    cv2.destroyAllWindows()
    
# cap_picture()

def cap_video():
    if not os.path.exists("Videos"):
        os.makedirs("Videos")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("camera does not turn on")
        exit()
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    heigth = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    i=0
    if i in range(30) :
        # video_name = "video"+ str(i) +".mp4"
        # int(i)
        # i=i+1
        video_name = "Video_{0}.mp4".format(datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))
    else: 
        print("Too much videos were recorded. For capture, please delete a video.")
        
    writer = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*"XVID"),20,(width, heigth))
    
    while True:
        ret, frame = cap.read()
        cv2.imshow("video",frame)
        writer.write(frame)
        if cv2.waitKey(1) &0xFF == ord("q"): break
    
    cap.release()
    writer.release()
    shutil.move(video_name,vid_path+"/"+video_name)
    cv2.destroyAllWindows()

# cap_video()        

def captureWithTimer():
    if not os.path.exists(pic_path):
        os.makedirs(pic_path)
        
    file = os.listdir(pic_path)
    last_image = file[-1]
    counter = 1
    saves = int(last_image[3:4]) +1
    second = input("please enter sec (max 80 sec):\n") 
    second = int(second)
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        if success:
            if counter % 1 == 0 :
                cv2.imwrite(pic_path + "/IMG_" + str(saves) + ".png", img)
                saves += 1
            counter += 1
            second -= 1
            if second == 0:    break
    cap.release()
    cv2.destroyAllWindows()
# captureWithTimer()


            
            
            