# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 22:08:57 2018

@author: ADMIN
"""

from tkinter import *
import time
import os

                                                            #Basic clock GUI
win = Tk()
win.title("Clock")
example = Label(win,font=('times', 28, 'bold'), background='blue', foreground='white')
example.pack(fill=BOTH, expand=1)
e1=Entry(win)
e1.pack()
bt=Button(win, text='Set alarm', command=Setal).pack()      #Button to set alarm time
def Setal():
    t=e1.get()
    if(t==time.strftime('%H:%M:%S')):
        os.system('start alarm.mp3')                        #Plays mp3 file as alarm


def passtime():                                             #Time change in clock
    a = time.strftime('%H:%M:%S')
    if a != example["text"]:
        example["text"] = a
    Setal()
    example.after(200, passtime) 
passtime()
win.mainloop()                                              #Set it on infinite loop
