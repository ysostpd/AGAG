import os
import tkinter
import wave
import time
import threading
import tkinter as tk
import pyaudio
import customtkinter
from PIL import ImageTk, Image
import pygame
from functions import *
import segmenter

'''
WELCOME TO PROTO 6.0
- IMPROVEMENTS
    - MULTI-WINDOWED
    - FILE READING 
    - NAMING CONVENTION FIXED
- UPDATES FOR PROTO 6
    - CHANGING WALLPAPER
    - LINE TO LINE TEXT READING
    - ROUNDED BUTTONS HEHEHE 
'''

pygame.mixer.init()

class VoiceRecorder(customtkinter.CTk):
    def __init__(self):
        # Preconfiguration of Main Frame
        self.root = tk.Tk()
        self.root.title("kathAwit 1.0")
        self.root.resizable(False, False)
        self.root.geometry("800x500")
        self.root.iconbitmap('resources/jukebox.ico')
        self.root.config(bg="#3c3f41")

        # Add image file
        bg = tkinter.PhotoImage(file="resources/bgi.png")

        # Show image using label
        lbl_bgimg = tkinter.Label(self.root, image=bg)
        lbl_bgimg.place(x=0, y=0)

        # Frame Setup
        self.fr_top = tkinter.Frame(bg="#3c3f41")
        self.fr_mid = tkinter.Frame(bg="#3c3f41")
        self.fr_bot = tkinter.Frame(bg="#3c3f41")
        self.fr_mid2 = tkinter.Frame(bg="#3c3f41")
        self.fr_hapit = tkinter.Frame(bg="#3c3f41") # temp only for tool defense
        self.fr_top.pack()
        self.fr_mid.pack()
        self.fr_hapit.pack()

# Setting Up the Elements
        # #=#=#=#=#= Calling Out Resources #=#=#=#=#=#=#
        img_rewind = tk.PhotoImage(file='resources/rewind50.png')
        img_convert = tk.PhotoImage(file='resources/guitar50.png')
        img_home = tk.PhotoImage(file='resources/home48.png')
        img_note = tk.PhotoImage(file='resources/note48.png')

        # #=#=#=#=#= Pre-existing Elements #=#=#=#=#=#=#
        self.my_img = Image.open("resources/logo.png")
        self.img_resized = self.my_img.resize((320, 96), Image.ANTIALIAS)
        self.my_img2 = ImageTk.PhotoImage(self.img_resized)
        self.lbl_logo = customtkinter.CTkLabel(self.fr_top, image=self.my_img2)
        self.lbl_HMM = customtkinter.CTkLabel(self.fr_top, text="via Long Short Term Memory\n (v. 1.0)",
                                              text_font=("Roboto Light", -12),
                                              text_color= "white")  # font name and size in px
        self.btn_rec = customtkinter.CTkButton(self.fr_mid,text="🎤", text_font=("Arial", 80), borderwidth=0,
                                              corner_radius=75, fg_color="red", hover_color="#400d04", text_color="white",
                                              command=self.cmd_rec)
        self.lbl_rec = customtkinter.CTkLabel(self.fr_mid,text="*click the microphone button to record*", text_color="white")

        # =#=#=#=#=#=#=#=# Elements that will pop up after command #=#=#=#=#=#=#+#=#+
        self.btn_replayraw = customtkinter.CTkButton(self.fr_bot, image=img_rewind, text="Replay", text_color="white",
                                               command=self.cmd_replayraw, fg_color="#85419b", hover_color="#3f154d")
        self.btn_convert = customtkinter.CTkButton(self.fr_bot, image=img_convert, text="Generate Accompaniment!",
                                                   text_color="white", command=self.cmd_convert,
                                                   fg_color="#85419b", hover_color="#3f154d")

        # =#=#=#=#=#=#=#=# Accompaniment Tab Elements #=#=#=#=#=#=#+#=#+
        self.btn_replayconverted = customtkinter.CTkButton(self.fr_mid2, image=img_rewind, text="Replay Converted Audio", text_color="white",
                                                     command=self.cmd_replayraw, fg_color="#85419b", hover_color="#3f154d")
        self.btn_home = customtkinter.CTkButton(self.fr_mid2, image=img_home, text="Home",
                                                   text_color="white",command=self.cmd_home,
                                                   fg_color="#85419b", hover_color="#3f154d" )
        self.btn_showchords = customtkinter.CTkButton(self.fr_mid2, image=img_note, text="Show Chord Progression",
                                                text_color="white", command=self.cmd_showchords,
                                                fg_color="#85419b", hover_color="#3f154d")
        self.lbl_chords = customtkinter.CTkLabel(self.fr_mid2, text="-", text_color="white", text_font=("Arial", 15))

        # Implementing pre-existing Elements
        self.lbl_logo.grid(row=0, column=0, pady=(10,0))
        self.lbl_HMM.grid(row=1, column=0, padx=10, pady=10)
        self.btn_rec.grid(row=0, column=0, padx=10)
        self.lbl_rec.grid(row=1, column=0, padx=10, pady=10)

        # Implementing Accompaniment Tab Elements
        self.lbl_chords.grid(row=0, column=1, padx=10, pady=10)
        self.btn_replayconverted.grid(row=2, column=0, padx=10, pady=10)
        self.btn_showchords.grid(row=2, column=1, padx=10, pady=10)
        self.btn_home.grid(row=2, column=2, padx=10)

# =#=#=#=#=#=#=#=#=# COMMANDS COMMANDS COMMANDS COMMANDS COMMANDS COMMANDS COMMANDS COMMANDS COMMANDS COMMANDS COMMANDS COMMANDS  #=#=#=#=#=#=#=#=#=#
        self.recording = False
        self.root.mainloop()
    def cmd_rec(self):
        pygame.mixer.music.stop()
        if self.recording:
            self.recording = False
        else:
            self.recording = True
            self.btn_rec.configure(text_color="red")
            threading.Thread(target=self.record).start()

    # not called by button. and tumatawag dito si cmd_rec
    def record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100,
                            input=True, frames_per_buffer=1024)
        frames = []
        start = time.time()
        while self.recording:
            self.fr_bot.forget()
            data = stream.read(1024)
            frames.append(data)
            passed = time.time() - start
            secs = passed % 60
            mins = passed // 60
        # animation only
            rcdg = "Recording.."
            if int(secs) % 2 == 0:
                self.btn_rec.configure(text_color="#ebd8d5")
                rcdg = "Recording.."
            else:
                self.btn_rec.configure(text_color="white")
                rcdg = "Recording..."
            self.lbl_rec.configure(text=f"{rcdg}\n{int(mins):02d}:{int(secs):02d}")
        stream.stop_stream()
        stream.close()
        audio.terminate()
        exists = True
        i = 1  #not so efficient as per reference
        while exists:
            if os.path.exists(f"Proto/recording{i}.wav"):
                i += 1
            else:
                exists = False
        self.lbl_rec.configure(text=f"Recorded!\n File saved as recording{i}.wav")
        self.fr_bot.pack(pady=20)
        self.btn_replayraw.grid(row=0, column=0, padx=10)
        self.btn_convert.grid(row=0, column=4, padx=2)
        self.btn_rec.configure(text_color="white")

        # Recording Shits
        sound_file = wave.open(f"Proto/recording{i}.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        sound_file.close()

    def cmd_replayraw(self):
        exists = True
        i = 1  # not so efficient as per reference
        while exists:
            if os.path.exists(f"Proto/recording{i}.wav"):
                i += 1
            else:
                exists = False
        song = f'Proto/recording{i-1}.wav'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

    def cmd_convert(self):
        pygame.mixer.music.stop()
        self.lbl_rec.configure(text="*click the microphone button to record*")
        self.fr_mid.forget()
        self.fr_bot.forget()
        self.fr_mid2.pack()

        segmenter.cmd_segmentor()

    def cmd_home(self):
        self.fr_mid2.forget()
        self.fr_mid.pack()

    def cmd_replayconverted(self):
        pass

    def cmd_showchords(self):

    # File Handling for Chord Display
        f_notes = open("resources/notes.txt", "r")
        self.lbl_chords.configure(text=f"{f_notes.read()}")
        f_notes.close()

    def cmd_segmenter(self):
        pass

VoiceRecorder()