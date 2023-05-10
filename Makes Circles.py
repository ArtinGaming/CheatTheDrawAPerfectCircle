import pyautogui
import math
import sys
import keyboard
# Radius s
R = 365
# measuring screen size
(x,y) = pyautogui.size()
# locating center of the screen 
(X,Y) = pyautogui.position(x/2,y/2)
# offsetting by radius 
pyautogui.moveTo(X + R,Y)

for i in range(365):
   #settsing pace with a modulus 
   if i % 6.5 == 0:
      pyautogui.mouseDown()
      pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))