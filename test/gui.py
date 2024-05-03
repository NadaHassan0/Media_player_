from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
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
controlSongMenu.add_command(label="Delete song")

window.geometry("800x600")
window.configure(bg="#e6e6fa")  # Changed the background color to navy blue
window.resizable(width=False,height=False)

mixer.init()
#NOUR
#icon
image_icon=PhotoImage(file="media_player/image/icons8-music-200.png")
window.iconphoto(False,image_icon)

#logo
#logo=PhotoImage(file="pngegg.png")
#Label(window,image=logo,bg="#D4D1FA").place(x=65,y=115)

#button
play_button=PhotoImage(file="media_player/image/icons8-play-button-circled-100.png")
Button(window,image=play_button,bg="#e6e6fa",bd=0).place(x=350,y=430)

stop_button=PhotoImage(file="media_player/image/icons8-more-than-708.png")
Button(window,image=stop_button,bg="#e6e6fa",bd=0).place(x=250,y=450)

resume_button=PhotoImage(file="media_player/image/icons8-pause-button-1000.png")
Button(window,image=resume_button,bg="#e6e6fa",bd=0).place(x=480,y=450)

next_button=PhotoImage(file="media_player/image/icons8-more-than-70.png")
Button(window,image=next_button,bg="#e6e6fa",bd=0).place(x=580,y=450)

next1_button=PhotoImage(file="media_player/image/icons8-702.png")
Button(window,image=next1_button,bg="#e6e6fa",bd=0).place(x=150,y=450)


window.mainloop()
