import tkinter as tk

def add_song():
    song = entry.get()
    # Add your code to handle the addition of the song here
    print("Song added:", song)

root = tk.Tk()
root.title("Python Audio Player")

# Create a frame for the song adding box
frame = tk.Frame(root, bg="blue", padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Add a label for instructions
label = tk.Label(frame, text="Add Song:", fg="white", bg="blue")
label.pack()

# Add an entry for user input
entry = tk.Entry(frame, bg="white")
entry.pack()

# Add a button to add the song
add_button = tk.Button(frame, text="Add", command=add_song, bg="white", fg="blue")
add_button.pack(pady=10)

root.mainloop()
