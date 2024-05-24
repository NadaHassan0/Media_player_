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
import numpy as np
import tkinter.filedialog as filedialog
import os
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
from pydub import AudioSegment
from pydub.playback import play
import tkinter as tk
from tkinter import filedialog, Menu
from pydub import AudioSegment
from pydub.playback import play
import threading
from playsound import playsound
import tempfile
import os
import pydub
import numpy as np
import scipy.signal as signal
import sounddevice as sd
import librosa
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog, messagebox


pygame.mixer.init()

#list_of_songs
list_of_songs = [
    'test/audio_files/hard-spanish-guitar-melody_126bpm_B_minor.wav',
    'test/audio_files/paradise-lo-fi-wet-chords-gentle-loop_88bpm_F_major.wav',
    'test/audio_files/rage-mode-type-lead-synth-loop_157bpm_D#_major.wav']

#list_of_covers(jpg)
list_of_covers = [
    'media_player/image/photo_2024-05-21_13-52-22.jpg',
    'media_player/image/photo_2024-05-21_17-17-53.jpg',
    'media_player/image/photo_2024-05-21_13-52-22.jpg'
]  

#variables
n = 0
music_playing = False
is_paused = False
is_muted = False
paused = False
speed = 1.0
current_position = 0
original_duration = 0
song_playing = False

# function to add songs
def add_songs():
    song_paths = filedialog.askopenfilenames(
        title="Select Songs",
        filetypes=[("Audio Files", "*.mp3 *.wav"), ("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")]
    )
    for song in song_paths:
        songs_listbox.insert(tk.END, song)

#function to delete song from menu
def delete_song():
    selected_song_index = songs_listbox.curselection()
    if selected_song_index:
        songs_listbox.delete(selected_song_index)

#frame for photo of the song
def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2=image1.resize((200, 200))
    load = ImageTk.PhotoImage(image2)
    
    label1 = tkinter.Label(window, image=load)
    label1.image = load
    label1.place(relx=.12, rely=.2)

    stripped_string = song_name[6:-4] #This is to exlude the other characters
                                                # 6       :      -4
                                    
    song_name_label = tkinter.Label(text = stripped_string, bg='#15253F', fg='white')
    song_name_label.place(relx=.10, rely=.55)


#def threading():
 #   t1 = Thread(target=progress)
  #  t1.start()

# Function to play the song
def play_song():
    global n, paused
    if not pygame.mixer.music.get_busy() or paused:
        song_name = list_of_songs[n]
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(0.5)
        get_album_cover(song_name, n)
        update_progress_bar()
        paused = False

# Function to update the progress bar
def update_progress_bar():
    global paused
    while pygame.mixer.music.get_busy() and not paused:
        song_len = pygame.mixer.Sound(list_of_songs[n]).get_length()
        pos = pygame.mixer.music.get_pos() / 1000  # Current position in seconds
        progress = (pos / song_len) * 100
        pbar["value"] = progress
        window.update()
        time.sleep(0.1)
    # If music is paused, simply return without updating the progress bar
    return

# Function to stop the song
def stop_song():
    global play_thread, song_playing, current_position, original_duration
    if song_playing:
        play_thread.terminate()
        song_playing = False
        current_position = 0
        original_duration = 0  # Reset the original duration
        pygame.mixer.music.stop()  # Stop the pygame music playback

# Function to pause the song
def pause_song():
    global play_thread, song_playing, current_position, original_duration
    if song_playing:
        play_thread.terminate()
        song_playing = False
        # Update the current position based on the new duration
        new_duration = pydub.AudioSegment.from_file(list_of_songs[n]).duration_seconds
        current_position = (current_position / original_duration) * new_duration
        original_duration = new_duration  # Update the original duration
        pygame.mixer.music.pause()  # Pause the pygame music playback


def next_song():
    global n
    n = (n + 1) % len(list_of_songs)  # Loop around to the beginning if at the end
    stop_song()  # Stop the current song before playing the next one
    play_song()

def previous_song():
    global n
    n = (n - 1) % len(list_of_songs)  # Loop around to the end if at the beginning
    stop_song()  # Stop the current song before playing the previous one
    play_song()


previous_volume = 0

# function to edit the volume of song
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




def change_speed(speed):
    global play_thread, current_position, original_duration
    stop_song()  # Stop the currently playing song
    song_name = list_of_songs[n]
    song = pydub.AudioSegment.from_file(song_name)
    
    # Store the original duration of the song
    original_duration = song.duration_seconds
    
    if speed == 0.5:
        song = song.speedup(playback_speed=0.5)
    elif speed == 1.5:
        song = song.speedup(playback_speed=1.5)
    elif speed == 2:
        song = song.speedup(playback_speed=2.0)
    
    # Calculate the new current position based on the changed song duration
    new_duration = song.duration_seconds
    current_position = (current_position / original_duration) * new_duration
    original_duration = new_duration  # Update the original duration

    temp_wav_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
    song.export(temp_wav_path, format="wav")

    def play_temp_file():
        audio = pydub.AudioSegment.from_wav(temp_wav_path)
        audio = audio[int(current_position * 1000):]  # Set the position to resume playback
        audio.export(temp_wav_path, format="wav")
        play(pydub.AudioSegment.from_wav(temp_wav_path))
        os.remove(temp_wav_path)

    play_thread = Thread(target=play_temp_file)
    play_thread.start()



def on_closing():
    stop_song()
    window.destroy()  

# Create the main window
window = tk.Tk()
window.title("NaNo Player")
window.geometry("800x600")
window.configure(bg="#15253F")
window.resizable(width=False, height=False)
window.protocol("WM_DELETE_WINDOW", on_closing)

# Menu
myMenu = Menu(window)
window.config(menu=myMenu)
controlSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Menu", menu=controlSongMenu)
controlSongMenu.add_command(label="Add songs", command=add_songs)
controlSongMenu.add_command(label="Deletesong", command=delete_song)
menu_bar = Menu(window)
window.config(menu=menu_bar)


# Create the menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Create a menu
controlSongMenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=controlSongMenu)

# Add commands to the menu
controlSongMenu.add_command(label="Add songs", command=add_songs)
controlSongMenu.add_command(label="Delete song", command=delete_song)

# Create a listbox to display the songs
songs_listbox = Listbox(window, bg='#15253F', fg='white', selectbackground='#15253F', selectforeground='white')
songs_listbox.place(relx=.5, rely=.3, relwidth=.3, relheight=.2)

# Populate the listbox with songs
for song in list_of_songs:
    songs_listbox.insert(tk.END, song)

# Create buttons
#add song button
add_song_button = PhotoImage(file="media_player/image/icons8-add-song-100.png")
tk.Button(window, image=add_song_button, bg="#15253F", bd=0, command=add_songs).place(x=120, y=150)

# play song button
play_button = PhotoImage(file="media_player/image/icons8-play-button-50.png")
tk.Button(window, image=play_button, bg="#15253F", bd=0, command=play_song).place(x=375, y=500)

#stop song button
stop_button = PhotoImage(file="media_player/image/icons8-stop-circled-50.png")
tk.Button(window, image=stop_button, bg="#15253F", bd=0, command=stop_song).place(x=300, y=500)

#pause song button
pause_button = PhotoImage(file="media_player/image/icons8-pause-button-50.png")
tk.Button(window, image=pause_button, bg="#15253F", bd=0, command=pause_song).place(x=450, y=500)

#next song button
next_button = PhotoImage(file="media_player/image/icons8-forward-30.png")
tk.Button(window, image=next_button, bg="#15253F", bd=0 ,command=next_song).place(x=520, y=510)

#
previous_button = PhotoImage(file="media_player/image/icons8-previous-30.png")
tk.Button(window, image=previous_button, bg="#15253F", bd=0 ,command=previous_song).place(x=250, y=510)

# Create a progress bar to indicate the current song's progress
style = ttk.Style()

# Set the theme to "alt"
style.theme_use("alt")
pbar =  ttk.Progressbar(window, orient="horizontal", length=500, mode="determinate", style="TProgressbar")
pbar.pack(pady=10)
pbar.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

# Create volume button
vol_img = PhotoImage(file='media_player/image/icons8-speaker-30.png')
mute_img = PhotoImage(file='media_player/image/icons8-mute-30.png')
vol_button = tk.Button(window, image=vol_img, command=mute, bg='#15253F', bd=0)
vol_button.place(relx=0.05, rely=0.65, anchor=tk.CENTER)

# Volume Slider
slider = customtkinter.CTkSlider(master=window, from_=0, to=1, command=volume, width=150)
slider.place(relx=0.2, rely=0.65, anchor=tk.CENTER)
slider.set(0.5)  # Set initial volume to 50%

# Create repeat mode button
repeat_mode = "Repeat All"
repeat_all_img = ImageTk.PhotoImage(file='media_player/image/icons8-repeat-30.png')
repeat_one_img = ImageTk.PhotoImage(file='media_player/image/icons8-repeat-one-30.png')
repeat_button = tk.Button(window, image=repeat_all_img, command=toggle_repeat_mode, bg="#15253F", bd=0)
repeat_button.place(relx=.75, rely=.85)

# Add a speed button
speed_icon = PhotoImage(file="media_player/image/icons8-speed.png")
speed_button = Label(window, image=speed_icon, bg='#15253F')
speed_button.place(x=650, y=550, anchor=tk.CENTER)
speed_menu = Menu(window, tearoff=0)
speed_menu.add_command(label="x0.5", command=lambda: change_speed(0.5))
speed_menu.add_command(label="x1", command=lambda: change_speed(1))
speed_menu.add_command(label="x1.5", command=lambda: change_speed(1.5))
speed_menu.add_command(label="x2", command=lambda: change_speed(2))
speed_button.bind("<Button-1>", lambda e: speed_menu.post(e.x_root, e.y_root))


# Start the Tkinter event loop
window.mainloop()