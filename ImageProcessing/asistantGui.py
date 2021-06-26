# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 20:18:03 2021

@author: beste
"""
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog
import cv2
import os
from time import strftime, localtime
from CameraCapture import CamCapture as cam, PhotoEditor as ed, Effects as effect
from FaceRecognition import FaceRecognization as recog
# import FaceRecognition.CascadeTraining as cas

    
root=Tk()
root.title("Asistant Interface")
asistantGui=Frame(root)
# root.tk_setPalette("white")

camera=Frame(root)
gallery=Frame(root)
video=Frame(root)
editor=Frame(root)
faceRecog=Frame(root)
objectTracking=Frame(root)

for frame in (asistantGui, gallery, video, editor, camera, faceRecog, objectTracking):
    frame.place(relx = 0, rely = 0, relheight=1, relwidth=1)
    
def raise_frame(frame):
    frame.tkraise()
    
#--------------------------------------Main(asistantGui)--------------------------------------------

Label(asistantGui,text="Welcome", font = "Times 18 bold italic").place(relx = 0.45, rely = 0.1)

galIcon = ImageTk.PhotoImage(file=r"icons\gallery.png")
Button(asistantGui,text='gallery',image = galIcon, bg="white", command=lambda:raise_frame(gallery)).place(relx = 0.55, rely = 0.3, relheight=0.10, relwidth=0.2)

vidIcon = ImageTk.PhotoImage(file=r"icons\videos.png")
Button(asistantGui,text='video', image = vidIcon, bg="white", command=lambda:raise_frame(video)).place(relx = 0.25, rely = 0.5,  relheight=0.10, relwidth=0.2)

edIcon = ImageTk.PhotoImage(file=r"icons\editor.png")
Button(asistantGui,text='editor', image = edIcon, bg="white", command=lambda:raise_frame(editor)).place(relx = 0.55, rely = 0.5, relheight=0.10, relwidth=0.2)

camIcon = ImageTk.PhotoImage(file=r"icons\camera.png")
Button(asistantGui,text='Camera', image = camIcon, bg="white", command=lambda:raise_frame(camera)).place(relx = 0.25, rely = 0.3, relheight=0.10, relwidth=0.2)

objIcon = ImageTk.PhotoImage(file=r"icons\track.png")
Button(asistantGui,text='Object Tracking',image = objIcon, bg="white", command=lambda:raise_frame(objectTracking)).place(relx = 0.55, rely = 0.7, relheight=0.10, relwidth=0.2)

regIcon = ImageTk.PhotoImage(file=r"icons\faceRecognition.png")
Button(asistantGui,text='Face Recognition',image = regIcon, bg="white", command=lambda:raise_frame(faceRecog)).place(relx = 0.25, rely = 0.7, relheight=0.10, relwidth=0.2)

time = strftime("%D %H:%M", localtime())
Label(asistantGui,text=time,font = "Times", bg= "gray").place(relx = 0, rely = 0.95, relheight=0.05, relwidth=1)

# Label(asistantGui, text=time.strftime("%H:%M",time.localtime()).place(relx = 0.9, rely = 0.9)

    
#------------------------------------------Camera--------------------------------------------------

Label(camera,text="Camera", font = "Times 18 bold italic").place(relx = 0.45, rely = 0.04)

btnIcon = ImageTk.PhotoImage(file=r"icons\lens.jpg")
Button(camera,image = btnIcon, command=lambda:openCam()).place(relx = 0.45, rely = 0.85)
Button(camera,text='Black White Effect', command=lambda:effect.blackWhite()).place(relx = 0.28, rely = 0.87)
Button(camera,text='Blurring Effect', command=lambda:effect.blurring()).place(relx = 0.55, rely = 0.87)

sungIcon = ImageTk.PhotoImage(file=r"icons\sunglasses.png")
Button(camera,text='Glasses Mask', image=sungIcon).place(relx = 0.68, rely = 0.87)
Label(camera,text="   ", bg= "gray").place(relx = 0.1, rely = 0.1, relheight=0.7, relwidth=0.8)
Frame(camera, bg= "white").place(relx = 0.15, rely = 0.15, relheight=0.6, relwidth=0.7)

def openCam():
    frame = cam.cap_picture()
    images = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    Label(camera, image = img).place(relx = 0.15, rely = 0.15, relheight=0.6, relwidth=0.7)
    # Label.ImageTk= img

Button(camera,text='prev', command=lambda:raise_frame(asistantGui)).place(relx = 0.05, rely = 0.04)

#-------------------------------------------Gallery--------------------------------------------------

Label(gallery,text="Gallery", font = "Times 18 bold italic").place(relx = 0.45, rely = 0.01)
Frame(gallery, bg= "white").place(relx = 0, rely = 0.15, relheight=0.9, relwidth=1)
Scrollbar(gallery).place(relx = 0.975, rely = 0.01, relheight=1)

def photos(): 
    images=[]
    num=0
    for img in os.listdir("CameraCapture/Pictures"):
        im = "CameraCapture/Pictures/" + img
        images.append(im)
        num += 1
    return images
    
def display():
    pic = photos()
    pic1 = ImageTk.PhotoImage(file=pic[0])
    Label(gallery, image= pic1, bg= "white").place(relx=0.03, rely =0.16, relheight= 0.35, relwidth= 0.28)
    
    pic2 = ImageTk.PhotoImage(file=pic[1])
    Label(gallery, image= pic2, bg= "white").place(relx=0.35, rely =0.16, relheight= 0.35, relwidth= 0.28)
    
    pic3 = ImageTk.PhotoImage(file=pic[2])
    Label(gallery, image= pic3, bg= "white").place(relx=0.67, rely =0.16, relheight= 0.35, relwidth= 0.28)
    
    pic4 = ImageTk.PhotoImage(file=pic[3])
    Label(gallery, image= pic4, bg= "white").place(relx=0.03, rely =0.53, relheight= 0.35, relwidth= 0.28)
    
    pic5 = ImageTk.PhotoImage(file=pic[4])
    Label(gallery, image= pic5, bg= "white").place(relx=0.35, rely =0.53, relheight= 0.35, relwidth= 0.28)
    
    pic6 = ImageTk.PhotoImage(file=pic[5])
    Label(gallery, image= pic6, bg= "white").place(relx=0.67, rely =0.53, relheight= 0.35, relwidth= 0.28)
    
    pic7 = ImageTk.PhotoImage(file=pic[6])
    Label(gallery, image= pic7, bg= "white").place(relx=0.03, rely =0.9, relheight= 0.35, relwidth= 0.28)
    
    # pic8 = ImageTk.PhotoImage(file=pic[7])
    # Label(gallery, image= pic8, bg= "white").place(relx=0.35, rely =0.9, relheight= 0.35, relwidth= 0.28)
    
    # pic9 = ImageTk.PhotoImage(file=pic[8])
    # Label(gallery, image= pic9).place(relx=0.67, rely =0.9, relheight= 0.35, relwidth= 0.28)

        
# photos()
Button(gallery,text='refresh', command=lambda:display()).place(relx = 0.46, rely = 0.07)

Button(gallery,text='prev', command=lambda:raise_frame(asistantGui)).place(relx = 0.05, rely = 0.04)


#----------------------------------------------Video----------------------------------------------------

Label(video,text="Video Record", font = "Times 18 bold italic").place(relx = 0.43, rely = 0)
Button(video,text='Start Recording', command=lambda:cam.cap_video()).place(relx = 0.45, rely = 0.9)
# Frame(video, bg= "white").place(relx = 0.25, rely = 0.15, relheight=0.6, relwidth=0.5)
LabelFrame(video, bg= "gray").place(relx = 0.2, rely = 0.1, relheight=0.7, relwidth=0.6)
Label(video,text="   ", bg= "white").place(relx = 0.25, rely = 0.15, relheight=0.6, relwidth=0.5)


Button(video,text='prev', command=lambda:raise_frame(asistantGui)).place(relx = 0.05, rely = 0.04)

#----------------------------------------------Editor---------------------------------------------------

Label(editor,text="Photo Editor", font = "Times 18 bold italic").place(relx = 0.42, rely = 0)

folIcon = ImageTk.PhotoImage(file=r"icons\img.png")
# Label(editor, image = folIcon).place(relx = 0.45, rely = 0.13)
Button(editor,text='Select photo', command=lambda:selectPhoto()).place(relx = 0.45, rely = 0.1)
Button(editor,text='Crop & Resize', command=lambda:resizeCrop()).place(relx = 0.5, rely = 0.9)
Button(editor,text='Edit', command=lambda:edit()).place(relx = 0.4, rely = 0.9)
Button(editor,text='Save', command=lambda:save()).place(relx = 0.45, rely = 0.9)
# Label(editor, bg= img).place(relx = 0.25, rely = 0.15, relheight=0.6, relwidth=0.5)

Button(editor,text='prev', command=lambda:raise_frame(asistantGui)).place(relx = 0.05, rely = 0.04)


def selectPhoto():
    img = filedialog.askopenfilename()
    print(img[50:])
    # img = Image.open("CameraCapture/Pictures/" + img[73:])
    im = ImageTk.PhotoImage(file=img[50:])
    Label(editor, image= im, bg = "white").place(relx = 0.2, rely = 0.2, relheight=0.6, relwidth=0.6)


def edit():
    img = selectPhoto()
    print("path:",img)
    if img is None:
        print("Photo can not selected")
        pass
    else:
        ed.edit(img)
        img = Image.open(img)
        img = ImageTk.PhotoImage(img)
        Label(image=img).place(relx=0.2, rely=0.25, relheight=0.7,relwidth=0.7)

def resizeCrop():
    img = selectPhoto()
    if img is None:
        print("Photo can not selected")
        pass
    else:
        ed.resizeAndCrop(img)
    
def save():
    pass


#------------------------------------------Face Recognition-----------------------------------------------

Label(faceRecog,text="Face Recognition", font = "Times 18 bold italic").place(relx = 0.40, rely = 0)
Label(faceRecog,text="Only 2 faces can be registered.").place(relx = 0.40, rely = 0.1)
Label(faceRecog,text="The camera will open. Please slightly turn left, right, zoom in and out of the camera with your face.").place(relx = 0.2, rely = 0.15)
Label(faceRecog,text="Now we need your photos (600 total). This may take a while...\n").place(relx = 0.30, rely = 0.2)
Label(faceRecog,text="   ", bg= "gray").place(relx = 0.25, rely = 0.25, relheight=0.55, relwidth=0.5)
Button(faceRecog,text='Recognize', command= lambda:recog.faceDetector()).place(relx = 0.4, rely = 0.85)
Button(faceRecog,text='Register').place(relx = 0.52, rely = 0.85) #, command= lambda:cas

Button(faceRecog,text='prev', command=lambda:raise_frame(asistantGui)).place(relx = 0.05, rely = 0.04)


#------------------------------------------Object Tracking-------------------------------------------------

Label(objectTracking,text="Object Tracking", font = "Times 18 bold italic").place(relx = 0.4, rely = 0)
Label(objectTracking,text="   ", bg= "gray").place(relx = 0.25, rely = 0.15, relheight=0.6, relwidth=0.5)

Button(objectTracking,text='prev', command=lambda:raise_frame(asistantGui)).place(relx = 0.05, rely = 0.04)



raise_frame(asistantGui)

root.geometry("1000x800")
# root.tk_setPalette("white")
root.resizable(width=True, height=True)
root.mainloop()
