import time
import pyautogui


def SendScript():
    time.sleep(4)
    with open('script.txt') as f:
        lines = f.readlines()
    for line in lines:
        pyautogui.typewrite(line.strip())
        pyautogui.press('enter')


SendScript()
