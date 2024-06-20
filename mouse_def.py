import pyautogui
import time 

a = 1

def LKM_mouse_def():
    pyautogui.click(button='left')

def PKM_mouse_def():
    pyautogui.click(button='right')



def left_mouse_def():
    pyautogui.moveRel(-50, 0, duration=0.5)

def right_mouse_def():
    pyautogui.moveRel(50, 0, duration=0.5)

def down_mouse_def():
    pyautogui.moveRel(0, 50, duration=0.5)

def upstairs_mouse_def():
    pyautogui.moveRel(0, -50, duration=0.5)

def block_mouse_def():
    pass




def unlocking_mouse_def():
    pass



