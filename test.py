import pyautogui
import time
time.sleep(3)
count=0
while count<=5:
    pyautogui.typewrite("karthi "+str(count))
    pyautogui.press("Enter")
    count=count+1