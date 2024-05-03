from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, filedialog
from pygame import mixer
import os
import customtkinter
import tkinter
from tkinter.ttk import Progressbar
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time
import math

window=Tk()
window.title("Music player")

myMenu = Menu(window)
window.config(menu=myMenu)
controlSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Menu", menu=controlSongMenu)
controlSongMenu.add_command(label="Ad songs")
controlSongMenu.add_command(label="Delete song")

window.geometry("800x600")
window.configure(bg = "#15253F")  # Changed the background color to navy blue
window.resizable(width=False,height=False)

mixer.init()

def volume(value):
 pygame.mixer.music.set_volume(value)
 
#icon
image_icon=PhotoImage(file="media_player\image\icons8-pause-button-50.png")
window.iconphoto(False,image_icon)

#logo
#logo=PhotoImage(file="pngegg.png")
#Label(window,image=logo,bg="#D4D1FA").place(x=65,y=115)

#buttons

slider = customtkinter.CTkSlider(master=window, from_= 0, to=1, command=volume, width=230)
slider.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)

play_button=PhotoImage(file="media_player\image\icons8-play-button-50.png")
Button(window,image=play_button,bg="#15253F",bd=0).place(x=170,y=450)

stop_button=PhotoImage(file="media_player\image\icons8-stop-circled-50.png")
Button(window,image=stop_button,bg="#15253F",bd=0).place(x=100,y=450)

resume_button=PhotoImage(file="media_player\image\icons8-pause-button-50.png")
Button(window,image=resume_button,bg="#15253F",bd=0).place(x=240,y=450)


progressbar = customtkinter.CTkProgressBar(master=window, progress_color='#D0D7E1', width=500)
progressbar.place(relx=0.5, rely=.66, anchor=tkinter.CENTER)

#next_button=PhotoImage(file="media_player/image/icons8-more-than-70.png")
#Button(window,image=next_button,bg="#e6e6fa",bd=0).place(x=580,y=450)

#previous_button=PhotoImage(file="media_player/image/icons8-702.png")
#Button(window,image=next1_button,bg="#e6e6fa",bd=0).place(x=150,y=450)

window.mainloop()