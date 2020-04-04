#library import 
import os
import cv2
import pathlib

#Lists for data 
notVideo = []
video = []
cleanData = []
width = 0
height = 0

for i in os.listdir("D:\Videos"):     #Taking Directory |||||||||||  Need to be Dynamic
    notVideo.append(i)                #Making list of available items
for i in notVideo:                     
    if i[:-5:-1] == "4pm.":            #Filtering the video files ||||||||| Need to add more video format
        video.append(i)               #Contains all the video file type
        notVideo.remove(i)            #Contains all the non video file type
        
initialPath = ("D:\\Videos\\")        #Need to be dynamic

for i in video:                       #Looping through the vidoes
    path = initialPath + i
    print(path)            #Printing the path
    cap = cv2.VideoCapture(path)
    
    if cap.isOpened():                #Getting height and width of the video
        width = cap.get(3)
        height = cap.get(4)
        
    print (int(width), int(height))
    if height == 720:
        cleanData.append(i)
        #os.remove(path)
        
cap.release()
print(cleanData)