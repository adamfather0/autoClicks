import win32api
import win32con
import time
from selenium import webdriver
import GUI
def autoClick(x=0,y=0,speed = 0):
    #參數
    url = GUI.entry_URL.get()
    x = int(GUI.entry_pos_x.get())
    y= int(GUI.entry_pos_y.get())
    speed = int(GUI.entry_speed.get())
    duration = int(GUI.entry_duration.get())
    #開啟指定網頁
    openWeb(url)
    #開始點擊
    run = True
    time_start = time.time()
    while run:
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        if speed == 0 :
            pass
        else:
            time.sleep(1/speed)
        time_end = time.time()
        if time_end - time_start > duration:
            run = False
       
    return 0

def openWeb(url=""):
    #自動打開url所指的網頁
    try:
        driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
    except:
        print("Please download webdriver on https://sites.google.com/a/chromium.org/chromedriver/. Then put it in the chrome folder.")
    driver.get(url)
    driver.maximize_window()
    time.sleep(1) #休息一秒後執行其他動作，不過可以刪掉


GUI.word_start.config(command = lambda:autoClick())
GUI.window.mainloop()



