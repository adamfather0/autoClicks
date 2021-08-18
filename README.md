# autoClick
## How to use it
* Open autoClick.py and run code.
* the GUI shows 4 fields for users to controll the:
    * URL of webpages
    * speed of Clicks (per second)
    * Duration of running time (in second)
    * Click position (in the format of (x,y))
* enjoy it!

## The details of the code
* the packages
    * win32api
    * win32con
    * time
    * selenium--webdriver
    * tkinter
* the description of functions
    1. URL :Using **webdriver** to open webpages on the **Chrome**, please make sure you have installed chrome in your platform before running this code. If there is a **WebDriverException** when excuting the code, just download chrome webdriver on https://sites.google.com/a/chromium.org/chromedriver/, then put it in the default location where your chrome is. 
    1. Speed of clicks : using **time.sleep( 1/speed )** to control the speed of clicks.
    1. Duration : I use **time** module to control the duration. However, it seems that there are some delays due to unknown reasons. I'll fixed it in the future. 
    1. Click position : Instead using html objects to identify the click position, I tried to use win32api and win32con to allow users to assign click position by position coordinate in the form of (x,y)
    # The end
    enjoy yuor clicks! weeeeeeee~~~
    
    >Author : adamfather0 