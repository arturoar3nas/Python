import webbrowser
import time

def open_youtube():
    new = 2
    i = 0
    url = "http://www.youtube.com"

    while i < 5:
        time.sleep(1)
        webbrowser.open(url,new=new)
        i = i + 1


open_youtube()
