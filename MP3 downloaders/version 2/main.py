import tkinter as tk
from tkinter import messagebox as messagebox

from moviepy import AudioFileClip
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path
import glob
import os


def error_message():
    messagebox.showinfo("Error!", "Please enter a valid URL")

def completion_message():
    messagebox.showinfo("Done!", "File downloaded")

def download_video(given_video_url):
    downloads = str(Path.home() / "Downloads")
    yt = YouTube(given_video_url, on_progress_callback=on_progress)
    ys = yt.streams.get_audio_only() # downloading mp3 only
    ys.download(downloads)
    current_m4a_file = os.path.join(downloads, yt.title + ".m4a")
    mp3_file = yt.title + ".mp3"
    mp3_location = os.path.join(downloads, mp3_file)
    m4a_audio_file = AudioFileClip(os.path.join(downloads, current_m4a_file))
    m4a_audio_file.write_audiofile(mp3_location)
    os.remove(os.path.join(downloads, current_m4a_file))
    completion_message()

def url_checker():
    given_url = url_entry.get()
    if given_url.startswith("http") or given_url.startswith("https"):
        if "youtube.com" in given_url:
            download_video(given_url)
        else:
            error_message()
    else:
        error_message()

root = tk.Tk()

root.geometry("600x450")
root.title("MP3 Downloader")

label = tk.Label(root, text="MP3 Downloader")
root.eval('tk::PlaceWindow . center')

label.pack()
text_label = tk.Label(root, text="Enter URL link below")
text_label.pack()

url_entry = tk.Entry(root, width=70)
url_entry.pack()

download_button = tk.Button(root,
                            width=15,
                            text="Download",
                            background='blue',
                            foreground='white',
                            command=url_checker)
download_button.pack()

root.mainloop()