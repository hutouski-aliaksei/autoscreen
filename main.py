from pyautogui import screenshot
from datetime import datetime
from time import sleep

if __name__ == '__main__':
    while True:
        time = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
        filename = time + ".png"
        screenshot(filename)
        sleep(5)
