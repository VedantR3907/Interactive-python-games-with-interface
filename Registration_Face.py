############################################################################################################################################################################
import cv2 as cv
import speech_recognition, pyttsx3
import face_recognition, cvzone, numpy as np
import os, time
from PIL import ImageFont, ImageDraw, Image

######################################################################################
# Images and fonts

folder = "E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_User/"
image_saved_count,name = [0, 0, 0],''
mute_image = cv.imread("E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/Mute.png")
microphone_image = cv.imread("E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/speak_microphone.png")
loading_background = cv.imread("E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/loading_background_1.png")
background_image = cv.imread('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/Background_1.png', cv.IMREAD_UNCHANGED)
save_image = cv.imread('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/save_image_text.png', cv.IMREAD_UNCHANGED)
wrong_image_not_saved = cv.imread('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/image_not_saved_wrong_main.png', cv.IMREAD_UNCHANGED)
image_saved = cv.imread('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/image_saved_main.png', cv.IMREAD_UNCHANGED)
microphone_registername = cv.imread('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/microphone_registername_main.png', cv.IMREAD_UNCHANGED)
login_rediret = cv.imread('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/login_redirect_main.png', cv.IMREAD_UNCHANGED)
font1 = "E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI//Fonts/DebugFreeTrial-MVdYB.otf"
font2 = "E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Fonts/Lobster-Regular.ttf"
######################################################################################
# Name and Paths

cap = cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

path = ('E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_User')
Names = []
myList = os.listdir(path)
for i in myList:
    Names.append(os.path.splitext(i)[0])

print(Names)

######################################################################################
# Showing Image and Waitkey

def call_image(image):
     cv.imshow("Image",image)
     cv.waitKey(1)

######################################################################################
# Changing Font Style

def fonts(image, x, y, text, font, color, size):
    font = ImageFont.truetype(font, size)
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x, y),  text, font = font, fill = color)
    return np.array(img_pil)

######################################################################################
# The voice BOT

def speakNow(command):
    voice = pyttsx3.init()
    voice.say(command)
    voice.runAndWait()

######################################################################################
# Voice Recognizor of user

def voice_recognizer(check_registery):
        
        success, image = cap.read()
        image[:] = mute_image
        image = fonts(image, 500, 580, "Wait...",font2, (255,255,255), 100)
        call_image(image)

        sr = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
            global name
            print("Silence Now...")
            sr.adjust_for_ambient_noise(source, duration = 2)

            print("Speak Now.....")

            #Image Microphone
            image[:] = microphone_image
            image = fonts(image, 480, 500, "Listening...",font2, (255,255,255), 100)
            call_image(image)
            if check_registery == False:
                speakNow("What's your name?")

            audio2 = sr.listen(source)
            text = sr.recognize_google(audio2)
            text = text.lower()

            if check_registery == False:
                name = text
                print(name)
                speakNow('did you spoke' + text)
                voice_confirm(text)
            else:
                  return text

######################################################################################
# Confirming of Users Name or Restarting

def voice_confirm(command):

            text = voice_recognizer(True)

            if text == "yes":
                if command in Names:
                    speakNow(command + "you are already registered")
                    image_saved_count[2] = 1
                    image_saved_count[0],image_saved_count[1] = 1, 1
                else:
                    speakNow("Welcome " + command + ", Vedant, Manan and Rinkesh Welcomes you to Champion Zone")
            else:
                  speakNow("Please Speak Your Name Again!")
                  voice_recognizer(False)

######################################################################################
#Main Loop

while True:
    ######################################################################################
    # Reading Video, all the logos importing and overlapping
    success, image = cap.read()
    image = cv.flip(image, 1)
    image = cvzone.overlayPNG(image, background_image,[0,0])

    save_image = cv.resize(save_image, (200,200))
    microphone_registername = cv.resize(microphone_registername, (200,200))
    login_rediret = cv.resize(login_rediret, (200,200))
    image = cvzone.overlayPNG(image, save_image, [50,20])
    image = cvzone.overlayPNG(image, microphone_registername, [1000,20])
    image = cvzone.overlayPNG(image, login_rediret, [50,500])

    cv.imshow("Image",image)
    key = cv.waitKey(1)

    ######################################################################################
    # Checking which key user press

    ######################################################################################
    # For Saving the Users Image

    if key == ord("s"):
        image_saved_count[1] = 1
        if sum(image_saved_count[0:2]) != 2:
            
            wrong_image_not_saved = cv.resize(wrong_image_not_saved, (400,400))
            image = cvzone.overlayPNG(image, wrong_image_not_saved, [440,175])
            call_image(image)
            speakNow("please Register your user-name first")
        else:
            cv.imwrite(f'{folder}/{name}.jpg',image[70:650,345:935])   #[100:600,400:900]
            image_saved = cv.resize(image_saved, (400,400))
            image = cvzone.overlayPNG(image, image_saved, [440,175])
            call_image(image)
            speakNow("Image Saved")

    ######################################################################################
    #For Verification of Name of the User

    elif key == ord('v'):
            image_saved_count[0] = 1
            cv.destroyWindow("Image")
            voice_recognizer(False)
    
    ######################################################################################
    # Redirecting to Face recognizar Python File

    elif key == ord('n'):
            if sum(image_saved_count[0:2]) != 2:
                wrong_image_not_saved = cv.resize(wrong_image_not_saved, (400,400))
                image = cvzone.overlayPNG(image, wrong_image_not_saved, [440,175])
                call_image(image)
                speakNow("Please Register or Log-in First")
            else:
                cv.destroyWindow("Image")
                image[:] = loading_background
                image = fonts(image, 410,450, "Welcome " + name.capitalize(), font1, (255,255,255), 80)
                call_image(image)
                if image_saved_count[2] == 1:
                    speakNow("Welcome back " + name)
                else:
                    speakNow("Registeration completed for " + name + "Welcome")
                    
                exec(open("E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Face_detection_video.py").read())
    
    ######################################################################################

############################################################################################################################################################################