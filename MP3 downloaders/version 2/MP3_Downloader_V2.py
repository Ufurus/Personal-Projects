import tkinter as tk
import tkinter.messagebox

import os
import sys

if getattr(sys, 'frozen', False):
    ffmpeg_path = os.path.join(sys._MEIPASS, 'ffmpeg.exe')
else:
    ffmpeg_path = "ffmpeg.exe"

os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path

from moviepy import AudioFileClip
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

def error_message():
    tk.messagebox.showinfo("Error!", "Please enter a valid URL")

def completion_message():
    tk.messagebox.showinfo("Done!", "File downloaded")

def download_video(given_video_url):
    downloads = str(Path.home() / "Downloads")
    yt = YouTube(given_video_url, on_progress_callback=on_progress)
    ys = yt.streams.get_audio_only() # downloading mp3 only
    temp_file = ys.download(downloads) # downloads it as m4a

    base, ext = os.path.splitext(temp_file)
    mp3_file = base + ".mp3"

    audio_file = AudioFileClip(temp_file)
    audio_file.write_audiofile(mp3_file, codec='libmp3lame')

    audio_file.close()

    if os.path.exists(temp_file) and temp_file != mp3_file:
        os.remove(temp_file)

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