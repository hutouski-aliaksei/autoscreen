import webbrowser
import threading


def run_browser(chrome_path, url):
    webbrowser.get(chrome_path).open(url)


def run_browser_thread(chrome_path, url):
    browser_thread = threading.Thread(target=run_browser, args=(chrome_path, url, ))
    browser_thread.daemon = True
    browser_thread.start()

