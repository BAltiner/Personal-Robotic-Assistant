os.listdir("C:/Users/beste/Desktop/EngiDesign/ImageProcessing/CameraCapture/Pictures")# -*- coding: utf-8 -*-
"""
Created on Thu April 15 18:42:35 2021

@author: Beste

"""

# fotograf yukleme ile algilama
import cv2
import os
import shutil
# import time

personNames = []
face_detection_cascade = cv2.CascadeClassifier("DefaultFaceDetect/haarcascade_frontalface_default.xml")

path = input("creating for who? ")
person = path
path = path + "_Positives"
countSave = 0
knownPersonNames =[]
#cap = cv2.VideoCapture(0)

def saveDataSets():
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("This name is already registered..")

def makeDatasetForCascade():
    # time.sleep(0.05)
    cap = cv2.VideoCapture(0)
    count = 0
    countSave = 1 
    # countSave = PositiveNum
    while True:
        success, face = cap.read()
        if success:
            cv2.imshow("Photo Shoot", face)
            face_det = face_detection_cascade.detectMultiScale(face, minNeighbors = 7)
            for (x,y,w,h) in face_det:
                if count % 5 == 0 :
                    cv2.imwrite(path + "/" + str(countSave) + ".jpg", face)
                    print(countSave)
                    countSave += 1
                count += 1
            # cv2.imshow("Photo Shoot", face)
            if countSave == 1001:    break
    cap.release()
    cv2.destroyAllWindows()
#makeDatasetForCascade()  

def resizeN():
    for file in os.listdir("Negatives"):
        img = cv2.imread("Negatives/" + file)
        img = cv2.resize(img, (100,100))
        # img = cv2.imwrite("Negatives/" + file, img)
 
def getNegative():
    if not os.path.exists('Negatives'):
        os.makedirs('Negatives')
        print("Negative dataset do not exist..")
        
    resizeN()
    
    for file in os.listdir("Negatives"):
        img_path = "Negatives/" + file + "\n"
        with open("bg.txt", "a") as f:
            f.write(img_path)
#getNegative()

def resizeP():
     for file in os.listdir(path):
        img = cv2.imread(path+"/" + file)
        img = cv2.resize(img, (50,50))
        # img = cv2.imwrite(path+"/" + file, img)

def getPositive():
    if not os.path.exists(path):
        os.makedirs(path)
        makeDatasetForCascade()
    else:   
        print("Positive file is already exists.")
        
    resizeP()
        
    for file in os.listdir(path): #information file
        img = cv2.imread(path+"/"+file)
        img = cv2.resize(img, (50,50))
        posDat = path + "/" + file + " 1 0 0 50 50\n"
        #1-numberOfObject 
        with open("pos.dat", "a") as f:
            f.write(posDat)
            
    for file in os.listdir(path):
        img = cv2.imread(path+"/"+file)
        img = cv2.resize(img, (50,50))
        # print(img.shape)
        posDat = path + "/" + file + " 1 0 0 50 50\n"
        with open("pos.txt", "a") as f:
            f.write(posDat)
            
def createVec():
    command1 = "opencv_createsamples.exe -vec pos.vec -bg bg.txt -num 1000 -info pos.dat -w 24 -h 24" 
    os.system(command1)
            
def SaveCreatedCascades():
    if not os.path.exists("Classiffiers"):
        os.makedirs("Classiffiers")
        #yaratılan xml leri kaydet 
        
def clean():
    # if os.path.exists(path):
    #     os.removedirs(path)
    if os.path.exists("pos.dat"): 
        os.removedirs("pos.dat")
    elif os.path.exists("pos.vec"):
        os.removedirs("pos.vec")
    elif os.path.exists("bg.txt"):
        os.removedirs("bg.txt")
    elif os.path.exists("Classiffiers"):  #elif
        for f in os.listdir("Classiffiers"):
            os.remove(os.path.join("Classiffiers",f))
    else:
        print("Error occured..")

def createCascade():
    print("\nNow we need your photos (1000 total). This may take a while...\n")
    getPositive()
    getNegative()
    createVec()
    SaveCreatedCascades()
    print("Your face is being define..")
    personNames.append(person)
    command3 = "opencv_traincascade.exe -data Classiffiers -vec pos.vec -bg bg.txt -numPos 1000 -numNeg 300 -numStages 10  -featureType HAAR -minHitRate 0.999 -maxFalseAlarmRate 0.4 -w 24 -h 24"
    # 1000-300 also okey
    os.system(command3)
    print("Cascade creating is done successfully.")
    if os.path.exists("Classiffiers/cascade.xml"):
        shutil.move("Classiffiers/cascade.xml", "CreatedCascades/" + person + "_cascade.xml")
        clean()
    else:
        print("Cascade is can not created. Please try again..")
        clean()
    knownPersonNames.append(person)


createCascade()
