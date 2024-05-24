import numpy as np
import scipy.signal as signal
import sounddevice as sd
import librosa
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog, messagebox

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player with Dynamic Waveform")
        
        self.file_path = None
        self.audio_data = None
        self.sample_rate = None
        self.filtered_audio = None
        self.start_idx = 0
        self.buffer_size = 1024
        self.stream = None
        self.is_playing = False
        
        self.create_widgets()
    
    def create_widgets(self):
        # File selection button
        self.open_button = tk.Button(self.root, text="Open Audio File", command=self.open_file)
        self.open_button.pack(pady=10)
        
        # Create matplotlib figure and axis
        self.fig, self.ax = plt.subplots()
        self.x = np.arange(0, self.buffer_size)
        self.line, = self.ax.plot(self.x, np.random.rand(self.buffer_size))
        self.ax.set_ylim(-1, 1)
        self.ax.set_xlim(0, self.buffer_size)
        
        # Create a canvas widget for matplotlib
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        
        # Play and Stop buttons
        self.play_button = tk.Button(self.root, text="Play", command=self.play_audio, state=tk.DISABLED)
        self.play_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_audio, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT, padx=10, pady=10)
    
    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if self.file_path:
            self.load_audio()
            self.play_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
    
    def load_audio(self):
        self.audio_data, self.sample_rate = librosa.load(self.file_path, sr=None, mono=True)
        nyquist = self.sample_rate / 2
        low_freq = 300
        high_freq = 3000
        b, a = signal.butter(4, [low_freq / nyquist, high_freq / nyquist], btype='band')
        self.filtered_audio = signal.filtfilt(b, a, self.audio_data)
        self.start_idx = 0
    
    def audio_callback(self, outdata, frames, time, status):
        if self.start_idx < len(self.filtered_audio) - frames:
            outdata[:, 0] = self.filtered_audio[self.start_idx:self.start_idx + frames]
            self.start_idx += frames
        else:
            outdata[:, 0] = np.zeros(frames)
            self.stop_audio()  # Stop when the audio finishes
    
    def update_plot(self, frame):
        if self.start_idx < len(self.filtered_audio) - self.buffer_size:
            self.line.set_ydata(self.filtered_audio[self.start_idx:self.start_idx + self.buffer_size])
        return self.line,
    
    def play_audio(self):
        if self.filtered_audio is None:
            messagebox.showerror("Error", "No audio file loaded")
            return
        if self.is_playing:
            return
        
        self.is_playing = True
        self.start_idx = 0  # Reset start index for playback
        
        self.stream = sd.OutputStream(callback=self.audio_callback, channels=1, samplerate=self.sample_rate, blocksize=self.buffer_size)
        self.stream.start()
        
        self.ani = animation.FuncAnimation(self.fig, self.update_plot, interval=50, blit=True)
        self.canvas.draw_idle()
    
    def stop_audio(self):
        if self.stream is not None:
            self.stream.stop()
            self.stream.close()
            self.stream = None
        
        self.is_playing = False
        
        if hasattr(self, 'ani'):
            self.ani.event_source.stop()
    
    def on_closing(self):
        self.stop_audio()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
