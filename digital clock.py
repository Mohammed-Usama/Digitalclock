from tkinter import Tk
from tkinter import Label
import time

master = Tk()
master.title("My Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(500,get_time)

clock = Label(master, font=("Calibri",80), bg="black", fg="blue")
clock.pack()

get_time()

master.mainloop()