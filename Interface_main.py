import keyboard
import cv2 as cv
import utils
from world import World, load_level
from player import Player
from enemies import Ghost
from particles import Trail
from projectiles import Bullet, Grenade
from button import Button
from texts import Text, Message, BlinkingText, MessageBox
import Object
from utils import scale_image, blit_rotate_center, blit_text_center
import math

interface_background = cv.imread("E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/interface_background.png")
Space_Invader = cv.imread("E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/space_invader_back.png")
Car_Racer = cv.imread("E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/car_racer_back.png")
Air_Fighter = cv.imread("E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/Air_fighter_back.jpg")
Ghost_Buster = cv.imread("E:/Extra Codes/Python/Python Projects/Champion-zone-with-AI/Images_project/ghost_busters_back.jpg")
game = ''

count,temp = 1, 0

while count != 0:

    if keyboard.is_pressed('s'):
        game = "Space_Invader"
        temp = 1
        cv.destroyAllWindows()
        cv.imshow("Image", Space_Invader)
        cv.waitKey(1)
    elif keyboard.is_pressed('c'):
        game = "Car_Racer"
        temp = 1
        cv.destroyAllWindows()
        cv.imshow("Image", Car_Racer)
        cv.waitKey(1)
    elif keyboard.is_pressed('g'):
        game = "Ghost_Buster"
        temp = 1
        cv.destroyAllWindows()
        cv.imshow("Image", Ghost_Buster)
        cv.waitKey(1)
    elif keyboard.is_pressed('a'):
        game = "Air_Fighter"
        temp = 1
        cv.destroyAllWindows()
        cv.imshow("Image", Air_Fighter)
        cv.waitKey(1)

    else:
        if temp == 0:
            cv.imshow("Image", interface_background)

    count += 1
    if count % 20000 == 0: 
        if game=="Space_Invader":
            exec(open("E:\Extra Codes\Python\Python Projects\Champion-zone-with-AI\Space Invader\main.py").read())
        elif game == 'Car_Racer':
            exec(open("E:\Extra Codes\Python\Python Projects\Champion-zone-with-AI\Car Racer\main.py").read())
        elif game == 'Air_Fighter':
            exec(open("E:\Extra Codes\Python\Python Projects\Champion-zone-with-AI\Aeroblaster_Pygame-1\main.py").read())
        elif game == 'Ghost_Buster':
            exec(open("E:\Extra Codes\Python\Python Projects\Champion-zone-with-AI\Ghosterbuster_Pygame-2\main.py").read())


    if temp == 0:
        cv.waitKey(0)
        cv.destroyAllWindows()
