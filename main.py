from pyautogui import screenshot, hotkey, locateCenterOnScreen, click
from datetime import datetime
from time import sleep
from helper import run_browser_thread


if __name__ == '__main__':
    interval = int(input("Enter time interval: "))
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    url = "https://www.trupanion.com"
    while True:
        run_browser_thread(chrome_path, url)
        sleep(5)
        hotkey('f11')
        sleep(1)
        try:
            x, y = locateCenterOnScreen('quote.png')
        except:
            print("Image not found")
        click(x, y)
        sleep(3)
        time = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
        filename = time + ".png"
        screenshot(filename)
        print(filename + " saved\n")
        hotkey('ctrl', 'w')
        sleep(interval)
