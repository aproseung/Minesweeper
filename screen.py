import pyautogui
import cv2
import os
import time
import numpy as np

base_path = "C:/Minesweeper/data/cell/"
cell_types = ["unknown", "empty", "one", "two", "three", "four", "five", "six", "seven", "eight", "mine"]

class ScreenHandler:
    def __init__(self):
        self.base_path = "C:/Minesweeper/data/cell/"
        self.cell_types = ["unknown", "empty", "one", "two",
                           "three", "four", "five", "six",
                           "seven", "eight", "mine"]
        self.board = None
        self.cell_w = 0
        self.cell_h = 0
        self.ROI = None

    def create_board(self):
        _screen = np.array(pyautogui.screenshot())
        screen = cv2.cvtColor(_screen, cv2.COLOR_BGR2GRAY)

        template = cv2.imread(base_path + "unknown.png", cv2.IMREAD_GRAYSCALE)
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)

        threshold = 0.95
        loc = np.where(res >= threshold)
        if len(loc[0]) == 0 or len(loc[1]) == 0:
            raise ValueError("No matching board region found. Check the template or screen.")
        rows = len(set(loc[0]))
        cols = len(set(loc[1]))
        print(f"Detected board size: {rows} rows x {cols} cols")
        self.board = np.ones((rows, cols)) * (-1)
        self.ROI = [min(loc[1]), min(loc[0]), max(loc[1]), max(loc[0])] # xmin, ymin, xmax, ymax
        self.cell_h, self.cell_w = template.shape

    def update_board(self):
        _screen = np.array(pyautogui.screenshot())
        screen = cv2.cvtColor(_screen, cv2.COLOR_BGR2GRAY)

        for idx, _type in enumerate(self.cell_types):
            temp_path = os.path.join(self.base_path, f"{_type}.png")
            template = cv2.imread(temp_path, cv2.IMREAD_GRAYSCALE)
            res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)

            threshold = 0.95
            loc = np.where(res >= threshold)
            for x, y in zip(*loc[::-1]):
                i, j = self.cvt_screen2board(x, y)
                if i < 0 or j < 0 or i >= len(self.board) or j >= len(self.board[0]): continue
                self.board[i, j] = idx - 1

    def cvt_board2screen(self, i, j):
        x = self.ROI[0] + j * self.cell_w + 5
        y = self.ROI[1] + i * self.cell_h + 5
        return x, y

    def cvt_screen2board(self, x, y):
        i = (y - self.ROI[1]) // self.cell_h
        j = (x - self.ROI[0]) // self.cell_w
        return i, j

    @staticmethod
    def click_screen(x, y):
        pyautogui.moveTo(x, y, duration=0.05)
        pyautogui.click(x, y)

if __name__ == "__main__":
    sr = ScreenReader()
    sr.create_board()