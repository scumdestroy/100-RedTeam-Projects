import pyautogui
import time

# `moveTo` moves mouse to a specific spot
pyautogui.moveTo(100, 100, duration=2)

# `move` moves it relative to its current position
pyautogui.move(100, 0, duration=1)
pyautogui.move(0, 100, duration=1)

# clicky-clicky
pyautogui.click()
pyautogui.doubleClick()
pyautogui.rightClick()


# naptime
time.sleep(666)
