#https://arcadespot.com/game/magic-piano-tiles/
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
#X:  713 Y:  557 RGB: (169, 173, 232)
#X:  845 Y:  571 RGB: (253, 254, 254)
#X:  993 Y:  821 RGB: (255, 255, 255)
#X: 1118 Y:  808 RGB: (153, 158, 230)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('q')==False:
    if pyautogui.pixel(713,500)[0]==0:
        click(713,500)
    if pyautogui.pixel(845,500)[0]==0:
        click(845,500)
    if pyautogui.pixel(993,500)[0]==0:
        click(993,500)
    if pyautogui.pixel(1118,500)[0]==0:
        click(1118,500)
    
    
