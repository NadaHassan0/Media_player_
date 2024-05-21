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
import wave
import numpy as np
import tkinter.filedialog as filedialog
import os
import pygame
import pygame
import tkinter as tk
from tkinter import filedialog

import tkinter as tk
from tkinter import filedialog, Listbox, PhotoImage, Menu
import pygame
import tkinter
from tkinter.ttk import Progressbar
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time
import math


pygame.mixer.init()

list_of_songs = ['media_player/songs_listbox/VivaLaVida.wav'] # Add more songs into this list, make sure they are .wav and put into the music Directory.
list_of_covers = ['media_player/image/photo_2024-05-21_13-52-22.jpg'] # Add more JPEGS into the img directory, You can download city from my Github as a starting point.
n = 0

def add_songs():
    song_paths = filedialog.askopenfilenames(
        title="Select Songs", 
        filetypes=[("Audio Files", "*.mp3 *.wav"), ("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")]
    )
    for song in song_paths:
        songs_listbox.insert(tk.END, song)

def delete_song():
    selected_song_index = songs_listbox.curselection()
    if selected_song_index:
        songs_listbox.delete(selected_song_index)

def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2=image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    
    label1 = tkinter.Label(window, image=load)
    label1.image = load
    label1.place(relx=.3, rely=.06)

    stripped_string = song_name[6:-4] #This is to exlude the other characters
                                                # 6       :      -4
                                    # Example: 'music/ | City | .wav'
                                    # This works because the music will always be between those 2 values
    
    song_name_label = tkinter.Label(text = stripped_string, bg='#222222', fg='white')
    song_name_label.place(relx=.4, rely=.6)


def threading():
    t1 = Thread(target=progress)
    t1.start()

def play_song():
    threading()
    global n 
    current_song = n
    if n > 2:
        n = 0
    song_name = list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(.5)
    get_album_cover(song_name, n)

    # print('PLAY')
    n += 1


def stop_song():
    pygame.mixer.music.stop()

def pause_song():
    pygame.mixer.music.pause()

def resume_song():
    pygame.mixer.music.unpause()

def volume(value):
    pygame.mixer.music.set_volume(float(value))
    if float(value) > 0:
        vol_button.config(image=vol_img)
    else:
        vol_button.config(image=mute_img)

def mute():
    if slider.get() > 0:
        previous_volume = slider.get()
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

def progress():
    a = pygame.mixer.Sound(f'{list_of_songs[n]}')
    song_len = a.get_length() * 3
    for i in range(0, math.ceil(song_len)):
        time.sleep(.4)
        progressbar.set(pygame.mixer.music.get_pos() / 1000000)

# Create the main window
window = tk.Tk()
window.title("Music Player")
window.geometry("800x600")
window.configure(bg="#15253F")
window.resizable(width=False, height=False)

# Menu
myMenu = Menu(window)
window.config(menu=myMenu)
controlSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Menu", menu=controlSongMenu)
controlSongMenu.add_command(label="Add songs", command=add_songs)
controlSongMenu.add_command(label="Delete song", command=delete_song)
controlSongMenu.add_command(label="Record song")

# Icon
image_icon = PhotoImage(file="media_player/image/icons8-music-50.png")
window.iconphoto(False, image_icon)

# Songs listbox
songs_listbox = Listbox(window, bg="#15253F", fg="white", selectbackground="gray")
songs_listbox.pack(fill=tk.BOTH, expand=True)

# Volume Slider
slider = customtkinter.CTkSlider(master=window, from_=0, to=1, command=volume, width=150)
slider.place(relx=0.2, rely=0.65, anchor=tk.CENTER)
slider.set(0.5)  # Set initial volume to 50%

# Buttons
add_song_button = PhotoImage(file="media_player/image/icons8-add-song-100.png")
tk.Button(window, image=add_song_button, bg="#15253F", bd=0, command=add_songs).place(x=120, y=150)

play_button = PhotoImage(file="media_player/image/icons8-play-button-50.png")
tk.Button(window, image=play_button, bg="#15253F", bd=0, command=play_song).place(x=375, y=500)

stop_button = PhotoImage(file="media_player/image/icons8-stop-circled-50.png")
tk.Button(window, image=stop_button, bg="#15253F", bd=0, command=stop_song).place(x=300, y=500)

pause_button = PhotoImage(file="media_player/image/icons8-pause-button-50.png")
tk.Button(window, image=pause_button, bg="#15253F", bd=0, command=pause_song).place(x=450, y=500)

#resume_button = PhotoImage(file="media_player/image/icons8-resume-button-50.png")
#tk.Button(window, image=resume_button, bg="#15253F", bd=0, command=resume_song).place(x=450, y=500)

next_button = PhotoImage(file="media_player/image/icons8-forward-30.png")
tk.Button(window, image=next_button, bg="#15253F", bd=0).place(x=520, y=510)

previous_button = PhotoImage(file="media_player/image/icons8-previous-30.png")
tk.Button(window, image=previous_button, bg="#15253F", bd=0).place(x=250, y=510)

progressbar = customtkinter.CTkProgressBar(master=window, progress_color='#D0D7E1', width=570)
progressbar.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

vol_img = ImageTk.PhotoImage(file='media_player/image/icons8-speaker-30.png')
mute_img = ImageTk.PhotoImage(file='media_player/image/icons8-mute-30.png')

vol_button = tk.Button(window, image=vol_img, command=mute, bg='#15253F', bd=0)
vol_button.place(relx=0.05, rely=0.65, anchor=tk.CENTER)

repeat_mode = "Repeat All"
repeat_all_img = ImageTk.PhotoImage(file='media_player/image/icons8-repeat-30.png')
repeat_one_img = ImageTk.PhotoImage(file='media_player/image/icons8-repeat-one-30.png')
repeat_button = tk.Button(window, image=repeat_all_img, command=toggle_repeat_mode, bg="#15253F", bd=0)
repeat_button.place(x=600, y=490)

window.mainloop()
