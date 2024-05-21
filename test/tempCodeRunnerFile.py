def add_songs():
    song_paths = filedialog.askopenfilenames(title="Select Songs", filetypes=[("MP3 Files", "*.mp3","wav Files", "*.wav")])
    for song in song_paths:
        songs_listbox.insert(tk.END, song)