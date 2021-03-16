#!/usr/bin/python
import pyautogui
import random
import time
import keyboard

screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.

# transforms minutes into seconds
def minutes(x):
  return x*60

current_hour = time.gmtime().tm_hour

hours = input('How many hours?')

print("Start")

while time.gmtime().tm_hour < (current_hour + int(hours)):
  # get random seed based on current minute and second
  now = time.time()
  minute = int(now / 60)
  seconds = int(now % 60)
  random.seed(minute*seconds)
  # get new random coordinates
  rand_y = random.randrange(0, screenHeight)
  rand_x = random.randrange(0, screenWidth)
  # check if user wants to quit
  if keyboard.is_pressed('esc'):
    print("Closing program")
    break
  # move cursor
  pyautogui.moveTo(rand_x, rand_y, duration=0.5, tween=pyautogui.easeInOutQuad) 
  # wait before moving on
  time.sleep(minutes(0.03))