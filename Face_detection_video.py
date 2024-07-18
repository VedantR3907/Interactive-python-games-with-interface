############################################################################################################################################################################

import cv2 as cv
import numpy as np
import face_recognition, cvzone, pyttsx3
import os, time
from PIL import ImageFont, ImageDraw, Image

######################################################################################
# Images and fonts

path = ('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_User')
background_image = cv.imread('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/Background_2.png', cv.IMREAD_UNCHANGED)
font = "E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Fonts/Lobster-Regular.ttf"
loading_page = cv.imread('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/loading_background_2.png')
images = []
Names = []
myList = os.listdir(path)
TotalTime = 17
curtime = time.time()
temp,count,count_destroy,loop_face = 0,0,0,0

######################################################################################
#Looping for the user_Images from the folder

for i in myList:
    curImg = cv.imread(f'{path}/{i}')
    images.append(curImg)
    Names.append(os.path.splitext(i)[0])

print(Names)

######################################################################################
# The voice BOT

def speakNow(command):
    voice = pyttsx3.init()
    voice.say(command)
    voice.runAndWait()

######################################################################################
# Finding the encodings of the image of the user

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]

        encodeList.append(encode)
    return encodeList

encodelistknown = findEncodings(images)
print('Encoding Completed!')

######################################################################################
# Changing the Font Style

def fonts(image, x, y, text, font, color,size):
    font = ImageFont.truetype(font, size)
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x, y),  text, font = font, fill = color)
    return np.array(img_pil)

######################################################################################
# Main

cap = cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while loop_face == 0:
    success, img = cap.read()
    img = cv.flip(img, 1)
    imgs = cv.resize(img, (0,0), None, 0.25, 0.25)
    imgs = cv.cvtColor(imgs, cv.COLOR_BGR2RGB)

    img = cvzone.overlayPNG(img, background_image,[0,0])

    facescurFrame = face_recognition.face_locations(imgs)
    encodecurFrame = face_recognition.face_encodings(imgs,facescurFrame)

    ######################################################################################
    # Matching the encodings with the face on the video

    for encodeFace, faceLoc in zip(encodecurFrame,facescurFrame):
        matches = face_recognition.compare_faces(encodelistknown, encodeFace)
        faceDis = face_recognition.face_distance(encodelistknown, encodeFace)
        
        matchindex = np.argmin(faceDis)
        if matches[matchindex]:
            name = Names[matchindex].upper()

            # Drawing rectangle on outlines of the user face and writing his/her name

            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            cv.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv.FILLED)
            cv.putText(img, name, (x1+6,y2-6), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

            ######################################################################################
            # Redirecting to ahead window after 4-5 seconds

            Time = int(TotalTime-(time.time() - curtime))
            if Time>0:
                img = fonts(img, 600, 590, str(Time), font, (0, 0, 0), 100)
            else:
                if count_destroy == 0:
                    cv.destroyWindow("Image")
                    count_destroy = 1
                img = loading_page
                img = fonts(img, 370, 150, "Loading...", font, (255, 255, 255), 150)
                cv.imshow("Image",img)        
                cv.waitKey(1)
                count += 1
                if count % 5 == 0:
                    speakNow("Welcome" + name)
                if count % 6 == 0:
                    exec(open("E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Interface_main.py").read())
            
            ######################################################################################

        else:
            curtime = time.time()

    if temp == 0:
        cv.imshow("Image",img)
        cv.waitKey(1)
############################################################################################################################################################################