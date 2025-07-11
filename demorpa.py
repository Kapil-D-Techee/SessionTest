#import os
#from pyvirtualdisplay import Display
import pyautogui
import time
pyautogui.click(100,100)
#pyautogui.doubleclick(200,200)
#pyautogui.drag(300,300, 400,400, duration=1)
#pyautogui.scroll(300)
x,y =pyautogui.position()
print(f'x: {x}, y: {y}') # to get mouse position value
#pyautogui.write('Hello, world!')  # type text at current mouse position
#pyautogui.hotkey('ctrl', 'a')  # selected all text
#pyautogui.hotkey('ctrl', 'c')  # copy selected text

#location = pyautogui.locateOnScreen('copyt_img.jpg',confidence=0.8)  # locate image on screen
#print(location)  # print the location of the image if found
#time.sleep(2)  # wait for 2 seconds
#pyautogui.click(pyautogui.center(location))  # click on center part of the located image
#print(pyautogui.size()) # Get screen size
#ss=pyautogui.screenshot()  # take a screenshot
#ss.save('screenshot.png')  # save the screenshot to a file in currnet directory

# Start virtual display
# Set display number matching xauth

