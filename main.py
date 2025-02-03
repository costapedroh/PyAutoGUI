import pyautogui
from time import sleep

pyautogui.moveTo(976,343, duration=1)

for i in range(700):
    pyautogui.click()
    sleep(0.1)
    
