from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")
root.iconbitmap(r"Clock.ico")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

label = Label(root,font=("AquireBold-8Ma60",100))
label.pack(anchor='center')
time()

mainloop()
