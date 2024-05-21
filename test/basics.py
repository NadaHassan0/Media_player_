import pygame
import pygame
import tkinter as tk
from tkinter import filedialog

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def choose_audio_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        play_audio(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Audio Player")

    select_button = tk.Button(root, text="Select Audio File", command=choose_audio_file)
    select_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop Playback", command=pygame.mixer.music.stop)
    stop_button.pack()

    root.mainloop()
