from __future__ import annotations
from types import TracebackType
from Xlib.protocol.request import GetGeometry
from pyautogui import *
from pynput.keyboard import *
from tkinter import *
import time
import os

running = False
    
def antiafk_loop():
    if running==True: 
        time.sleep(3)
        keyDown('shift')
        time.sleep(0.001)
        hotkey(':')
        time.sleep(0.001)
        keyUp('shift')
        time.sleep(0.001)
        typewrite('e dance')
        time.sleep(3)
        hotkey('x')
        time.sleep(3)
        hotkey('k')
        time.sleep(3)
        hotkey('k')
        time.sleep(3)
        hotkey('z')
        time.sleep(3)
        hotkey('s')
    else:
        root.after(60, antiafk_loop)

def start():
    global running
    running = True

def stop():
    global running
    running = False 
    
def launch_fivem():
    filepath = '"D:\\jeu\\rockstar\\FiveM.exe"'
    os.startfile(filepath)

root = Tk()
root.title("Anti Afk")
root.geometry("400x400")

app = Frame(root)
app.grid()
start = Button(app, text='start', command=start)
stop = Button(app, text='stop', command=stop)
launch_fivem = Button(app, text='launch_fivem', command=launch_fivem)

start.grid()
stop.grid()
launch_fivem.grid()

root.after(1000, antiafk_loop)
root.mainloop()
