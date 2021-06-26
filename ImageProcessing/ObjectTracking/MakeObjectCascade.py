# -*- coding: utf-8 -*-
"""
Created on Thu April 15 18:42:35 2021

@author: beste
"""

import cv2
import os
import shutil

objectNames = []

path = input("creating for what?\n ")
objectName = path
path = path + "_Positives"
countSave = 0
knownObjectNames =[]
#cap = cv2.VideoCapture(0)

def saveDataSets():
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("This name is already registered..")

def makeDatasetForCascade():
    cap = cv2.VideoCapture(0)
    count = 0
    countSave = 1 
    while True:
        success, frame = cap.read()
        if success:
            if count % 5 == 0 :
                cv2.imwrite(path + "/" + str(countSave) + ".jpg", frame)
                print(countSave)
                countSave += 1
            count += 1
        if countSave == 201:    break
    cv2.imshow("Photo Shoot", frame)
    cap.release()
    cv2.destroyAllWindows()
#makeDatasetForCascade()  

def resizeN():
    for file in os.listdir("Negatives"):
        img = cv2.imread("Negatives/" + file)
        img = cv2.resize(img, (100,100))
        img = cv2.imwrite("Negatives/" + file, img)
 
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
        img = cv2.imwrite(path+"/" + file, img)

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
    command1 = "opencv_createsamples.exe -vec pos.vec -bg bg.txt -num 200 -info pos.dat -w 24 -h 24" 
    os.system(command1)
            
def SaveCreatedCascades():
    if not os.path.exists("Classiffiers"):
        os.makedirs("Classiffiers")
        #yaratılan xml leri kaydet 
        
def clean():
    if os.path.exists(path):
        os.removedirs(path)
    elif os.path.exists("pos.dat"): 
        os.removedirs("pos.dat")
    elif os.path.exists("pos.vec"):
        os.removedirs("pos.vec")
    elif os.path.exists("bg.txt"):
        os.removedirs("bg.txt")
    if os.path.exists("Classiffiers"):  #elif
        for f in os.listdir("Classiffiers"):
            os.remove(os.path.join("Classiffiers",f))
    else:
        print("Error occured..")

def createCascade():
    print("\nNow we need objects photos (200 total). This may take a while...\n")
    getPositive()
    getNegative()
    createVec()
    SaveCreatedCascades()
    print("Object is being define..")
    objectNames.append(objectName)
    command3 = "opencv_traincascade.exe -data Classiffiers -vec pos.vec -bg bg.txt -numPos 200 -numNeg 90 -numStages 10  -featureType HAAR -minHitRate 0.999 -maxFalseAlarmRate 0.4 -w 24 -h 24"
    os.system(command3)
    print("Cascade creating is done successfully.")
    if os.path.exists("Classiffiers/cascade.xml"):
        shutil.move("Classiffiers/cascade.xml", "CreatedCascades/" + objectName + "_cascade.xml")
        clean()
    else:
        print("Cascade is can not created. Please try again..")
        clean()
    knownObjectNames.append(objectName)


createCascade()
