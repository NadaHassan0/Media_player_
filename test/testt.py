import tkinter as tk
from tkinter import filedialog, Listbox, PhotoImage, Menu
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import pygame
from threading import Thread
import time
import math

pygame.mixer.init()

# Initial lists
list_of_songs = [
    'media_player/songs_listbox/02. Adele - Hello (Ringtone).mp3',
    'media_player/songs_listbox/08 Elastic Heart (feat. The Weeknd & Diplo).mp3'
]

list_of_covers = [
    'media_player/image/photo_2024-05-21_13-52-22.jpg',
    'media_player/image/photo_2024-05-21_17-17-53.jpg'
]

# Variables
n = 0
music_playing = False
is_paused = False
is_muted = False
speed = 1.0

# Initialize the main window
root = tk.Tk()
root.title("Media Player")
root.geometry("800x600")
root.configure(bg="#15253F")
root.resizable(width=False, height=False)
root.protocol("WM_DELETE_WINDOW", root.destroy)

# Listbox to display songs
songs_listbox = Listbox(root, bg='#15253F', fg='white', selectbackground='#15253F', selectforeground='white')
songs_listbox.place(relx=.5, rely=.3, relwidth=.3, relheight=.2)

# Populate the listbox with songs
for song in list_of_songs:
    songs_listbox.insert(tk.END, song)

# Function to add songs
def add_songs():
    song_paths = filedialog.askopenfilenames(
        title="Select Songs",
        filetypes=[("MP3 Files", "*.mp3")]
    )
    for song in song_paths:
        list_of_songs.append(song)
        songs_listbox.insert(tk.END, song)
        # Dummy code to add corresponding cover
        cover_path = f'media_player/image/photo_{os.path.basename(song)}.jpg'
        list_of_covers.append(cover_path)

# Function to delete song from menu
def delete_song():
    selected_song_index = songs_listbox.curselection()
    if selected_song_index:
        song_index = selected_song_index[0]
        songs_listbox.delete(song_index)
        list_of_songs.pop(song_index)
        list_of_covers.pop(song_index)

# Function to display album cover
def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2 = image1.resize((200, 200))
    load = ImageTk.PhotoImage(image2)
    
    label1 = tk.Label(root, image=load)
    label1.image = load
    label1.place(relx=.12, rely=.2)

    stripped_string = os.path.basename(song_name)[:-4]
    song_name_label = tk.Label(root, text=stripped_string, bg='#15253F', fg='white')
    song_name_label.place(relx=.10, rely=.55)

# Function to handle threading
def threading(func):
    t1 = Thread(target=func)
    t1.start()

# Function to play song
def play_song():
    global n, is_paused, music_playing
    current_song = n
    if n >= len(list_of_songs):
        n = 0
    song_name = list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(.5)
    get_album_cover(song_name, n)
    music_playing = True
    threading(progress)

def progress():
    while music_playing:
        song_length = pygame.mixer.Sound(f'{list_of_songs[n]}').get_length()
        for i in range(int(song_length)):
            if not music_playing:
                break
            time.sleep(1)
            progressbar.set(pygame.mixer.music.get_pos() / song_length)

# Function to stop song
def stop_song():
    global music_playing
    pygame.mixer.music.stop()
    music_playing = False

def next_song():
    global n
    n = (n + 1) % len(list_of_songs)
    play_song()

def previous_song():
    global n
    n = (n - 1) % len(list_of_songs)
    play_song()

def pause_song():
    global is_paused  
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
    else:
        pygame.mixer.music.pause()
        is_paused = True

previous_volume = 0

# Function to edit the volume of song
def volume(value):
    pygame.mixer.music.set_volume(float(value))
    if float(value) > 0:
        vol_button.config(image=vol_img)
    else:
        vol_button.config(image=mute_img)

def mute():
    global previous_volume
    if slider.get() > 0:
        previous_volume = slider.get()
        slider.set(0)
        vol_button.config(image=mute_img)
    else:
        slider.set(previous_volume)
        vol_button.config(image=vol_img)

def toggle_repeat_mode():
    global repeat_mode
    if repeat_mode == "Repeat All":
        repeat_mode = "Repeat One"
        repeat_button.config(image=repeat_one_img)
    else:
        repeat_mode = "Repeat All"
        repeat_button.config(image=repeat_all_img)

def set_speed(value):
    global speed
    speed = float(value)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

# Menu
myMenu = Menu(root)
root.config(menu=myMenu)
controlSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Menu", menu=controlSongMenu)
controlSongMenu.add_command(label="Add songs", command=add_songs)
controlSongMenu.add_command(label="Delete song", command=delete_song)

# Create buttons
add_song_button = PhotoImage(file="media_player/image/icons8-add-song-100.png")
tk.Button(root, image=add_song_button, bg="#15253F", bd=0, command=add_songs).place(x=120, y=150)

play_button = PhotoImage(file="media_player/image/icons8-play-button-50.png")
tk.Button(root, image=play_button, bg="#15253F", bd=0, command=play_song).place(x=375, y=500)

stop_button = PhotoImage(file="media_player/image/icons8-stop-circled-50.png")
tk.Button(root, image=stop_button, bg="#15253F", bd=0, command=stop_song).place(x=300, y=500)

pause_button = PhotoImage(file="media_player/image/icons8-pause-button-50.png")
tk.Button(root, image=pause_button, bg="#15253F", bd=0, command=pause_song).place(x=450, y=500)

next_button = PhotoImage(file="media_player/image/icons8-forward-30.png")
tk.Button(root, image=next_button, bg="#15253F", bd=0, command=next_song).place(x=520, y=510)

previous_button = PhotoImage(file="media_player/image/icons8-previous-30.png")
tk.Button(root, image=previous_button, bg="#15253F", bd=0, command=previous_song).place(x=250, y=510)

# Progressbar
progressbar = Progressbar(root, orient=tk.HORIZONTAL, length=570, mode='determinate')
progressbar.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

# Create volume button
vol_img = PhotoImage(file='media_player/image/icons8-speaker-30.png')
mute_img = PhotoImage(file='media_player/image/icons8-mute-30.png')
vol_button = tk.Button(root, image=vol_img, command=mute, bg='#15253F', bd=0)
vol_button.place(relx=0.05, rely=0.65, anchor=tk.CENTER)

# Volume Slider
slider = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, command=volume, length=150, bg='#15253F', fg='white', troughcolor='gray')
slider.place(relx=0.2, rely=0.65, anchor=tk.CENTER)
slider.set(0.5)  # Set initial volume to 50%

# Create repeat mode button
repeat_mode = "Repeat All"
repeat_all_img = ImageTk.PhotoImage(file='media_player/image/icons8-repeat-30.png')
repeat_one_img = ImageTk.PhotoImage(file='media_player/image/icons8-repeat-one-30.png')
repeat_button = tk.Button(root, image=repeat_all_img, command=toggle_repeat_mode, bg="#15253F", bd=0)
repeat_button.place(relx=.75, rely=.85)

# Speed Slider
speed_slider = tk.Scale(root, from_=0.5, to=2.0, orient=tk.HORIZONTAL, command=set_speed, length=210, bg='#15253F', fg='white', troughcolor='gray')
speed_slider.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
speed_slider.set(1.0)

# Start the Tkinter event loop
root.mainloop()