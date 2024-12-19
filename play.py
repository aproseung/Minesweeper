import pyautogui

class Player:
    def __init__(self):
        pass

    def click(self, x, y):
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x, y)