import tkinter as tk

def define_layout(obj, cols=1, rows=1):
    
    def method(trg, col, row):
        
        for c in range(cols):    
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj)==list:        
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)    

#GUI
window = tk.Tk()
window.title("autoClick")
w,h = window.maxsize()
window.geometry('{}x{}'.format(w,h))

align_mode = "nswe"
pad = 5
WIDTH = 790
HEIGHT = 610
#設定視窗中總共有多少欄和列
define_layout(window, cols=10, rows=7)
#title
title = tk.Label(window, text = "AutoClick", fg = "#0066FF", font=("Arial",30))
title.grid(column=0,row=0,ipadx=pad,padx =pad,columnspan=10,sticky=align_mode)
#輸入URL的欄位 
word_URL= tk.Label(window, text = "Enter URL", bg="gray", fg="#0066FF",font=("Arial",16))
word_URL.grid(column=0,row=1,ipadx=pad,padx =pad,sticky=tk.W)
entry_URL = tk.Entry(window,width=40)
entry_URL.grid(column=1,row=1,columnspan = 1,ipadx=pad,padx =pad,sticky=tk.W)
#輸入點擊速度的欄位
word_speed= tk.Label(window, text = "Speed(clicks/s)", bg="gray", fg="#0066FF",font=("Arial",16))
word_speed.grid(column=0,row=2,ipadx=pad,padx =pad,sticky=tk.W)
entry_speed = tk.Entry(window,width=40)
entry_speed.grid(column=1,row=2,columnspan = 1,ipadx=pad,padx =pad,sticky=tk.W)
#輸入執行時間的欄位 
word_duration= tk.Label(window, text = "Duration(s)", bg="gray", fg="#0066FF",font=("Arial",16))
word_duration.grid(column=0,row=3,ipadx=pad,padx =pad,sticky=tk.W)
entry_duration = tk.Entry(window,width=40)
entry_duration.grid(column=1,row=3,columnspan = 1,ipadx=pad,padx =pad,sticky=tk.W)
#輸入點擊位置的欄位
word_pos= tk.Label(window, text = "Click position(x,y)", bg="gray", fg="#0066FF",font=("Arial",16))
word_pos.grid(column=0,row=4,ipadx=pad,padx =pad,sticky=tk.W)
word_x= tk.Label(window, text = "x:", bg="gray", fg="#0066FF",font=("Arial",16))
word_x.grid(column=1,row=4,ipadx=pad,padx =pad,sticky=tk.W)
word_y= tk.Label(window, text = "y:", bg="gray", fg="#0066FF",font=("Arial",16))
word_y.grid(column=3,row=4,ipadx=pad,padx =pad,sticky=tk.W)
entry_pos_x = tk.Entry(window,width=40)
entry_pos_x.grid(column=1,row=4,columnspan = 1,ipadx=pad,padx =pad,sticky=tk.E)
entry_pos_y = tk.Entry(window,width=40)
entry_pos_y.grid(column=3,row=4,columnspan = 1,ipadx=pad,padx =pad,sticky=tk.E)

word_start= tk.Button(window, text = "start Click!", bg="gray", fg="#0066FF",font=("Arial",30))
word_start.grid(column=0,row=5,columnspan = 10,ipadx=pad,sticky=align_mode)

#讓每個項目縮放視窗時位置不會跑掉
layout_list = [title,word_URL,entry_URL,word_speed,entry_speed,word_duration,entry_duration,word_pos,word_x
                ,word_y,entry_pos_x,entry_pos_y,word_start]
define_layout(layout_list)