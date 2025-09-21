from pyautogui import screenshot, hotkey, locateCenterOnScreen, click, moveTo, write
from datetime import datetime
from time import sleep
from helper import run_browser_thread


if __name__ == '__main__':
    interval = int(input("Enter time interval: "))
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    url = "https://dev-mpor.trupanion.com/"
    while True:
        located = False
        moveTo(10, 10)
        run_browser_thread(chrome_path, url)
        sleep(5)
        hotkey('f11')
        sleep(1)
        try:
            x, y = locateCenterOnScreen('enter.png')
            located = True
        except:
            print("Image not found")
            located = False
        if located:
            moveTo(x, y-200)
            click(clicks=3)
            sleep(0.5)
            hotkey('backspace')
            sleep(0.5)
            write("galagut12@outlook.com")
            sleep(0.5)
            click(x, y)
        sleep(10)
        time = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
        filename = time + ".png"
        screenshot(filename)
        print(filename + " saved\n")
        hotkey('ctrl', 'w')
        sleep(interval)
