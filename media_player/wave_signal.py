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
        self.root.title("Audio Player with Dynamic Waveform and Frequency Spectrum")
        
        self.file_path = None
        self.audio_data = None
        self.sample_rate = None
        self.filtered_audio = None
        self.start_idx = 0
        self.buffer_size = 1024
        self.stream = None
        self.is_playing = False
        self.playback_speed = 1.0
        
        self.create_widgets()
    
    def create_widgets(self):
        # File selection button
        self.open_button = tk.Button(self.root, text="Open Audio File", command=self.open_file)
        self.open_button.pack(pady=10)
        
        # Create matplotlib figure and axis for waveform and spectrum
        self.fig, (self.ax_waveform, self.ax_spectrum) = plt.subplots(2, 1)
        self.x_waveform = np.arange(0, self.buffer_size)
        self.line_waveform, = self.ax_waveform.plot(self.x_waveform, np.random.rand(self.buffer_size))
        self.ax_waveform.set_ylim(-1, 1)
        self.ax_waveform.set_xlim(0, self.buffer_size)
        
        self.x_spectrum = np.fft.rfftfreq(self.buffer_size, d=1./self.sample_rate if self.sample_rate else 1)
        self.line_spectrum, = self.ax_spectrum.plot(self.x_spectrum, np.random.rand(len(self.x_spectrum)))
        self.ax_spectrum.set_ylim(0, 1)
        self.ax_spectrum.set_xlim(0, np.max(self.x_spectrum))
        
        # Create a canvas widget for matplotlib
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        
        # Play and Stop buttons
        self.play_button = tk.Button(self.root, text="Play", command=self.play_audio, state=tk.DISABLED)
        self.play_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_audio, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Speed buttons
        self.speed_up_button = tk.Button(self.root, text="Speed x2", command=self.double_speed, state=tk.DISABLED)
        self.speed_up_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.speed_down_button = tk.Button(self.root, text="Speed x0.5", command=self.halve_speed, state=tk.DISABLED)
        self.speed_down_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Low pass filter button
        self.lowpass_button = tk.Button(self.root, text="Apply Low Pass Filter", command=self.apply_lowpass_filter, state=tk.DISABLED)
        self.lowpass_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        # High pass filter button
        self.highpass_button = tk.Button(self.root, text="Apply High Pass Filter", command=self.apply_highpass_filter, state=tk.DISABLED)
        self.highpass_button.pack(side=tk.LEFT, padx=10, pady=10)
    
    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if self.file_path:
            self.load_audio()
            self.play_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.lowpass_button.config(state=tk.NORMAL)
            self.highpass_button.config(state=tk.NORMAL)
            self.speed_up_button.config(state=tk.NORMAL)
            self.speed_down_button.config(state=tk.NORMAL)
    
    def load_audio(self):
        self.audio_data, self.sample_rate = librosa.load(self.file_path, sr=None, mono=True)
        self.filtered_audio = self.audio_data.copy()  # Initialize filtered_audio with original audio
        self.start_idx = 0
        self.x_spectrum = np.fft.rfftfreq(self.buffer_size, d=1./self.sample_rate)
        self.ax_spectrum.set_xlim(0, np.max(self.x_spectrum))
    
    def audio_callback(self, outdata, frames, time, status):
        if self.start_idx < len(self.filtered_audio) - frames:
            chunk_size = int(frames * self.playback_speed)
            chunk = self.filtered_audio[self.start_idx:self.start_idx + chunk_size]
            if len(chunk) < frames:
                outdata[:len(chunk)] = chunk[:, None]
                outdata[len(chunk):] = 0
            else:
                outdata[:] = chunk[:frames][:, None]
            self.start_idx += chunk_size
        else:
            outdata.fill(0)
            self.stop_audio()
    
    def update_plot(self, frame):
        if self.start_idx < len(self.filtered_audio) - self.buffer_size:
            waveform_chunk = self.filtered_audio[self.start_idx:self.start_idx + self.buffer_size]
            self.line_waveform.set_ydata(waveform_chunk)
        
            spectrum_chunk = np.abs(np.fft.rfft(waveform_chunk))
            self.line_spectrum.set_ydata(spectrum_chunk)
        
            # Set the desired frequency range for display
            frequency_range = 0.5  # Modify the frequency range as desired
            self.ax_spectrum.set_xlim(0, frequency_range)
    
            return self.line_waveform, self.line_spectrum
    
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
    
    def apply_lowpass_filter(self):
        if self.filtered_audio is None:
            messagebox.showerror("Error", "No audio file loaded")
            return
        
        cutoff_freq = 2000  # Modify the cutoff frequency as desired
        
        nyquist = self.sample_rate / 2
        b, a = signal.butter(4, cutoff_freq / nyquist, btype='low')
        self.filtered_audio = signal.filtfilt(b, a, self.audio_data)
        self.start_idx = 0
    
    def apply_highpass_filter(self):
        if self.filtered_audio is None:
            messagebox.showerror("Error", "No audio file loaded")
            return
        
        cutoff_freq = 500  # Modify the cutoff frequency as desired
        
        nyquist = self.sample_rate / 2
        b, a = signal.butter(4, cutoff_freq / nyquist, btype='high')
        self.filtered_audio = signal.filtfilt(b, a, self.audio_data)
        self.start_idx = 0
    
    def double_speed(self):
        self.playback_speed = 2.0
    
    def halve_speed(self):
        self.playback_speed = 0.5

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
