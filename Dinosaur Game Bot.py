"""
Python bot that plays T-Rex Dino game from Google Chrome offline mode
made by Tiago Taquelim .F , @sikozonpc 14/09/17
"""

import pyautogui as pg
import time
import os
from PIL import ImageGrab, ImageOps
from numpy import array

x = 1366/2
y = 720 / 2

pg.moveTo(280, 400)
pg.click()

def up():
    pg.press("space")
    time.sleep(0.3)
    pg.press("down")

    
# Takes a snapshot of the screen to create the bounding box
# for the event handling, since screen widths/heights varies

def snapshot():
    box = ()
    img = ImageGrab.grab()
    img.save(os.getcwd() + "\\full_snap__" + str(int(time.time())) + ".png", "PNG")
    print("Screenshot took")
    
def boot():
    while 1:
        box = (253, 402, 330, 436)
        # Creates a full snapshot of the screen and returns an RGB image
        img = ImageOps.grayscale(ImageGrab.grab(box))
        a = array(img.getcolors())
        a = int(a.sum())
        time.sleep(0.095)

        # Delete # for debug 
        #print(a)

        
        if (a == 2948 or a == 3203 or a == 3359):
            up()

            # Delete # for debug 
            #print("Jump at" , a)


if __name__ == "__main__":
    intpt = input("1 TO RUN BOT\n2 TO TAKE SNAPSHOT\n")
    print(intpt)
    if (intpt == "1"):
        boot()
        
    if intpt == "2":
        snapshot()



    
