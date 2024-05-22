import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import simpleaudio as sa 
import threading

class AudioPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("WAV File Speed Adjuster")

        self.load_button = tk.Button(master, text="Load WAV File", command=self.load_file)
        self.load_button.pack()

        self.play_button = tk.Button(master, text="Play", state=tk.DISABLED, command=self.play_audio)
        self.play_button.pack()

        self.speed_slider = tk.Scale(master, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, label="Speed")
        self.speed_slider.set(1.0)
        self.speed_slider.pack()

        self.audio_segment = None
        self.playback_thread = None

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if file_path:
            self.audio_segment = AudioSegment.from_wav(file_path)
            self.play_button.config(state=tk.NORMAL)

    def play_audio(self):
        if self.audio_segment:
            speed = self.speed_slider.get()
            # Adjust speed
            playback_segment = self.audio_segment._spawn(self.audio_segment.raw_data, overrides={
                "frame_rate": int(self.audio_segment.frame_rate * speed)
            }).set_frame_rate(self.audio_segment.frame_rate)
            
            # Ensure there's no currently playing audio
            if self.playback_thread and self.playback_thread.is_alive():
                self.stop_audio()
                
            self.playback_thread = threading.Thread(target=play, args=(playback_segment,))
            self.playback_thread.start()

    def stop_audio(self):
        sa.stop_all()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()
