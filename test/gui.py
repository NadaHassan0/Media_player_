from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

window=Tk()
window.title("Music player")

myMenu = Menu(window)
window.config(menu=myMenu)
controlSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Menu", menu=controlSongMenu)
controlSongMenu.add_command(label="Ad songs")
controlSongMenu.add_command(label="Delee song")

window.geometry("920x670+290+85")
window.configure(bg="#D4D1FA")  # Changed the background color to navy blue
window.resizable(False,False)

mixer.init()

#icon
image_icon=PhotoImage(file="pngegg.png")
window.iconphoto(False,image_icon)

#logo
#logo=PhotoImage(file="pngegg.png")
#ouLabel(window,image=logo,bg="#D4D1FA").place(x=65,y=115)

#button
play_button=PhotoImage(file="7f2ee150-698e-4cd6-b32e-7c2f878bf1fkk3.png")
Button(window,image=play_button,bg="#D4D1FA",bd=0).place(x=100,y=550)

#stop_button=PhotoImage(file="pngegg.png")
#Button(window,image=stop_button,bg="#D4D1FA",bd=0).place(x=30,y=500)

#resume_button=PhotoImage(file="pngegg.png")
#Button(window,image=resume_button,bg="#D4D1FA",bd=0).place(x=115,y=500)

#pause_button=PhotoImage(file="pngegg.png")
#Button(window,image=pause_button,bg="#D4D1FA",bd=0).place(x=200,y=500)


window.mainloop()
