import win32gui
import win32con
import win32api
import base64
import requests
import json
from os import system
from cv2 import *
from pathlib import Path
cam = VideoCapture(0)   # 0 -> index of camera
imgbb = "70666f44ff616dc614abdfdd3d310af3" # Insert your own API key.
url = 'https://api.imgbb.com/1/upload' # Use your own image host, or by default use imgbb
def uploadImage(filename):
    with open(filename, "rb") as file:
        payload = {
            "key": imgbb,
            "image": base64.b64encode(file.read()),
            "expiration": "60",
        }
        res = requests.post(url, payload)
        file.close()
    return res.json()["data"]["url"]
hwndMain = win32gui.FindWindow("Notepad", "Untitled - Notepad") # Can use "Notepad", "Untitled - Notepad" to test without game
hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
print(hwndMain)
print(hwndChild)
#while(True):
#    temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x44, 0)
#    print(temp)
#    sleep(1)

# initialize the camera
while True:
    s, img = cam.read()
    if s:    # frame captured without any errors
        namedWindow("cam-test")
        imshow("cam-test",img)
        waitKey(0)
        imwrite("filename.jpg",img) #save image
    pic = uploadImage("filename.jpg")
    print(pic)
    with open("url.txt", "w") as file:
        file.write(pic)
        file.close()
    print("Starting NodeJS")
    system("node req.js")
    print("Finished.")
    txt = Path('output.txt').read_text()
    print(txt)
    jtxt = json.loads(txt)
    score = jtxt[0]['class']
    print(score)
    if score.lower() == "up":
        win32api.SendMessage(hwndChild, win32con.WM_CHAR, 0x57, 0)
    elif score.lower() == "left":
        win32api.SendMessage(hwndChild, win32con.WM_CHAR, 0x41, 0)
    elif score.lower() == "right":
        win32api.SendMessage(hwndChild, win32con.WM_CHAR, 0x44, 0)