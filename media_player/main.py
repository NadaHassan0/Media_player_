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
controlSongMenu.add_command(label="Add songs")
controlSongMenu.add_command(label="Delete song")

window.geometry("800x600")
window.configure(bg = "#15253F")  
window.resizable(width=False,height=False)

mixer.init()

def volume(value):
 pygame.mixer.music.set_volume(value)


def volume(value):
    pygame.mixer.music.set_volume(value)
    if value > 0:
        vol_button.config(image=vol_img)
    else:
        vol_button.config(image=mute_img)


def mute():
    volume_value = slider.get()
    if volume_value > 0:
        slider.set(0)
        vol_button.config(image=mute_img)
    else:
        slider.set(0.5)
        vol_button.config(image=vol_img)

def toggle_repeat_mode():
    global repeat_mode
    if repeat_mode == "Repeat All":
        repeat_mode = "Repeat One"
        repeat_button.config(image=repeat_one_img)
    else:
        repeat_mode = "Repeat All"
        repeat_button.config(image=repeat_all_img)
 
#icon
image_icon=PhotoImage(file="media_player/image/icons8-music-50.png")
window.iconphoto(False,image_icon)

#logo
#logo=PhotoImage(file="media_player/image/icons8-music-50.png")
#Label(window,image=logo,bg="#D4D1FA").place(x=65,y=115)

#buttons
slider = customtkinter.CTkSlider(master=window, from_= 0, to=1, command=volume, width=150)
slider.place(relx=0.2, rely=0.65, anchor=tkinter.CENTER)

add_song_button=PhotoImage(file="media_player/image/icons8-add-song-100.png")
Button(window,image=add_song_button,bg="#15253F",bd=0).place(x=120,y=150)

play_button=PhotoImage(file="media_player\image\icons8-play-button-50.png")
Button(window,image=play_button,bg="#15253F",bd=0).place(x=375,y=500)

stop_button=PhotoImage(file="media_player\image\icons8-stop-circled-50.png")
Button(window,image=stop_button,bg="#15253F",bd=0).place(x=300,y=500)

resume_button=PhotoImage(file="media_player\image\icons8-pause-button-50.png")
Button(window,image=resume_button,bg="#15253F",bd=0).place(x=450,y=500)

next_button=PhotoImage(file="media_player/image/icons8-forward-30.png")
Button(window,image=next_button,bg="#15253F",bd=0).place(x=520,y=510)

previous_button=PhotoImage(file="media_player/image/icons8-previous-30.png")
Button(window,image=previous_button,bg="#15253F",bd=0).place(x=250,y=510)

progressbar = customtkinter.CTkProgressBar(master=window, progress_color='#D0D7E1', width=570)
progressbar.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

vol_img = ImageTk.PhotoImage(file='media_player/image/icons8-speaker-30.png')
mute_img = ImageTk.PhotoImage(file='media_player/image/icons8-mute-30.png')

vol_button = Button(window, image=vol_img, command=mute, bg='#15253F', bd=0)
vol_button.place(relx=0.05, rely=0.65, anchor=tkinter.CENTER)

repeat_mode = "Repeat All"
repeat_all_img = ImageTk.PhotoImage(file='media_player/image/icons8-repeat-30.png')
repeat_one_img = ImageTk.PhotoImage(file='media_player/image/icons8-repeat-one-30.png')
repeat_button = Button(window, image=repeat_all_img, command=toggle_repeat_mode, bg="#15253F", bd=0)
repeat_button.place(x=600, y=490) 

window.mainloop()