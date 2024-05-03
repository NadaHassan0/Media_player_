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

window = Tk()
window.title("Music player")

myMenu = Menu(window)
window.config(menu=myMenu)
controlSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Menu", menu=controlSongMenu)
controlSongMenu.add_command(label="Add songs")
controlSongMenu.add_command(label="Delete song")

window.geometry("800x600")
window.configure(bg="#15253F")
window.resizable(width=False, height=False)

mixer.init()


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



image_icon = PhotoImage(file="media_player/image/icons8-pause-button-50.png")
window.iconphoto(False, image_icon)

slider = customtkinter.CTkSlider(master=window, from_=0, to=1, command=volume, width=230)
slider.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)

play_button = PhotoImage(file="media_player/image/icons8-play-button-50.png")
Button(window, image=play_button, bg="#15253F", bd=0).place(x=170, y=450)

stop_button = PhotoImage(file="media_player/image/icons8-stop-circled-50.png")
Button(window, image=stop_button, bg="#15253F", bd=0).place(x=100, y=450)

resume_button = PhotoImage(file="media_player/image/icons8-pause-button-50.png")
Button(window, image=resume_button, bg="#15253F", bd=0).place(x=240, y=450)

vol_img = ImageTk.PhotoImage(file='media_player/image/icons8-speaker-30.png')
mute_img = ImageTk.PhotoImage(file='media_player/image/icons8-mute-30.png')

vol_button = Button(window, image=vol_img, command=mute, bg='#15253F', bd=0)
vol_button.place(relx=0.61, rely=0.8, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=window, progress_color='#D0D7E1', width=500)
progressbar.place(relx=0.5, rely=0.66, anchor=tkinter.CENTER)



def toggle_repeat_mode():
    global repeat_mode
    if repeat_mode == "Repeat All":
        repeat_mode = "Repeat One"
        repeat_button.config(image=repeat_one_img)
    else:
        repeat_mode = "Repeat All"
        repeat_button.config(image=repeat_all_img)


# Define repeat mode variable and set initial mode
repeat_mode = "Repeat All"

# Load images for repeat modes
repeat_all_img = ImageTk.PhotoImage(file='media_player/image/icons8-repeat-30.png')
repeat_one_img = ImageTk.PhotoImage(file='media_player/image/icons8-repeat-one-30.png')

# Create button for toggling repeat mode
repeat_button = Button(window, image=repeat_all_img, command=toggle_repeat_mode, bg="#15253F", bd=0)
repeat_button.place(x=300, y=460)  # Adjust position as needed

window.mainloop()