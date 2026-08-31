import subprocess
import os
from yt_dlp import YoutubeDL

class WrongURL(Exception):
    pass

try:
    link = input("Enter URL: ")
    if len(link) != 43 or 'youtube.com' not in link:
        raise WrongURL("Enter a valid URL")
finally:
    url = [link]

with YoutubeDL() as ydl:
    ydl.download(url[0])

file_name = [i for i in os.listdir(os.getcwd()) if i.endswith(".webm")][0]
new_name = str(file_name[:file_name.index('[') - 1]) + '.mp4'

subprocess.run(["ffmpeg", '-i', file_name, '-c', 'copy', new_name])
os.remove(file_name)