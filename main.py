#Required Libraries
import tkinter as tk
from tkinter import filedialog
import pygame
import os

#Initialized Pygame Mixture
pygame.mixer.init()

#Main Window
root=tk.Tk()
root.title("Music Player")
root.geometry("400x300")
root.resizable(False, False)

current_song=None
paused=False

#Functions
def load_song():
    global current_song
    song=filedialog.askopenfilename(
        filetypes=[("Audio Files","*.mp3 *.wav")]
    )
    if song:
        current_song=song
        song_label.config(text=os.path.basename(song))
def play_song():
    global paused
    if current_song:
        if paused:
            pygame.mixer.music.unpause()
            paused=False
        else:
            pygame.mixer.music.load(current_song)
            pygame.mixer.music.play()
def pause_song():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused=True
def stop_song():
    pygame.mixer.music.stop()
def set_volume(val):
    pygame.mixer.music.set_volume(float(val)/100)

#User Interface
song_label=tk.Label(root,text="No Song Selected!",font=("Arial",10))
song_label.pack(pady=10)

load_bth=tk.Button(root,text="Load Song",width=20,command=load_song)
load_bth.pack(pady=5) 

play_btn=tk.Button(root,text="Play Song",width=20,command=play_song)
play_btn.pack(pady=5)

pause_btn=tk.Button(root,text="Pause Song",width=20,command=pause_song)
pause_btn.pack(pady=5)

stop_btn=tk.Button(root,text="Stop Song",width=20,command=stop_song)
stop_btn.pack(pady=5)

volume_scale=tk.Scale(root,from_=0,to=100,orient=tk.HORIZONTAL,label="Volume",command=set_volume)
volume_scale.set(70)
volume_scale.pack(pady=10)

root.mainloop()